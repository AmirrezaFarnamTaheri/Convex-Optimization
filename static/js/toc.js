/**
 * Enhanced Table of Contents
 * Features: Hierarchy, Scrollspy (IntersectionObserver), Collapse/Expand
 */

document.addEventListener('DOMContentLoaded', () => {
    const tocContainer = document.getElementById('toc');
    const content = document.querySelector('.lecture-content');

    if (!tocContainer || !content) return;

    // 1. Build TOC Hierarchy
    const headings = Array.from(content.querySelectorAll('h2, h3'));
    if (headings.length === 0) return;

    const tocList = document.createElement('ul');
    tocList.className = 'toc-list';

    let currentH2Item = null;
    let currentH3List = null;

    headings.forEach((heading, index) => {
        // Ensure ID
        if (!heading.id) {
            // Check parent section ID first
            const parentSection = heading.closest('.section-card');
            if (parentSection && parentSection.id && heading.tagName === 'H2') {
                heading.id = parentSection.id; // Link H2 to Section ID
            } else {
                heading.id = 'heading-' + index;
            }
        }

        const link = document.createElement('a');
        link.href = '#' + heading.id;
        // Clean text: remove icons
        const clone = heading.cloneNode(true);
        const icons = clone.querySelectorAll('i, svg');
        icons.forEach(i => i.remove());
        link.textContent = clone.textContent.trim();
        link.className = 'toc-link';
        link.dataset.target = heading.id;

        const li = document.createElement('li');
        li.appendChild(link);

        if (heading.tagName === 'H2') {
            li.className = 'toc-item-h2';
            tocList.appendChild(li);
            currentH2Item = li;
            currentH3List = null; // Reset
        } else if (heading.tagName === 'H3') {
            li.className = 'toc-item-h3';
            if (!currentH2Item) {
                // Orphan H3, add to root
                tocList.appendChild(li);
            } else {
                if (!currentH3List) {
                    currentH3List = document.createElement('ul');
                    currentH3List.className = 'toc-sublist hidden'; // Default collapsed
                    currentH2Item.appendChild(currentH3List);

                    // Add toggle to parent link
                    const parentLink = currentH2Item.querySelector('.toc-link');
                    if(parentLink && !parentLink.querySelector('.toc-toggle')) {
                        const toggle = document.createElement('span');
                        toggle.className = 'toc-toggle';
                        toggle.innerHTML = '<i data-feather="chevron-right"></i>';
                        toggle.onclick = (e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            currentH3List.classList.toggle('hidden');
                            toggle.innerHTML = currentH3List.classList.contains('hidden')
                                ? '<i data-feather="chevron-right"></i>'
                                : '<i data-feather="chevron-down"></i>';
                            if (typeof feather !== 'undefined') feather.replace();
                        };
                        parentLink.prepend(toggle);
                    }
                }
                currentH3List.appendChild(li);
            }
        }
    });

    tocContainer.innerHTML = '';
    tocContainer.appendChild(tocList);
    if (typeof feather !== 'undefined') feather.replace();

    // 2. Scrollspy (IntersectionObserver)
    const observerOptions = {
        root: null,
        rootMargin: '-10% 0px -80% 0px', // Active zone near top
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id;
                activateLink(id);
            }
        });
    }, observerOptions);

    headings.forEach(h => observer.observe(h));

    function activateLink(id) {
        // Remove active from all
        document.querySelectorAll('.toc-link').forEach(l => l.classList.remove('active'));

        // Add active to current
        const activeLink = document.querySelector(`.toc-link[data-target="${id}"]`);
        if (activeLink) {
            activeLink.classList.add('active');

            // Expand parent if H3
            const parentList = activeLink.closest('.toc-sublist');
            if (parentList) {
                parentList.classList.remove('hidden');
                const toggle = parentList.parentElement.querySelector('.toc-toggle');
                if (toggle) toggle.innerHTML = '<i data-feather="chevron-down"></i>';
                if (typeof feather !== 'undefined') feather.replace();
            }

            // Scroll TOC to keep active in view
            activeLink.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        }
    }
});
