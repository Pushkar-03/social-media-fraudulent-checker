document.getElementById('input-form').addEventListener('submit', function (event) {
    const inputField = document.getElementById('social_id');
    if (!inputField.value) {
        alert('Please enter a valid Social Media ID!');
        event.preventDefault();
    }
});

document.getElementById('theme-toggle').addEventListener('click', function () {
    const body = document.body;
    body.classList.toggle('dark-mode');

    // Save the preference
    const isDarkMode = body.classList.contains('dark-mode');
    localStorage.setItem('dark-mode', isDarkMode);
});

// Load saved theme preference
window.onload = function () {
    const isDarkMode = localStorage.getItem('dark-mode') === 'true';
    if (isDarkMode) {
        document.body.classList.add('dark-mode');
    }
};

document.getElementById('social_id').addEventListener('input', function (event) {
    const value = event.target.value;
    if (isNaN(value) || value <= 0) {
        event.target.setCustomValidity('Please enter a valid positive number!');
    } else {
        event.target.setCustomValidity('');
    }
});

const suggestions = [101, 102, 103, 104];
const inputField = document.getElementById('social_id');

inputField.addEventListener('input', function () {
    const value = inputField.value;
    const suggestionsList = document.getElementById('suggestions');
    suggestionsList.innerHTML = '';

    if (value) {
        const matches = suggestions.filter(id => id.toString().startsWith(value));
        matches.forEach(match => {
            const option = document.createElement('option');
            option.value = match;
            suggestionsList.appendChild(option);
        });
    }
});


// Theme Toggle Logic
document.getElementById('theme-toggle').addEventListener('click', () => {
    const body = document.body;
    body.classList.toggle('dark');
    const isDarkMode = body.classList.contains('dark');
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
});

// Apply Saved Theme on Page Load
window.onload = () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark');
    }
};
