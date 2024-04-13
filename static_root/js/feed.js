document.addEventListener("DOMContentLoaded", function() {
    const dropdown = document.querySelector(".dropdown");

    function toggleDropdown() {
        const dropdownContent = dropdown.querySelector(".dropdown-content");
        dropdownContent.classList.toggle("show");
    }

    document.addEventListener("click", function(event) {
        if (!event.target.matches('.dropbtn')) {
            const dropdownContents = document.querySelectorAll('.dropdown-content');
            dropdownContents.forEach(function(dropdownContent) {
                if (dropdownContent.classList.contains('show')) {
                    dropdownContent.classList.remove('show');
                }
            });
        }
    });

    dropdown.addEventListener("click", function(event) {
        event.stopPropagation();
        toggleDropdown();
    });

    // Example of adding click functionality to different links
    const links = document.querySelectorAll('.nav-link');

    links.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            // Replace with the appropriate logic for each link click
            console.log('Link clicked:', event.target.textContent);
            // You can add code here to load content based on the clicked link
        });
    });
});
