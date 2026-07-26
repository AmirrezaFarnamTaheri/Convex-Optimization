/**
 * widgets-loader.js — optional convention-based widget mounter.
 *
 * Lecture pages normally mount widgets explicitly with an inline module script
 * at the bottom of the page (see docs/WIDGETS.md section 1.1):
 *
 *   <script type="module">
 *     import { initConvexCombination } from './widgets/js/convex-combination.js';
 *     initConvexCombination('widget-convex-combination');
 *   </script>
 *
 * That explicit form stays the default: it is greppable, it fails loudly, and it
 * keeps each page's widget set obvious. This loader exists for pages that would
 * otherwise repeat the same boilerplate many times. Opt in per element:
 *
 *   <div id="widget-gd-vs-newton" data-widget="gd-vs-newton"></div>
 *   <script type="module">
 *     import { mountWidgets } from '../../static/js/widgets-loader.js';
 *     mountWidgets();
 *   </script>
 *
 * Only elements carrying an explicit data-widget attribute are touched, so this
 * never double-mounts a widget that an inline script already initialized.
 *
 * Module resolution: data-widget="gd-vs-newton" loads ./widgets/js/gd-vs-newton.js
 * (relative to the lecture page) and calls its init export. The export name is
 * derived as init + PascalCase(name), matching the naming rule in
 * docs/WIDGETS.md section 2; a module with a single named export or a default
 * export also works.
 */

const pascalCase = (name) =>
  name
    .split(/[-_]/)
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join('');

function resolveInit(module, widgetName) {
  const expected = `init${pascalCase(widgetName)}`;
  if (typeof module[expected] === 'function') return module[expected];

  if (typeof module.default === 'function') return module.default;

  // Fall back to a lone named export (covers casing variants like initGDvsNewton).
  const fns = Object.keys(module).filter((k) => typeof module[k] === 'function');
  if (fns.length === 1) return module[fns[0]];

  return null;
}

/**
 * Mount every element carrying a data-widget attribute.
 *
 * @param {object}     [options]
 * @param {ParentNode} [options.root=document]           Subtree to scan.
 * @param {string}     [options.basePath='./widgets/js'] Module directory,
 *        resolved relative to the page, not to this script.
 * @returns {Promise<Array<{name: string, id: string, ok: boolean, error?: Error}>>}
 *        One result per element, so callers can assert on the outcome.
 */
export async function mountWidgets({ root = document, basePath = './widgets/js' } = {}) {
  const targets = Array.from(root.querySelectorAll('[data-widget]'));

  return Promise.all(
    targets.map(async (el) => {
      const name = el.dataset.widget;
      const id = el.id;

      if (!id) {
        const error = new Error(`[widgets-loader] element with data-widget="${name}" has no id`);
        console.error(error.message);
        return { name, id, ok: false, error };
      }

      if (el.dataset.widgetMounted === 'true') {
        return { name, id, ok: true };
      }

      try {
        const module = await import(`${basePath}/${name}.js`);
        const init = resolveInit(module, name);

        if (!init) {
          throw new Error(
            `no init export found (expected init${pascalCase(name)}); ` +
              `module exports: ${Object.keys(module).join(', ') || '(none)'}`
          );
        }

        init(id);
        el.dataset.widgetMounted = 'true';
        return { name, id, ok: true };
      } catch (error) {
        console.error(`[widgets-loader] failed to mount "${name}" into #${id}:`, error);
        return { name, id, ok: false, error };
      }
    })
  );
}

export default mountWidgets;
