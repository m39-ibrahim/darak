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
        try {
        slides[slideIndex].style.display = "block"; // Show the first slide
            // Clear any existing dots
         dotContainer.innerHTML = "";
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
    catch(err) {
        console.log(err.message);
    }
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
    console.log("Search icon clicked")
    var searchBox = document.getElementById('search-box');
    if (searchBox.classList.contains('visible')) {
        // searchBox.classList.remove('visible');
    } else {
        searchBox.classList.add('visible');
    }
});

document.getElementById('close-search').addEventListener('click', function() {
    document.getElementById('search-box').classList.remove('visible');
});


document.addEventListener('DOMContentLoaded', function() {
    const sectionLinks = document.querySelectorAll('.section-link');
    const categoryContainer = document.getElementById('category-container');

    // Add mouseover event listener to the category container
    categoryContainer.addEventListener('mouseover', function() {
        // Keep the container open when the mouse is inside
        categoryContainer.style.display = 'block';
    });

    // Add mouseout event listener to the category container
    categoryContainer.addEventListener('mouseout', function(event) {
        // const clickedCategory = event.target.textContent.trim();
        // console.log('Category clicked:', clickedCategory);
        // // Send the selected category to the server
        // sendCategoryToServer(clickedCategory);
        // Check if the mouse is leaving the container
        if (!categoryContainer.contains(event.relatedTarget)) {
            // Close the container only if the mouse is not entering a child element
            categoryContainer.style.display = 'none';
        }
    });

    categoryContainer.addEventListener('click', function(event) {
        const clickedCategory = event.target.textContent.trim();
        console.log('Category clicked:', clickedCategory);
        // Send the selected category to the server
        sendCategoryToServer(clickedCategory);
    });

    
    function sendCategoryToServer(category) {
        // Create an XMLHttpRequest object
        const xhr = new XMLHttpRequest();
        // Define the request method, URL, and asynchronous flag
        xhr.open('POST', '/categories', true);
        // Set the request header
        xhr.setRequestHeader('Content-Type', 'application/json');
        // Define the callback function when the request is complete
        xhr.onload = function() {
            if (xhr.status === 200) {
                console.log('Category sent to server successfully.');
            } else {
                console.error('Error sending category to server.');
            }
        };
        // Create a JSON object with the selected category
        const data = JSON.stringify({ category: category });
        // Send the request with the JSON data
        xhr.send(data);
    }

    sectionLinks.forEach(function(sectionLink) {
        sectionLink.addEventListener('mouseover', function() {
            const category = this.getAttribute('data-category');
            const categoryArray = category.split(', '); // Split category string into array
            categoryContainer.innerHTML = ''; // Clear previous content
            // Create and append the title element
            // const titleElement = document.createElement('h2');
            // titleElement.textContent = 'Categories';
            // titleElement.classList.add('category-title');
            // categoryContainer.insertBefore(titleElement, categoryContainer.firstChild);
            categoryContainer.style.paddingTop = '20px';
            categoryContainer.style.paddingBottom = '10px'; 
            categoryArray.forEach(function(cat) {
                const categoryElement = document.createElement('a');
                const d = document.createElement('div');
                d.classList.add('category-link');
                categoryElement.classList.add('category-link');
                categoryElement.href = '/categories/'+cat;
                var linkText = document.createTextNode(cat);
                categoryElement.appendChild(linkText);
                d.appendChild(categoryElement);
                categoryContainer.appendChild(d);
            });
            categoryContainer.style.display = 'block';
        });
    });
});



$(document).ready(function() {
    $('.category-link').click(function(event) {
        event.preventDefault();  // Prevent the default behavior of the link
        var category = $(this).data('category');
        // Perform your desired action with the category data, such as displaying content dynamically
        console.log('Category clicked:', category);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // const sectionLinks = document.querySelectorAll('.section-link');

    // sectionLinks.forEach(function(sectionLink) {
    //     sectionLink.addEventListener('click', function(event) {
    //         event.preventDefault();  // Prevent the default behavior of the link
    //         const sectionName = this.textContent.trim();
    //         // Perform your desired action with the section data
    //         console.log('Section clicked:', sectionName);
    //         // Send the selected section to the server
    //         sendSectionToServer(sectionName);
    //         // window.location.href = '/sections/' + sectionName.replace(/\s+/g, '_').toLowerCase();
    //     });
    // });

    function sendSectionToServer(sectionName) {
        // Create an XMLHttpRequest object
        const xhr = new XMLHttpRequest();
        // Define the request method, URL, and asynchronous flag
        xhr.open('POST', '/sections/' + sectionName, true);
        // Set the request header
        xhr.setRequestHeader('Content-Type', 'application/json');
        // Define the callback function when the request is complete
        xhr.onload = function() {
            if (xhr.status === 200) {
                console.log('Section sent to server successfully.');
            } else {
                console.error('Error sending section to server.');
            }
        };
        // Send the request
        xhr.send();
    }
});
