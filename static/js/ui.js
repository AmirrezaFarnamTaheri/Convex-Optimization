/**
 * UI Enhancements for Convex Optimization Course
 * Handles:
 * - Collapsible Environment Boxes (Proofs, Examples, Solutions)
 * - Hierarchical Section/Subsection Toggling
 * - Page Settings (Font Size, Global Toggles, Layout)
 * - Sidebar/TOC Toggling & Resizing
 * - Theme Switching (via theme-switcher.js)
 */

/* =========================================
   0. CONTROL DOCK (New Centralized Toolbar)
   ========================================= */
class ControlDock {
    constructor() {
        if (document.querySelector('.control-dock')) return;

        this.dock = document.createElement('div');
        this.dock.className = 'control-dock';
        document.body.appendChild(this.dock);
    }

    addButton(id, icon, title, onClick, position = 'end') {
        if (document.getElementById(id)) return document.getElementById(id);

        const btn = document.createElement('button');
        btn.id = id;
        btn.className = 'dock-btn';
        btn.innerHTML = icon.startsWith('<') ? icon : `<i data-feather="${icon}"></i>`;
        btn.setAttribute('data-title', title);
        btn.setAttribute('aria-label', title);

        btn.addEventListener('click', (e) => {
            onClick(e, btn);
        });

        if (position === 'start') {
            this.dock.insertBefore(btn, this.dock.firstChild);
        } else {
            this.dock.appendChild(btn);
        }

        if (typeof feather !== 'undefined') feather.replace();
        return btn;
    }
}

function initControlDock() {
    window.controlDock = new ControlDock();
    // Dispatch event for other scripts
    window.dispatchEvent(new Event('convex-dock-ready'));
}

// Immediate initialization if possible, else on DOMContentLoaded
if (document.body) {
    initControlDock();
} else {
    document.addEventListener('DOMContentLoaded', initControlDock);
}

document.addEventListener('DOMContentLoaded', () => {
    // 2. Initialize Components
    initCollapsibleEnvironments();
    initHierarchicalSections();
    initPageSettings();
    initHeaderFontSize();
    initSidebarToggle();
    initBackToTop();
    initResizableSidebar();

    if (typeof feather !== 'undefined') feather.replace();
});


/* =========================================
   1. COLLAPSIBLE ENVIRONMENTS
   ========================================= */
function initCollapsibleEnvironments() {
    const collapsibleSelectors = [
        { selector: '.theorem-box', defaultCollapsed: false, label: 'Theorem' },
        { selector: '.proof-box', defaultCollapsed: true, label: 'Proof' },
        { selector: '.solution-box', defaultCollapsed: true, label: 'Solution' },
        { selector: '.answer', defaultCollapsed: true, label: 'Answer' },
        { selector: '.recap-box', defaultCollapsed: true, label: 'Recap' },
        { selector: '.example', defaultCollapsed: false, label: 'Example' },
        { selector: '.example-box', defaultCollapsed: false, label: 'Example' },
        { selector: '.intuition-box', defaultCollapsed: false, label: 'Intuition' },
        { selector: '.interpretation-box', defaultCollapsed: false, label: 'Interpretation' }
    ];

    collapsibleSelectors.forEach(config => {
        document.querySelectorAll(config.selector).forEach(box => {
            makeCollapsible(box, config.defaultCollapsed, config.label);
        });
    });
}

