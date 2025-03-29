// -------------------------Second-Work-Description-------------------------
document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll(".discover-section-code-item-default, .discover-section-code-item-active");
    const previewImages = document.querySelectorAll(".discover-section-codes-preview-image img");
    const heading = document.getElementById("dynamic-heading");
    const paragraph = document.getElementById("dynamic-paragraph");

    items.forEach((item, index) => {
        item.addEventListener("click", function () {
            // Replace class for divs
            document.querySelector(".discover-section-code-item-active")?.classList.replace("discover-section-code-item-active", "discover-section-code-item-default");
            this.classList.replace("discover-section-code-item-default", "discover-section-code-item-active");

            // Replace class for images
            document.querySelector(".discover-section-codes-preview-picture")?.classList.replace("discover-section-codes-preview-picture", "hidden");
            previewImages[index].classList.replace("hidden", "discover-section-codes-preview-picture");

            let selectedType = this.textContent.trim();

            document.querySelector('.discover-section-preview-content-title').textContent = selectedType;
            document.querySelector('.discover-section-preview-content-description').textContent = getDescription(selectedType);
        });
    });
});

function getDescription(type) {
    const descriptions = {
        "URL": "Easily share website links with a QR code.",
        "Text": "A concise way to share messages, discount codes, or crucial information.",
        "Wi-Fi": "Share Wi-Fi network credentials effortlessly.",
        "PDF": "Scan to download and view a PDF document.",
        "Video": "Link directly to a video file for easy access.",
        "MP3": "Provide access to an audio file via QR code.",
        "Image": "Share an image through a scannable QR code."
    };
    return descriptions[type] || "QR Code type not found.";
}

document.querySelectorAll('.nav-link, .footer-right-link, .navbar-brand').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);
        const navbarHeight = document.querySelector('.navbar').offsetHeight; // Get navbar height

        if (targetSection) {
            window.scrollTo({
                top: targetSection.offsetTop - navbarHeight, // Adjust scroll position
                behavior: 'smooth'
            });
        }
    });
});