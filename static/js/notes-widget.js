/**
 * Convex Optimization Study Tools
 * Decoupled widgets for Notes, Bookmarks, and Highlighting.
 */

/* =========================================
   1. NOTES WIDGET
   ========================================= */
class NotesWidget {
    constructor() {
        this.lectureId = window.location.pathname;
        this.notes = [];
        this.panel = null;
        this.isPreviewMode = false;

        this.loadDependencies().then(() => {
            this.loadData();
            this.createUI();
        });
    }

    async loadDependencies() {
        if (typeof marked === 'undefined') {
            return new Promise((resolve) => {
                const script = document.createElement('script');
                // Resolve relative to this script file
                const myScript = document.querySelector('script[src*="notes-widget.js"]');
                const baseUrl = myScript ? myScript.src.substring(0, myScript.src.lastIndexOf('/')) : 'static/js';
                script.src = baseUrl + '/../lib/marked/marked.min.js';
                script.onload = resolve;
                script.onerror = () => { console.warn('Marked.js failed to load'); resolve(); };
                document.head.appendChild(script);
            });
        }
    }

    loadData() {
        const data = localStorage.getItem(`kw-notes-${this.lectureId}`);
        this.notes = data ? JSON.parse(data) : [];
    }

    saveData() {
        localStorage.setItem(`kw-notes-${this.lectureId}`, JSON.stringify(this.notes));
    }

    createUI() {
        if (!window.controlDock) return;

        // Dock Button
        window.controlDock.addButton(
            'notes-widget-btn',
            'edit-3',
            'Lecture Notes',
            () => this.togglePanel()
        );

        // Panel
        this.panel = document.createElement('div');
        this.panel.className = 'tool-panel hidden';
        this.panel.id = 'notes-panel';
        this.panel.setAttribute('role', 'dialog');
        this.panel.setAttribute('aria-label', 'Lecture Notes');

        this.panel.innerHTML = `
            <div class="tool-header">
                <span class="tool-title"><i data-feather="edit-3"></i> Notes</span>
                <button class="tool-close" aria-label="Close Notes"><i data-feather="x"></i></button>
            </div>
            <div class="tool-toolbar">
                <button class="btn btn-sm btn-ghost" id="note-add" title="Add Note"><i data-feather="plus"></i> New</button>
                <button class="btn btn-sm btn-ghost" id="note-preview" title="Toggle Preview"><i data-feather="eye"></i> Preview</button>
                <div class="dropdown" style="position:relative; display:inline-block;">
                    <button class="btn btn-sm btn-ghost" id="note-export-btn" title="Export"><i data-feather="download"></i></button>
                    <div class="dropdown-content hidden" id="note-export-menu" style="position:absolute; top:100%; right:0; background:var(--bg-surface-2); border:1px solid var(--border-subtle); border-radius:4px; min-width:120px; z-index:10;">
                        <button class="btn-ghost" style="width:100%; text-align:left; padding:8px;" id="export-md">Markdown (.md)</button>
                        <button class="btn-ghost" style="width:100%; text-align:left; padding:8px;" id="export-json">JSON (.json)</button>
                    </div>
                </div>
            </div>
            <div class="tool-body" id="notes-list"></div>
        `;

        document.body.appendChild(this.panel);
        this.bindEvents();
        this.renderNotes();
        this.injectStyles();

        // Enable Drag & Resize
        if (window.enableDrag) {
            window.enableDrag(this.panel, this.panel.querySelector('.tool-header'), { saveKey: 'notes-panel' });
        }
        if (typeof Resizable !== 'undefined') {
            new Resizable(this.panel, { saveKey: 'notes-panel', handles: ['se', 'e', 's', 'w'] });
        }
    }

    bindEvents() {
        this.panel.querySelector('.tool-close').onclick = () => this.togglePanel();
        this.panel.querySelector('#note-add').onclick = () => this.addNote();
        this.panel.querySelector('#note-preview').onclick = () => this.togglePreview();

        const exportBtn = this.panel.querySelector('#note-export-btn');
        const exportMenu = this.panel.querySelector('#note-export-menu');
        exportBtn.onclick = () => exportMenu.classList.toggle('hidden');

        this.panel.querySelector('#export-md').onclick = () => { this.exportNotes('md'); exportMenu.classList.add('hidden'); };
        this.panel.querySelector('#export-json').onclick = () => { this.exportNotes('json'); exportMenu.classList.add('hidden'); };
    }