function makeCollapsible(box, defaultCollapsed, label) {
    if (box.querySelector('.env-toggle-btn')) return;

    // Wrap content
    const contentWrapper = document.createElement('div');
    contentWrapper.className = 'env-collapsible-content';
    // Initially explicit height handling often helps smooth transitions,
    // but CSS typically handles max-height: 0 vs scrollHeight.
    
    while (box.firstChild) {
        contentWrapper.appendChild(box.firstChild);
    }
    box.appendChild(contentWrapper);

    // Toggle Button
    const btn = document.createElement('button');
    btn.className = 'env-toggle-btn';
    // Use feather icons if available, else text fallback
    btn.innerHTML = defaultCollapsed ? '<i data-feather="chevron-down"></i>' : '<i data-feather="chevron-up"></i>';
    btn.setAttribute('aria-label', 'Toggle ' + label);
    btn.setAttribute('title', 'Toggle ' + label);
    // Style adjustments for the button are in CSS (absolute top-right)

    box.appendChild(btn);

    if (defaultCollapsed) {
        box.classList.add('env-collapsed');
        contentWrapper.style.display = 'none'; // Hard hide initially to prevent layout jumps
    } else {
        contentWrapper.style.display = 'block';
    }

    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isCollapsed = box.classList.toggle('env-collapsed');
        
        // Handling display for animation
        if (isCollapsed) {
            contentWrapper.style.display = 'none';
            btn.innerHTML = '<i data-feather="chevron-down"></i>';
        } else {
            contentWrapper.style.display = 'block';
            btn.innerHTML = '<i data-feather="chevron-up"></i>';
        }
        
        if (typeof feather !== 'undefined') feather.replace();
    });
}


/* =========================================
   2. HIERARCHICAL SECTIONS
   ========================================= */
function initHierarchicalSections() {
    // Process Level 1: Sections (.section-card with h2)
    const cards = document.querySelectorAll('.section-card');

    cards.forEach(card => {
        if (card.classList.contains('lecture-header')) return;

        const h2 = card.querySelector('h2');
        if (!h2) return;

        // Group content after H2
        const contentWrapper = document.createElement('div');
        contentWrapper.className = 'hierarchical-content';

        let next = h2.nextSibling;
        const toMove = [];
        while (next) {
            toMove.push(next);
            next = next.nextSibling;
        }
        toMove.forEach(el => contentWrapper.appendChild(el));
        card.appendChild(contentWrapper);

        // Setup H2 Toggle
        card.classList.add('hierarchical-section'); 
        h2.style.cursor = 'pointer';
        h2.classList.add('section-toggle');
        
        const originalText = h2.innerHTML;
        // Check if icon already exists to avoid duplication on re-run
        if (!h2.querySelector('.toggle-icon')) {
            h2.innerHTML = `<span class="toggle-icon" style="margin-right:8px; display:inline-block;"><i data-feather="chevron-down"></i></span><span class="header-text">${originalText}</span>`;
        }

        h2.addEventListener('click', () => {
            const isCollapsed = card.classList.toggle('collapsed');
            const icon = h2.querySelector('.toggle-icon');
            
            if (isCollapsed) {
                 contentWrapper.classList.add('hidden');
            } else {
                 contentWrapper.classList.remove('hidden');
            }

            if (icon) {
                icon.innerHTML = isCollapsed ? '<i data-feather="chevron-right"></i>' : '<i data-feather="chevron-down"></i>';
                if (typeof feather !== 'undefined') feather.replace();
            }
        });

        // Process Level 2: Subsections (h3 inside contentWrapper)
        groupSubsections(contentWrapper);
    });
}

function groupSubsections(container) {
    const children = Array.from(container.childNodes);
    if (children.length === 0) return;

    // Check if there are any H3s to group
    const hasH3 = children.some(c => c.nodeType === 1 && c.tagName === 'H3');
    if (!hasH3) return;

    // Create a new fragment to rebuild content
    const fragment = document.createDocumentFragment();
    let currentSubsection = null;
    let currentContent = null;

    children.forEach(child => {
        if (child.nodeType === 1 && child.tagName === 'H3') {
            // New Subsection Found
            const h3 = child;

            currentSubsection = document.createElement('div');
            currentSubsection.className = 'hierarchical-section hierarchical-subsection';

            // Setup H3 Toggle
            h3.style.cursor = 'pointer';
            const originalText = h3.innerHTML;
            h3.innerHTML = `<span class="toggle-icon" style="margin-right:8px; display:inline-block;"><i data-feather="chevron-down"></i></span>${originalText}`;

            currentContent = document.createElement('div');
            currentContent.className = 'hierarchical-content';

            h3.addEventListener('click', (e) => {
                e.stopPropagation();
                const isCollapsed = currentSubsection.classList.toggle('collapsed');
                
                if (isCollapsed) {
                    currentContent.classList.add('hidden');
                } else {
                    currentContent.classList.remove('hidden');
                }

                const icon = h3.querySelector('.toggle-icon');
                if (icon) {
                    icon.innerHTML = isCollapsed ? '<i data-feather="chevron-right"></i>' : '<i data-feather="chevron-down"></i>';
                    if (typeof feather !== 'undefined') feather.replace();
                }
            });

            currentSubsection.appendChild(h3);
            currentSubsection.appendChild(currentContent);
            fragment.appendChild(currentSubsection);

        } else {
            // Content node
            if (currentContent) {
                currentContent.appendChild(child);
            } else {
                // Orphan content before first H3
                fragment.appendChild(child);
            }
        }
    });

    // Replace container content
    container.innerHTML = '';
    container.appendChild(fragment);
}


