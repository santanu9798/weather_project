// Add loading state on form submit
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.search-form');
    const btn = document.querySelector('.search-btn');
    const input = document.querySelector('.search-input');

    if (form) {
        form.addEventListener('submit', function () {
            btn.innerHTML = '<span class="btn-text">Searching...</span>';
            btn.style.opacity = '0.8';
            btn.disabled = true;
        });
    }

    // Auto-focus input on load
    if (input) {
        input.focus();
        // Move cursor to end
        const val = input.value;
        input.value = '';
        input.value = val;
    }
});