    injectStyles() {
        if (document.getElementById('tool-panel-styles')) return;
        const style = document.createElement('style');
        style.id = 'tool-panel-styles';
        style.textContent = `
            .tool-panel {
                position: fixed; top: 80px; right: 80px; width: 350px; height: 500px; max-height: 90vh;
                background: var(--bg-surface-1); border: 1px solid var(--border-subtle);
                border-radius: var(--radius-lg); box-shadow: var(--shadow-xl);
                z-index: 3000; display: flex; flex-direction: column;
            }
            .tool-panel.hidden { display: none; }
            .tool-header {
                padding: var(--space-4); border-bottom: 1px solid var(--border-subtle);
                display: flex; justify-content: space-between; align-items: center;
                background: var(--bg-surface-2); border-radius: var(--radius-lg) var(--radius-lg) 0 0;
            }
            .tool-title { font-weight: 600; display: flex; gap: 8px; align-items: center; }
            .tool-close { background: none; border: none; color: var(--text-secondary); cursor: pointer; }
            .tool-toolbar { padding: var(--space-3); display: flex; gap: 8px; border-bottom: 1px solid var(--border-subtle); align-items: center; }
            .tool-body { overflow-y: auto; flex: 1; padding: var(--space-3); }
            
            .note-item {
                background: var(--bg-surface-2); padding: var(--space-3); border-radius: var(--radius-md);
                margin-bottom: var(--space-3); border: 1px solid var(--border-subtle); display: flex; flex-direction: column;
            }
            .note-item textarea {
                width: 100%; background: transparent; border: none; color: var(--text-primary);
                font-family: var(--font-mono); font-size: 0.9em; resize: vertical; min-height: 80px; outline: none;
                margin-top: 8px;
            }
            .note-meta { display: flex; justify-content: space-between; font-size: 0.75em; color: var(--text-tertiary); margin-bottom: 4px; align-items: center; }
            
            /* Markdown Toolbar */
            .md-toolbar { display: flex; gap: 4px; margin-bottom: 4px; background: var(--bg-surface-3); padding: 4px; border-radius: 4px; }
            .md-btn { background: none; border: none; cursor: pointer; color: var(--text-secondary); padding: 2px 4px; border-radius: 3px; }
            .md-btn:hover { background: var(--bg-surface-1); color: var(--text-primary); }
            
            .dropdown-content button:hover { background: var(--bg-surface-3); }
        `;
        document.head.appendChild(style);
    }

    togglePanel() {
        this.panel.classList.toggle('hidden');
        const btn = document.getElementById('notes-widget-btn');
        if (btn) btn.classList.toggle('active', !this.panel.classList.contains('hidden'));
    }

    addNote() {
        this.notes.unshift({ id: Date.now(), text: '', timestamp: new Date().toISOString() });
        this.renderNotes();
        this.saveData();
    }

    updateNote(id, text) {
        const n = this.notes.find(n => n.id === id);
        if (n) { n.text = text; this.saveData(); }
    }

    deleteNote(id) {
        if (confirm('Delete note?')) {
            this.notes = this.notes.filter(n => n.id !== id);
            this.renderNotes();
            this.saveData();
        }
    }

    togglePreview() {
        this.isPreviewMode = !this.isPreviewMode;
        this.renderNotes();
    }

    exportNotes(format = 'md') {
        if (this.notes.length === 0) { alert('No notes to export.'); return; }
        let content = '';
        let filename = `notes.${format}`;
        let type = 'text/plain';

        if (format === 'json') {
            content = JSON.stringify(this.notes, null, 2);
            type = 'application/json';
        } else {
            content = `# Notes for ${this.lectureId}\n\n`;
            this.notes.forEach(n => {
                content += `## ${new Date(n.timestamp).toLocaleDateString()}\n\n${n.text}\n\n---\n\n`;
            });
            type = 'text/markdown';
        }

        const blob = new Blob([content], { type: type });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }

    insertMarkdown(id, symbol, closeSymbol = '') {
        const textarea = this.panel.querySelector(`textarea[data-id="${id}"]`);
        if (!textarea) return;

        const start = textarea.selectionStart;
        const end = textarea.selectionEnd;
        const text = textarea.value;
        const selection = text.substring(start, end);

        const newText = text.substring(0, start) + symbol + selection + (closeSymbol || symbol) + text.substring(end);
        textarea.value = newText;
        this.updateNote(id, newText);

        textarea.focus();
        const newCursor = start + symbol.length;
        textarea.setSelectionRange(newCursor, newCursor + selection.length);
    }