/* =========================================
   3. PAGE SETTINGS (Font Size, Global Toggles)
   ========================================= */
function initHeaderFontSize() {
    // Deprecated in new design - font size control moved to settings panel
    // Keeping function structure if called, but implementation merged into initPageSettings
}

function initPageSettings() {
    if (document.getElementById('page-settings-panel')) return;

    const panel = document.createElement('div');
    panel.id = 'page-settings-panel';
    panel.className = 'section-card';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Page Settings');
    panel.style.position = 'fixed';
    panel.style.bottom = '80px';
    panel.style.left = '20px';
    panel.style.width = '320px';
    panel.style.maxHeight = '80vh';
    panel.style.overflowY = 'auto';
    panel.style.zIndex = '1032';
    panel.style.display = 'none';
    panel.style.padding = 'var(--space-4)';
    panel.style.margin = '0';

    panel.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:var(--space-4); border-bottom:1px solid var(--border-subtle); padding-bottom:var(--space-2);">
            <h4 style="margin:0; font-size:var(--text-base);">Settings</h4>
            <button class="btn btn-ghost btn-xs" id="close-settings" aria-label="Close Settings"><i data-feather="x"></i></button>
        </div>

        <div class="control-group" style="margin-bottom: var(--space-4);">
            <label>Layout & View</label>
            <button class="btn btn-secondary btn-sm" id="toggle-focus-mode" style="width: 100%; margin-bottom: 8px;"><i data-feather="eye"></i> Focus Mode</button>
            <button class="btn btn-secondary btn-sm" id="toggle-fullscreen" style="width: 100%;"><i data-feather="maximize"></i> Full Screen</button>
        </div>

        <div class="control-group" style="margin-bottom: var(--space-4);">
            <label>Content Width</label>
            <div style="display:flex; gap:8px;">
                <button class="btn btn-secondary btn-sm" id="width-std" style="flex:1;">Standard</button>
                <button class="btn btn-secondary btn-sm" id="width-wide" style="flex:1;">Wide</button>
            </div>
        </div>`;
    body.appendChild(typeSec);

    // --- Layout Section ---
    const layoutSec = document.createElement('div');
    layoutSec.className = 'settings-section';
    layoutSec.innerHTML = `<span class="settings-title">Layout</span>
        <div class="settings-row" style="flex-direction:column; align-items:flex-start;">
            <div style="display:flex; justify-content:space-between; width:100%; margin-bottom:8px;">
                <label>Max Width</label>
                <span id="width-val" style="font-size:var(--text-xs); color:var(--text-tertiary);">1200px</span>
            </div>
            <input type="range" id="layout-width" min="800" max="2000" step="50" value="1200" aria-label="Content Width">
        </div>

        <div class="control-group" style="margin-bottom: var(--space-4);">
            <label>Typography</label>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:0.8em; color:var(--text-tertiary);">Font Size</span>
                <div style="display:flex; gap:4px;">
                    <button class="btn btn-secondary btn-sm" id="font-dec" aria-label="Decrease Font Size"><i data-feather="minus"></i></button>
                    <button class="btn btn-ghost btn-sm" id="font-reset" aria-label="Reset Font Size">Reset</button>
                    <button class="btn btn-secondary btn-sm" id="font-inc" aria-label="Increase Font Size"><i data-feather="plus"></i></button>
                </div>
            </div>
             <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.8em; color:var(--text-tertiary);">Line Height</span>
                 <div style="display:flex; gap:4px;">
                    <button class="btn btn-secondary btn-sm" id="lh-tight">S</button>
                    <button class="btn btn-secondary btn-sm" id="lh-normal">M</button>
                    <button class="btn btn-secondary btn-sm" id="lh-relaxed">L</button>
                </div>
            </div>
        </div>

        <div class="control-group" style="margin-bottom: var(--space-4);">
            <label>Content Visibility</label>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                 <label style="display:flex; align-items:center; gap:6px; font-weight:normal; cursor:pointer;">
                    <input type="checkbox" id="show-proofs" checked> Proofs
                 </label>
                 <label style="display:flex; align-items:center; gap:6px; font-weight:normal; cursor:pointer;">
                    <input type="checkbox" id="show-solutions" checked> Solutions
                 </label>
                 <label style="display:flex; align-items:center; gap:6px; font-weight:normal; cursor:pointer;">
                    <input type="checkbox" id="show-examples" checked> Examples
                 </label>
                 <label style="display:flex; align-items:center; gap:6px; font-weight:normal; cursor:pointer;">
                    <input type="checkbox" id="show-theorems" checked> Theorems
                 </label>
            </div>
        </div>

        <div class="control-group" style="margin-bottom: var(--space-4);">
            <label>Structure</label>
            <div style="display:flex; gap:8px;">
                <button class="btn btn-secondary btn-sm" id="sections-expand" style="flex:1;">Expand All</button>
                <button class="btn btn-secondary btn-sm" id="sections-collapse" style="flex:1;">Collapse</button>
            </div>
            <input type="range" id="layout-padding" min="0" max="6" step="0.5" value="1.5" aria-label="Page Padding">
        </div>`;
    body.appendChild(layoutSec);

    // --- Visibility Section ---
    const visSec = document.createElement('div');
    visSec.className = 'settings-section';
    visSec.innerHTML = `<span class="settings-title">Visibility</span>
        <div class="settings-row">
            <label>Header</label>
            <label class="switch">
                <input type="checkbox" id="toggle-header" checked>
                <span class="slider"></span>
            </label>
        </div>
        <div class="settings-row">
            <label>Sidebar</label>
            <label class="switch">
                <input type="checkbox" id="toggle-sidebar" checked>
                <span class="slider"></span>
            </label>
        </div>
    `;
    
    document.body.appendChild(panel);

    // --- Event Logic ---

    // Toggle Panel
    let triggerBtn;
    if (window.controlDock) {
        triggerBtn = window.controlDock.addButton(
            'settings-trigger',
            'settings',
            'Page Settings',
            () => {
                if (panel.style.display === 'block') {
                    panel.style.display = 'none';
                    triggerBtn.classList.remove('active');
                } else {
                    panel.style.display = 'block';
                    triggerBtn.classList.add('active');
                }
            }
        );
    } else {
        // Fallback if no dock (Legacy Floating Button)
        triggerBtn = document.createElement('button');
        triggerBtn.className = 'btn btn-primary';
        triggerBtn.style.position = 'fixed';
        triggerBtn.style.bottom = '20px';
        triggerBtn.style.left = '20px';
        triggerBtn.style.zIndex = '1031';
        triggerBtn.style.borderRadius = '50%';
        triggerBtn.style.width = '48px';
        triggerBtn.style.height = '48px';
        triggerBtn.style.padding = '0';
        triggerBtn.style.display = 'flex';
        triggerBtn.style.alignItems = 'center';
        triggerBtn.style.justifyContent = 'center';
        triggerBtn.style.boxShadow = 'var(--shadow-lg)';
        triggerBtn.title = 'Page Settings';
        triggerBtn.innerHTML = '<i data-feather="settings"></i>';
        document.body.appendChild(triggerBtn);

        triggerBtn.addEventListener('click', () => {
            if (panel.style.display === 'block') {
                panel.style.display = 'none';
                triggerBtn.classList.remove('active');
            } else {
                panel.style.display = 'block';
                triggerBtn.classList.add('active');
            }
        });
    }

    document.getElementById('close-settings').addEventListener('click', () => {
        panel.style.display = 'none';
        if (triggerBtn) triggerBtn.classList.remove('active');
    });

    // 1. Font Size
    const root = document.documentElement;
    const sizes = ['0.875rem', '0.9375rem', '1rem', '1.125rem', '1.25rem', '1.375rem', '1.5rem'];
    const defaultIndex = 2; // 1rem
    let currentIndex = defaultIndex;

    // Load saved settings
    const savedFont = localStorage.getItem('font-size-index');
    if (savedFont !== null) {
        currentIndex = parseInt(savedFont, 10);
        root.style.setProperty('--text-base', sizes[currentIndex]);
    }

    // Width Logic
    const setWidth = (wide) => {
        root.style.setProperty('--container-width', wide ? '1600px' : '1200px');
        document.getElementById('width-std').classList.toggle('active', !wide);
        document.getElementById('width-wide').classList.toggle('active', wide);
        localStorage.setItem('container-wide', wide);
    };
    const savedWide = localStorage.getItem('container-wide') === 'true';
    setWidth(savedWide);

    document.getElementById('width-std').onclick = () => setWidth(false);
    document.getElementById('width-wide').onclick = () => setWidth(true);

    // Line Height Logic
    const setLineHeight = (val, btnId) => {
        root.style.setProperty('--line-height', val);
        ['lh-tight', 'lh-normal', 'lh-relaxed'].forEach(id => {
            document.getElementById(id).classList.toggle('active', id === btnId);
        });
        localStorage.setItem('line-height-id', btnId);
    };
    const savedLH = localStorage.getItem('line-height-id') || 'lh-normal';
    const lhMap = { 'lh-tight': '1.25', 'lh-normal': '1.6', 'lh-relaxed': '1.8' };
    setLineHeight(lhMap[savedLH], savedLH);

    document.getElementById('lh-tight').onclick = () => setLineHeight('1.25', 'lh-tight');
    document.getElementById('lh-normal').onclick = () => setLineHeight('1.6', 'lh-normal');
    document.getElementById('lh-relaxed').onclick = () => setLineHeight('1.8', 'lh-relaxed');


    const updateFont = () => {
        root.style.setProperty('--text-base', sizes[fontIndex]);
        document.getElementById('font-display').textContent = percentages[fontIndex];
        localStorage.setItem('font-size-index', fontIndex);
    };
    updateFont(); // Init

    document.getElementById('font-dec').addEventListener('click', () => {
        if (fontIndex > 0) { fontIndex--; updateFont(); }
    });
    document.getElementById('font-inc').addEventListener('click', () => {
        if (fontIndex < sizes.length - 1) { fontIndex++; updateFont(); }
    });

    // 2. Layout
    const widthInput = document.getElementById('layout-width');
    const paddingInput = document.getElementById('layout-padding');
    const widthVal = document.getElementById('width-val');
    const paddingVal = document.getElementById('padding-val');

    // Load saved
    const savedWidth = localStorage.getItem('layout-width') || '1200';
    const savedPadding = localStorage.getItem('layout-padding') || '1.5';

    const setWidth = (val) => {
        root.style.setProperty('--container-max-width', val + 'px');
        root.style.setProperty('--lecture-max-width', (parseInt(val) + 400) + 'px'); // Lecture container wider
        widthVal.textContent = val + 'px';
        localStorage.setItem('layout-width', val);
    };

    const setPadding = (val) => {
        root.style.setProperty('--page-padding', val + 'rem');
        paddingVal.textContent = val + 'rem';
        localStorage.setItem('layout-padding', val);
    };

    widthInput.value = savedWidth;
    setWidth(savedWidth);
    widthInput.addEventListener('input', (e) => setWidth(e.target.value));

    paddingInput.value = savedPadding;
    setPadding(savedPadding);
    paddingInput.addEventListener('input', (e) => setPadding(e.target.value));

    // 3. Visibility
    const toggleHeader = document.getElementById('toggle-header');
    const toggleSidebar = document.getElementById('toggle-sidebar');
    const toggleFooter = document.getElementById('toggle-footer');

    const setVisibility = (key, el, cssVar, displayVal = 'block') => {
        const isVisible = localStorage.getItem(key) !== 'false'; // Default true
        el.checked = isVisible;
        root.style.setProperty(cssVar, isVisible ? displayVal : 'none');

        el.addEventListener('change', (e) => {
            const checked = e.target.checked;
            root.style.setProperty(cssVar, checked ? displayVal : 'none');
            localStorage.setItem(key, checked);
        });
    };

    setVisibility('show-header', toggleHeader, '--header-display', 'flex');
    setVisibility('show-sidebar', toggleSidebar, '--sidebar-display', 'block');
    setVisibility('show-footer', toggleFooter, '--footer-display', 'block');

    // 4. Actions
    const fsBtn = document.getElementById('toggle-fullscreen');
    if (fsBtn) {
        fsBtn.addEventListener('click', () => {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen();
                fsBtn.innerHTML = '<i data-feather="minimize"></i> Exit Full Screen';
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                    fsBtn.innerHTML = '<i data-feather="maximize"></i> Full Screen';
                }
            }
            if (typeof feather !== 'undefined') feather.replace();
        });
    }

    // Focus Mode
    const focusBtn = document.getElementById('toggle-focus-mode');
    focusBtn.onclick = () => {
        document.body.classList.toggle('focus-mode');
        const active = document.body.classList.contains('focus-mode');
        focusBtn.classList.toggle('active', active);
        if (active) {
            focusBtn.innerHTML = '<i data-feather="eye-off"></i> Exit Focus';
        } else {
             focusBtn.innerHTML = '<i data-feather="eye"></i> Focus Mode';
        }
        if (typeof feather !== 'undefined') feather.replace();
    };

    // Global Visibility Toggles
    const setupVisibilityToggle = (id, className) => {
        const checkbox = document.getElementById(id);
        const toggle = () => {
            if (checkbox.checked) document.body.classList.remove(className);
            else document.body.classList.add(className);
            localStorage.setItem(id, checkbox.checked);
        };

        const saved = localStorage.getItem(id);
        if (saved !== null) {
            checkbox.checked = saved === 'true';
            toggle();
        }

        checkbox.onchange = toggle;
    };

    setupVisibilityToggle('show-proofs', 'hide-proofs');
    setupVisibilityToggle('show-solutions', 'hide-solutions');
    setupVisibilityToggle('show-examples', 'hide-examples');
    setupVisibilityToggle('show-theorems', 'hide-theorems');


    // Global Toggles
    const toggleSections = (expand) => {
        document.querySelectorAll('.hierarchical-section').forEach(sec => {
            const h = sec.querySelector('h2, h3');
            const icon = h ? h.querySelector('.toggle-icon') : null;
            const content = sec.querySelector('.hierarchical-content');

            if (expand) {
                sec.classList.remove('collapsed');
                if (content) content.classList.remove('hidden');
                if (icon) icon.innerHTML = '<i data-feather="chevron-down"></i>';
            } else {
                sec.classList.add('collapsed');
                if (content) content.classList.add('hidden');
                if (icon) icon.innerHTML = '<i data-feather="chevron-right"></i>';
            }
        });
        
        // Also toggle Proofs/Boxes
        const selector = '.proof-box, .solution-box, .recap-box, .answer';
        document.querySelectorAll(selector).forEach(box => {
            const btn = box.querySelector('.env-toggle-btn');
            const content = box.querySelector('.env-collapsible-content');
            
            if (expand) {
                box.classList.remove('env-collapsed');
                if (content) content.style.display = 'block';
                if (btn) btn.innerHTML = '<i data-feather="chevron-up"></i>';
            } else {
                box.classList.add('env-collapsed');
                if (content) content.style.display = 'none';
                if (btn) btn.innerHTML = '<i data-feather="chevron-down"></i>';
            }
        });

        if (typeof feather !== 'undefined') feather.replace();
    };

    document.getElementById('sections-expand').addEventListener('click', () => toggleSections(true));
    document.getElementById('sections-collapse').addEventListener('click', () => toggleSections(false));

    if (typeof feather !== 'undefined') feather.replace();
}


/* =========================================
   4. SIDEBAR TOGGLE & RESIZING
   ========================================= */
function initSidebarToggle() {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;

    // 1. Mobile Dock Toggle
    if (window.controlDock) {
        const dockBtn = window.controlDock.addButton(
            'sidebar-toggle-dock',
            'menu',
            'Toggle Sidebar',
            () => {
                sidebar.classList.toggle('active');
                // Mobile style logic
                if (sidebar.classList.contains('active')) {
                     sidebar.style.position = 'fixed';
                     sidebar.style.top = '72px';
                     sidebar.style.left = '0';
                     sidebar.style.height = 'calc(100vh - 72px)';
                     sidebar.style.width = '80%';
                     sidebar.style.maxWidth = '300px';
                     sidebar.style.zIndex = '2000';
                     sidebar.style.background = 'var(--bg-surface-1)';
                     sidebar.style.borderRight = '1px solid var(--border-subtle)';
                     sidebar.style.padding = 'var(--space-4)';
                     sidebar.style.display = 'block';
                } else {
                     sidebar.style = '';
                }
            },
            'end'
        );

        // Only show dock button on mobile
        const checkSize = () => {
            const isMobile = window.innerWidth <= 1024;
            dockBtn.style.display = isMobile ? 'flex' : 'none';
            if (!isMobile) sidebar.classList.remove('active');
        };
        checkSize();
        window.addEventListener('resize', checkSize);
    }

    // 2. Desktop Collapse Button (In Sidebar)
    const header = sidebar.querySelector('#toc-container h2');
    if (header && !document.getElementById('sidebar-collapse-btn')) {
        const collapseBtn = document.createElement('button');
        collapseBtn.id = 'sidebar-collapse-btn';
        collapseBtn.className = 'btn-ghost btn-xs';
        collapseBtn.style.float = 'right';
        collapseBtn.innerHTML = '<i data-feather="chevrons-left"></i>';
        collapseBtn.title = "Collapse Sidebar";
        collapseBtn.onclick = () => toggleDesktopSidebar(false);
        header.insertBefore(collapseBtn, header.firstChild);
    }

    // 3. Desktop Expand Trigger (Floating on Left)
    const expandTrigger = document.createElement('div');
    expandTrigger.id = 'sidebar-expand-trigger';
    expandTrigger.className = 'sidebar-expand-trigger hidden';
    expandTrigger.title = "Expand Sidebar";
    expandTrigger.innerHTML = '<i data-feather="list"></i>';
    expandTrigger.onclick = () => toggleDesktopSidebar(true);
    document.body.appendChild(expandTrigger);

    function toggleDesktopSidebar(show) {
        const main = document.getElementById('main');

        if (show) {
            sidebar.classList.remove('collapsed-desktop');
            expandTrigger.classList.add('hidden');
            // Restore width if needed, but CSS handles standard view
        } else {
            sidebar.classList.add('collapsed-desktop');
            expandTrigger.classList.remove('hidden');
        }

        if (typeof feather !== 'undefined') feather.replace();
    }
}

function initResizableSidebar() {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;

    if (typeof Resizable !== 'undefined') {
        new Resizable(sidebar, {
            handles: ['e'], // East handle only
            minWidth: 200,
            saveKey: 'sidebar',
            onResize: () => {
                // Adjust main content margin if necessary,
                // but Flexbox usually handles this if sidebar width is explicit.
                // However, Resizable sets absolute width.
                // In flex container, 'width' property works.
            }
        });
    }
}

/* =========================================
   5. BACK TO TOP BUTTON
   ========================================= */
function initBackToTop() {
    if (!window.controlDock) return;

    const btn = window.controlDock.addButton(
        'back-to-top-dock',
        'arrow-up',
        'Back to Top',
        () => {
             window.scrollTo({ top: 0, behavior: 'smooth' });
        },
        'start' // At the top of the stack (which is visually bottom/top depending on flex direction)
    );

    // Default hidden
    btn.style.display = 'none';

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            btn.style.display = 'flex';
        } else {
            btn.style.display = 'none';
        }
    });
}
