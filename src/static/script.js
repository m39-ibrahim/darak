function showLoginForm() {
    document.getElementById('login-form').style.display = 'block';
    document.getElementById('signup-form').style.display = 'none';
}

function showSignUpForm() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('signup-form').style.display = 'block';
}


document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll(".hero-img");
    const dotContainer = document.querySelector(".dot-container");
    let slideIndex = 0; // Start with the first image as active

    // Function to update the slide's visibility and corresponding dot
    function updateSlides() {
        slides.forEach((slide, index) => {
            slide.style.display = "none"; // Hide all slides
            // Remove 'active' class from all dots
            dotContainer.children[index].classList.remove("active");
        });
        slides[slideIndex].style.display = "block"; // Show the active slide
        dotContainer.children[slideIndex].classList.add("active"); // Highlight the active dot
    }

    // Initialize slides and dots
    function initSlider() {
        slides[slideIndex].style.display = "block"; // Show the first slide
        // Create dots
        slides.forEach((_, index) => {
            const dot = document.createElement("span");
            dot.classList.add("dot");
            dot.addEventListener("click", () => {
                slideIndex = index;
                updateSlides();
            });
            dotContainer.appendChild(dot);
        });
        updateSlides(); // Update slides for the first time
    }

    // Move slide forward or backward
    window.moveSlide = function (step) {
        slideIndex += step;
        if (slideIndex >= slides.length) {
            slideIndex = 0; // Go back to the first slide
        } else if (slideIndex < 0) {
            slideIndex = slides.length - 1; // Go to the last slide
        }
        updateSlides();
    };

    initSlider();
});



document.getElementById('search-icon').addEventListener('click', function() {
    var searchBox = document.getElementById('search-box');
    if (searchBox.classList.contains('visible')) {
        searchBox.classList.remove('visible');
    } else {
        searchBox.classList.add('visible');
    }
});

document.getElementById('close-search').addEventListener('click', function() {
    document.getElementById('search-box').classList.remove('visible');
});