    renderNotes() {
        const list = this.panel.querySelector('#notes-list');
        list.innerHTML = '';
        if (this.notes.length === 0) {
            list.innerHTML = '<div style="text-align:center;color:var(--text-tertiary);padding:20px;">No notes yet.</div>';
            return;
        }
        this.notes.forEach(note => {
            const el = document.createElement('div');
            el.className = 'note-item';
            const dateStr = new Date(note.timestamp).toLocaleDateString();
            
            if (this.isPreviewMode && typeof marked !== 'undefined') {
                el.innerHTML = `
                    <div class="note-meta">
                        <span>${dateStr}</span>
                        <button class="btn-ghost btn-xs" aria-label="Delete Note"><i data-feather="trash-2" style="width:14px;"></i></button>
                    </div>
                    <div class="markdown-body" style="font-size:0.9em;">${marked.parse(note.text || '')}</div>
                `;
            } else {
                el.innerHTML = `
                    <div class="note-meta">
                        <span>${dateStr}</span>
                        <div style="display:flex; gap:4px;">
                            <button class="btn-ghost btn-xs" aria-label="Delete Note"><i data-feather="trash-2" style="width:14px;"></i></button>
                        </div>
                    </div>
                    <div class="md-toolbar">
                        <button class="md-btn" title="Bold" onclick="window.notesWidget.insertMarkdown(${note.id}, '**')"><b>B</b></button>
                        <button class="md-btn" title="Italic" onclick="window.notesWidget.insertMarkdown(${note.id}, '_')"><i>I</i></button>
                        <button class="md-btn" title="Code" onclick="window.notesWidget.insertMarkdown(${note.id}, '\`')">{}</button>
                        <button class="md-btn" title="List" onclick="window.notesWidget.insertMarkdown(${note.id}, '- ', '')">•</button>
                    </div>
                    <textarea data-id="${note.id}" placeholder="Enter note...">${note.text}</textarea>
                `;

                const ta = el.querySelector('textarea');
                ta.oninput = (e) => this.updateNote(note.id, e.target.value);
            }

            el.querySelector('.note-meta button').onclick = () => this.deleteNote(note.id);
            list.appendChild(el);
        });
        if (typeof feather !== 'undefined') feather.replace();
    }
}

/* =========================================
   2. BOOKMARKS WIDGET
   ========================================= */
class BookmarkWidget {
    constructor() {
        this.lectureId = window.location.pathname;
        this.bookmarks = [];
        this.panel = null;

        this.loadData();
        this.createUI();
    }

    loadData() {
        const data = localStorage.getItem(`kw-bookmarks-${this.lectureId}`);
        this.bookmarks = data ? JSON.parse(data) : [];
    }

    saveData() {
        localStorage.setItem(`kw-bookmarks-${this.lectureId}`, JSON.stringify(this.bookmarks));
    }

    createUI() {
        if (!window.controlDock) return;

        window.controlDock.addButton(
            'bookmark-widget-btn',
            'bookmark',
            'Bookmarks',
            () => this.togglePanel()
        );

        this.panel = document.createElement('div');
        this.panel.className = 'tool-panel hidden';
        this.panel.id = 'bookmarks-panel';
        this.panel.setAttribute('role', 'dialog');
        this.panel.setAttribute('aria-label', 'Bookmarks');

        this.panel.innerHTML = `
            <div class="tool-header">
                <span class="tool-title"><i data-feather="bookmark"></i> Bookmarks</span>
                <button class="tool-close" aria-label="Close Bookmarks"><i data-feather="x"></i></button>
            </div>
            <div class="tool-toolbar">
                <button class="btn btn-sm btn-ghost" id="bk-add" style="width:100%"><i data-feather="plus"></i> Bookmark Current View</button>
            </div>
            <div class="tool-body" id="bk-list"></div>
        `;

        document.body.appendChild(this.panel);
        this.bindEvents();
        this.renderBookmarks();

        // Enable Drag & Resize
        if (window.enableDrag) {
            window.enableDrag(this.panel, this.panel.querySelector('.tool-header'), { saveKey: 'bookmarks-panel' });
        }
        if (typeof Resizable !== 'undefined') {
            new Resizable(this.panel, { saveKey: 'bookmarks-panel', handles: ['se', 's', 'e'] });
        }
    }

    bindEvents() {
        this.panel.querySelector('.tool-close').onclick = () => this.togglePanel();
        this.panel.querySelector('#bk-add').onclick = () => this.addBookmark();
    }

