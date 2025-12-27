/**
 * Widget Utilities
 *
 * Common utilities for all interactive widgets to improve code quality,
 * performance, and prevent memory leaks.
 * Version: 1.0.0
 */

/**
 * Debounce function to prevent expensive operations from running too frequently
 * @param {Function} func - The function to debounce
 * @param {number} wait - The delay in milliseconds
 * @returns {Function} The debounced function
 */
function debounce(func, wait = 250) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Creates a managed ResizeObserver that automatically cleans up
 * @param {HTMLElement} element - Element to observe
 * @param {Function} callback - Callback function
 * @param {Object} options - Options
 * @param {boolean} options.debounce - Whether to debounce the callback
 * @param {number} options.debounceDelay - Debounce delay in ms
 * @returns {ResizeObserver} The observer instance
 */
function createManagedResizeObserver(element, callback, options = {}) {
    const { debounce: shouldDebounce = true, debounceDelay = 250 } = options;

    const finalCallback = shouldDebounce ? debounce(callback, debounceDelay) : callback;

    const observer = new ResizeObserver(entries => {
        try {
            finalCallback(entries);
        } catch (error) {
            console.error('ResizeObserver callback error:', error);
        }
    });

    observer.observe(element);

    // Auto-cleanup when element is removed from DOM
    const cleanupObserver = new MutationObserver(() => {
        if (!document.body.contains(element)) {
            observer.disconnect();
            cleanupObserver.disconnect();
        }
    });

    cleanupObserver.observe(document.body, { childList: true, subtree: true });

    return observer;
}

/**
 * Creates a cleanup manager for widgets
 * @returns {Object} Cleanup manager with methods
 */
function createCleanupManager() {
    const cleanupFunctions = [];

    return {
        /**
         * Add a cleanup function
         * @param {Function} fn - Cleanup function to run on widget destruction
         */
        add(fn) {
            cleanupFunctions.push(fn);
        },

        /**
         * Add a ResizeObserver to be cleaned up
         * @param {ResizeObserver} observer - Observer to disconnect
         */
        addObserver(observer) {
            this.add(() => observer.disconnect());
        },

        /**
         * Add an animation frame to be canceled
         * @param {number} frameId - Animation frame ID
         */
        addAnimationFrame(frameId) {
            this.add(() => cancelAnimationFrame(frameId));
        },

        /**
         * Add an event listener to be removed
         * @param {HTMLElement} element - Element with listener
         * @param {string} event - Event name
         * @param {Function} handler - Event handler
         */
        addListener(element, event, handler) {
            this.add(() => element.removeEventListener(event, handler));
        },

        /**
         * Run all cleanup functions
         */
        cleanup() {
            cleanupFunctions.forEach(fn => {
                try {
                    fn();
                } catch (error) {
                    console.error('Cleanup error:', error);
                }
            });
            cleanupFunctions.length = 0;
        }
    };
}

/**
 * Auto-cleanup wrapper for container removal
 * @param {HTMLElement} container - Widget container
 * @param {Function} cleanupFn - Cleanup function
 */
