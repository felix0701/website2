document.addEventListener("DOMContentLoaded", function () {
    const dynamicText = document.getElementById('dynamic-text');
    const additionalText = document.getElementById('additional-text');
    const texts = [
        'Find a New Project',
        'Find a New Research Fellow',
        'Find a Mentor',
        'Find a Research',
    ];

    let currentIndex = 0;

    function updateDynamicText() {
        dynamicText.textContent = 'Help Me';
        additionalText.textContent = texts[currentIndex];
        currentIndex = (currentIndex + 1) % texts.length;
    }

    function animateText() {
        const initialAnimationDuration = 1000; // 1 second
        const subsequentAnimationDuration = 1000; // 2 seconds

        // Initial animation to show "Help Me"
        setTimeout(function () {
            dynamicText.textContent = 'Help Me';
            currentIndex = 0;

            // Subsequent animations with a time gap
            setInterval(updateDynamicText, subsequentAnimationDuration);
        }, initialAnimationDuration);
    }

    animateText();
});