    togglePanel() {
        this.panel.classList.toggle('hidden');
        const btn = document.getElementById('bookmark-widget-btn');
        if (btn) btn.classList.toggle('active', !this.panel.classList.contains('hidden'));
    }

    addBookmark() {
        let header = null;
        const headers = Array.from(document.querySelectorAll('h1, h2, h3'));
        for (let h of headers) {
            const rect = h.getBoundingClientRect();
            if (rect.top >= 0 && rect.top < window.innerHeight / 2) {
                header = h;
                break;
            }
        }

        const scrollY = window.scrollY;
        const title = header ? header.innerText : `Position ${Math.round(scrollY)}`;
        const targetId = header ? (header.id || (header.id = `bk-${Date.now()}`)) : null;

        this.bookmarks.push({
            id: Date.now(),
            title: title,
            targetId: targetId,
            scrollY: scrollY
        });
        this.saveData();
        this.renderBookmarks();
    }

    deleteBookmark(id) {
        this.bookmarks = this.bookmarks.filter(b => b.id !== id);
        this.saveData();
        this.renderBookmarks();
    }

    renderBookmarks() {
        const list = this.panel.querySelector('#bk-list');
        list.innerHTML = '';
        if (this.bookmarks.length === 0) {
            list.innerHTML = '<div style="text-align:center;color:var(--text-tertiary);padding:20px;">No bookmarks.</div>';
            return;
        }

        if (!document.getElementById('bk-styles')) {
            const s = document.createElement('style');
            s.id = 'bk-styles';
            s.textContent = `
                .bk-item {
                    padding: 10px; border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
                    margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;
                    cursor: pointer; transition: background 0.2s;
                }
                .bk-item:hover { background: var(--bg-surface-2); }
            `;
            document.head.appendChild(s);
        }

        this.bookmarks.forEach(b => {
            const el = document.createElement('div');
            el.className = 'bk-item';
            el.innerHTML = `<span>${b.title}</span><button class="btn-ghost btn-xs" aria-label="Delete"><i data-feather="trash-2" style="width:14px;"></i></button>`;

            el.onclick = () => {
                if (b.targetId) {
                    const t = document.getElementById(b.targetId);
                    if (t) t.scrollIntoView({ behavior: 'smooth' });
                } else {
                    window.scrollTo({ top: b.scrollY, behavior: 'smooth' });
                }
            };

            el.querySelector('button').onclick = (e) => {
                e.stopPropagation();
                this.deleteBookmark(b.id);
            };

            list.appendChild(el);
        });
        if (typeof feather !== 'undefined') feather.replace();
    }
}

/* =========================================
   3. HIGHLIGHTER WIDGET
   ========================================= */
class HighlighterWidget {
    constructor() {
        this.lectureId = window.location.pathname;
        this.highlights = [];
        this.isActive = false;
        this.panel = null;

        this.loadData();
        this.restoreHighlights();
        this.createUI();

        document.addEventListener('mouseup', (e) => this.handleSelection(e));
        document.addEventListener('keydown', (e) => this.handleShortcuts(e));
    }

    loadData() {
        const data = localStorage.getItem(`kw-highlights-${this.lectureId}`);
        this.highlights = data ? JSON.parse(data) : [];
    }

    saveData() {
        localStorage.setItem(`kw-highlights-${this.lectureId}`, JSON.stringify(this.highlights));
    }

    createUI() {
        if (!window.controlDock) return;

        // Toggle Button
        this.btn = window.controlDock.addButton(
            'highlight-widget-btn',
            'pen-tool',
            'Highlighter (Alt+1-4)',
            () => this.toggleActive()
        );

        // Panel Button (Right Click or Long Press? For now let's add a separate button or make it open on double click?
        // No, let's just make the "pen-tool" button toggle the panel if already active, or have a separate button?
        // Actually, let's add a separate button to the dock for "Highlights List" or put it in the panel that opens)

        // Better: Make the highlighter button toggle the MODE. Add a small "List" button or context menu?
        // Let's create a Panel that is toggled by a secondary action or separate button?
        // To save space, let's just add a "Highlights" list button to the dock.

        window.controlDock.addButton(
            'highlight-list-btn',
            'list',
            'View Highlights',
            () => this.togglePanel()
        );

        // Panel
        this.panel = document.createElement('div');
        this.panel.className = 'tool-panel hidden';
        this.panel.id = 'highlights-panel';
        this.panel.setAttribute('role', 'dialog');
        this.panel.setAttribute('aria-label', 'Highlights List');

        this.panel.innerHTML = `
            <div class="tool-header">
                <span class="tool-title"><i data-feather="list"></i> Highlights</span>
                <button class="tool-close" aria-label="Close Highlights"><i data-feather="x"></i></button>
            </div>
            <div class="tool-toolbar">
                 <small style="color:var(--text-tertiary);">Select text to highlight</small>
            </div>
            <div class="tool-body" id="hl-list"></div>
        `;

        document.body.appendChild(this.panel);
        this.bindEvents();
        this.renderHighlights();
        this.injectStyles();

        if (window.enableDrag) {
            window.enableDrag(this.panel, this.panel.querySelector('.tool-header'), { saveKey: 'highlights-panel' });
        }
        if (typeof Resizable !== 'undefined') {
            new Resizable(this.panel, { saveKey: 'highlights-panel', handles: ['se', 's', 'e'] });
        }
    }