function autoCleanupOnRemoval(container, cleanupFn) {
    const observer = new MutationObserver(() => {
        if (!document.body.contains(container)) {
            try {
                cleanupFn();
            } catch (error) {
                console.error('Auto-cleanup error:', error);
            }
            observer.disconnect();
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
    return observer;
}

/**
 * Safe wrapper for async operations
 * @param {Function} asyncFn - Async function to wrap
 * @param {string} errorMessage - Error message prefix
 * @returns {Function} Wrapped async function
 */
function safeAsync(asyncFn, errorMessage = 'Async operation failed') {
    return async (...args) => {
        try {
            return await asyncFn(...args);
        } catch (error) {
            console.error(`${errorMessage}:`, error);
            throw error;
        }
    };
}

/**
 * Check if container exists and show error if not
 * @param {string} containerId - Container ID
 * @returns {HTMLElement|null} Container element or null
 */
function getContainer(containerId) {
    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container #${containerId} not found.`);
        return null;
    }
    return container;
}

/**
 * Show loading indicator in container
 * @param {HTMLElement} container - Container element
 * @param {string} message - Loading message
 */
function showLoading(container, message = 'Loading...') {
    container.innerHTML = `<div class="widget-loading-indicator">${message}</div>`;
}

/**
 * Show error message in container
 * @param {HTMLElement} container - Container element
 * @param {string} message - Error message
 */
function showError(container, message = 'An error occurred') {
    container.innerHTML = `<div class="widget-error" style="color: var(--color-danger); padding: 20px; text-align: center;">
        <strong>Error:</strong> ${message}
    </div>`;
}

/**
 * Safe JSON parse with fallback
 * @param {string} jsonString - JSON string
 * @param {*} fallback - Fallback value
 * @returns {*} Parsed object or fallback
 */
function safeJSONParse(jsonString, fallback = null) {
    try {
        return JSON.parse(jsonString);
    } catch (error) {
        console.error('JSON parse error:', error);
        return fallback;
    }
}

/**
 * Clamp value between min and max
 * @param {number} value - Number to clamp
 * @param {number} min - Minimum value
 * @param {number} max - Maximum value
 * @returns {number} Clamped value
 */
function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
}

/**
 * Linear interpolation
 * @param {number} a - Start value
 * @param {number} b - End value
 * @param {number} t - Interpolation parameter [0, 1]
 * @returns {number} Interpolated value
 */
function lerp(a, b, t) {
    return a + (b - a) * clamp(t, 0, 1);
}

/**
 * Get CSS custom property value
 * @param {string} propertyName - CSS custom property name (with or without --)
 * @returns {string} Property value
 */
function getCSSVariable(propertyName) {
    const name = propertyName.startsWith('--') ? propertyName : `--${propertyName}`;
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
}

/**
 * Safe Three.js scene cleanup
 * @param {THREE.Scene} scene - Three.js scene
 * @param {THREE.Renderer} renderer - Three.js renderer
 */
function cleanupThreeJS(scene, renderer) {
    if (!scene || !renderer) return;

    try {
        // Dispose of geometries and materials
        scene.traverse((object) => {
            if (object.geometry) {
                object.geometry.dispose();
            }
            if (object.material) {
                if (Array.isArray(object.material)) {
                    object.material.forEach(material => material.dispose());
                } else {
                    object.material.dispose();
                }
            }
        });

        // Dispose renderer
        renderer.dispose();
        renderer.forceContextLoss();
    } catch (error) {
        console.error('Three.js cleanup error:', error);
    }
}

/**
 * Format number with specified precision
 * @param {number} value - Number to format
 * @param {number} precision - Decimal places
 * @returns {string} Formatted number
 */
function formatNumber(value, precision = 2) {
    if (!isFinite(value)) return 'N/A';
    return value.toFixed(precision);
}

/**
 * Check if value is numeric
 * @param {*} value - Value to check
 * @returns {boolean} True if numeric
 */
function isNumeric(value) {
    return !isNaN(parseFloat(value)) && isFinite(value);
}

/**
 * Enables dragging for an element using a handle
 * @param {HTMLElement} element - The element to make draggable
 * @param {HTMLElement} handle - The handle element (optional, defaults to element)
 * @param {Object} options - Options (saveKey for persistence)
 */
function enableDrag(element, handle, options = {}) {
    handle = handle || element;
    let isDragging = false;
    let startX, startY, initialLeft, initialTop;
    const { saveKey } = options;

    // Load saved position
    if (saveKey) {
        const saved = JSON.parse(localStorage.getItem(saveKey + '-pos'));
        if (saved) {
            element.style.left = saved.left;
            element.style.top = saved.top;
            // Clear specific positioning if needed (like bottom/right) to allow left/top to work
            if (saved.left) element.style.right = 'auto';
            if (saved.top) element.style.bottom = 'auto';
        }
    }

    handle.addEventListener('mousedown', (e) => {
        // Prevent dragging if clicking on interactive elements inside the handle
        if (e.target.closest('button') || e.target.closest('input') || e.target.closest('.no-drag')) return;

        isDragging = true;
        handle.style.cursor = 'grabbing';

        startX = e.clientX;
        startY = e.clientY;

        const rect = element.getBoundingClientRect();

        // We must switch to left/top positioning for dragging to work consistently
        // This calculates the current absolute position relative to the viewport/document
        initialLeft = rect.left;
        initialTop = rect.top;

        // Force convert to left/top positioning in pixels
        element.style.left = `${initialLeft}px`;
        element.style.top = `${initialTop}px`;
        element.style.right = 'auto';
        element.style.bottom = 'auto';
        element.style.transform = 'none'; // Clear center transforms if any

        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
    });

    const onMouseMove = (e) => {
        if (!isDragging) return;
        const dx = e.clientX - startX;
        const dy = e.clientY - startY;

        element.style.left = `${initialLeft + dx}px`;
        element.style.top = `${initialTop + dy}px`;
    };

    const onMouseUp = () => {
        if (!isDragging) return;
        isDragging = false;
        handle.style.cursor = 'grab'; // Reset to grab

        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);

        if (saveKey) {
            localStorage.setItem(saveKey + '-pos', JSON.stringify({
                left: element.style.left,
                top: element.style.top
            }));
        }
    };

    // Set initial cursor
    handle.style.cursor = 'grab';
}

// Expose utilities to global scope for non-module scripts
if (typeof window !== 'undefined') {
    window.enableDrag = enableDrag;
    window.widgetUtils = {
        debounce,
        createManagedResizeObserver,
        createCleanupManager,
        autoCleanupOnRemoval,
        safeAsync,
        getContainer,
        showLoading,
        showError,
        safeJSONParse,
        clamp,
        lerp,
        getCSSVariable,
        cleanupThreeJS,
        formatNumber,
        isNumeric,
        enableDrag
    };
}
