document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.star');
    const ratingInput = document.getElementById('rating');

    stars.forEach(star => {
        star.addEventListener('mouseover', function() {
            highlightStars(star.dataset.value);
        });

        star.addEventListener('mouseout', function() {
            highlightStars(ratingInput.value);
        });

        star.addEventListener('click', function() {
            ratingInput.value = star.dataset.value;
            highlightStars(star.dataset.value);
        });
    });

    function highlightStars(rating) {
        stars.forEach(star => {
            if (star.dataset.value <= rating) {
                star.classList.add('selected');
            } else {
                star.classList.remove('selected');
            }
        });
    }
});