    bindEvents() {
        this.panel.querySelector('.tool-close').onclick = () => this.togglePanel();
    }

    togglePanel() {
        this.panel.classList.toggle('hidden');
        this.renderHighlights(); // Refresh
    }

    injectStyles() {
        if (document.getElementById('hl-styles')) return;
        const s = document.createElement('style');
        s.id = 'hl-styles';
        s.textContent = `
            .kw-highlight { border-radius: 2px; cursor: pointer; transition: background 0.2s; }
            .kw-highlight:hover { filter: brightness(0.95); }
            .kw-highlight-yellow { background-color: rgba(253, 224, 71, 0.4); }
            .kw-highlight-green { background-color: rgba(134, 239, 172, 0.4); }
            .kw-highlight-blue { background-color: rgba(147, 197, 253, 0.4); }
            .kw-highlight-red { background-color: rgba(252, 165, 165, 0.4); }

            .hl-menu {
                position: absolute; background: var(--bg-surface-1); padding: 8px; border-radius: 20px;
                display: flex; gap: 8px; box-shadow: var(--shadow-lg); border: 1px solid var(--border-subtle);
                z-index: 4000; animation: fadeIn 0.1s ease;
            }
            .hl-color-btn {
                width: 24px; height: 24px; border-radius: 50%; border: 1px solid rgba(0,0,0,0.1);
                cursor: pointer; transition: transform 0.1s;
            }
            .hl-color-btn:hover { transform: scale(1.2); }

            .hl-item {
                padding: 10px; border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
                margin-bottom: 8px; font-size: 0.9em;
            }
            .hl-item-header { display: flex; justify-content: space-between; margin-bottom: 4px; }
            .hl-color-dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }

            @keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
        `;
        document.head.appendChild(s);
    }

    toggleActive() {
        this.isActive = !this.isActive;
        this.btn.classList.toggle('active', this.isActive);
        document.body.style.cursor = this.isActive ? 'text' : '';
    }

    handleSelection(e) {
        if (!this.isActive) return;

        if (e.target.classList.contains('kw-highlight')) {
            if (confirm('Remove highlight?')) {
                this.removeHighlight(e.target);
            }
            window.getSelection().removeAllRanges();
            return;
        }

        const selection = window.getSelection();
        if (selection.isCollapsed || !selection.rangeCount) return;

        const text = selection.toString().trim();
        if (text.length < 2) return;

        if (e.target.closest('.tool-panel')) return;

        this.showMenu(selection);
    }

    handleShortcuts(e) {
        if (e.altKey && ['1', '2', '3', '4'].includes(e.key)) {
            const selection = window.getSelection();
            if (selection.isCollapsed) return;

            e.preventDefault();
            const colors = ['yellow', 'green', 'blue', 'red'];
            const color = colors[parseInt(e.key) - 1];
            this.createHighlight(selection, color);
            window.getSelection().removeAllRanges();
        }
    }

    showMenu(selection) {
        const existing = document.getElementById('hl-menu');
        if (existing) existing.remove();

        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();

        const menu = document.createElement('div');
        menu.id = 'hl-menu';
        menu.className = 'hl-menu';
        menu.style.top = `${window.scrollY + rect.bottom + 10}px`;
        menu.style.left = `${window.scrollX + rect.left + (rect.width/2) - 60}px`;

        const colors = [
            { name: 'yellow', hex: '#fde047' },
            { name: 'green', hex: '#86efac' },
            { name: 'blue', hex: '#93c5fd' },
            { name: 'red', hex: '#fca5a5' }
        ];

        colors.forEach(c => {
            const b = document.createElement('button');
            b.className = 'hl-color-btn';
            b.style.backgroundColor = c.hex;
            b.setAttribute('aria-label', `Highlight ${c.name}`);
            b.onclick = (e) => {
                e.stopPropagation();
                this.createHighlight(selection, c.name);
                menu.remove();
                window.getSelection().removeAllRanges();
            };
            menu.appendChild(b);
        });

        document.body.appendChild(menu);

        const close = (e) => {
            if (!menu.contains(e.target)) {
                menu.remove();
                document.removeEventListener('mousedown', close);
            }
        };
        setTimeout(() => document.addEventListener('mousedown', close), 0);
    }

    createHighlight(selection, color) {
        const range = selection.getRangeAt(0);
        const content = range.toString();

        const span = document.createElement('span');
        span.className = `kw-highlight kw-highlight-${color}`;
        span.textContent = content;
        span.dataset.id = Date.now();

        try {
            range.surroundContents(span);
        } catch(e) {
            console.warn('Cannot highlight across block boundaries (simple mode).');
            return;
        }

        let container = span.parentElement;
        const path = this.getPath(container);

        this.highlights.push({
            id: span.dataset.id,
            text: content,
            color: color,
            path: path,
            timestamp: new Date().toISOString()
        });
        this.saveData();
        this.renderHighlights();
    }

    getPath(el) {
        if (el.id) return '#' + el.id;
        return 'body';
    }

    restoreHighlights() {
        this.highlights.forEach(h => {
            const parent = document.querySelector(h.path);
            if (!parent) return;

            const walker = document.createTreeWalker(parent, NodeFilter.SHOW_TEXT, null, false);
            let node;
            while(node = walker.nextNode()) {
                if (node.parentElement.classList.contains('kw-highlight')) continue;

                const idx = node.textContent.indexOf(h.text);
                if (idx !== -1) {
                    const range = document.createRange();
                    range.setStart(node, idx);
                    range.setEnd(node, idx + h.text.length);

                    const span = document.createElement('span');
                    span.className = `kw-highlight kw-highlight-${h.color}`;
                    span.dataset.id = h.id;

                    try {
                        range.surroundContents(span);
                    } catch (e) {}
                    break;
                }
            }
        });
    }

    removeHighlight(el) {
        const id = el.dataset.id;
        const parent = el.parentNode;
        while(el.firstChild) parent.insertBefore(el.firstChild, el);
        parent.removeChild(el);
        parent.normalize();

        this.highlights = this.highlights.filter(h => h.id != id);
        this.saveData();
        this.renderHighlights();
    }

    renderHighlights() {
        if (!this.panel) return;
        const list = this.panel.querySelector('#hl-list');
        list.innerHTML = '';
        if (this.highlights.length === 0) {
            list.innerHTML = '<div style="text-align:center;color:var(--text-tertiary);padding:20px;">No highlights.</div>';
            return;
        }

        this.highlights.forEach(h => {
            const el = document.createElement('div');
            el.className = 'hl-item';
            const colorMap = { yellow: '#fde047', green: '#86efac', blue: '#93c5fd', red: '#fca5a5' };

            el.innerHTML = `
                <div class="hl-item-header">
                    <span class="hl-color-dot" style="background:${colorMap[h.color]}"></span>
                    <button class="btn-ghost btn-xs" aria-label="Delete"><i data-feather="trash-2" style="width:14px;"></i></button>
                </div>
                <div>${h.text}</div>
            `;

            el.querySelector('button').onclick = () => {
                const span = document.querySelector(`.kw-highlight[data-id="${h.id}"]`);
                if (span) this.removeHighlight(span);
                else {
                    // Just remove data if span not found
                    this.highlights = this.highlights.filter(x => x.id !== h.id);
                    this.saveData();
                    this.renderHighlights();
                }
            };

            el.onclick = (e) => {
                if (e.target.closest('button')) return;
                const span = document.querySelector(`.kw-highlight[data-id="${h.id}"]`);
                if (span) span.scrollIntoView({ behavior: 'smooth', block: 'center' });
            };

            list.appendChild(el);
        });
        if (typeof feather !== 'undefined') feather.replace();
    }
}

/* =========================================
   BOOTSTRAP
   ========================================= */
document.addEventListener('DOMContentLoaded', () => {
    // Initialize independently
    window.notesWidget = new NotesWidget();
    window.bookmarkWidget = new BookmarkWidget();
    window.highlighterWidget = new HighlighterWidget();
});
