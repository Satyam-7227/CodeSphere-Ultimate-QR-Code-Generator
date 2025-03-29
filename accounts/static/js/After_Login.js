// -------------------------Sidebar-Toggle-------------------------
document.querySelector('.navigation-control-icon-block').addEventListener('click', function () {
    let sidebar = document.getElementById('sidebar');
    let toggleButton = document.querySelector('.navigation-control-icon-block');
    let screenWidth = window.innerWidth;

    if (screenWidth > 800) {
        sidebar.classList.toggle('shrink');
    } else {
        sidebar.classList.toggle('active');
    }

    if (sidebar.classList.contains('active') || sidebar.classList.contains('shrink')) {
        toggleButton.classList.add('moved');
    } else {
        toggleButton.classList.remove('moved');
    }
});

// -------------------------RightSideContent-&-ActiveButton-Change-------------------------
function toggleSection(section) {
    document.querySelectorAll(".section").forEach(div => div.style.display = "none");
    document.getElementById(section).style.display = "block";

    // Remove active class from all buttons
    document.querySelectorAll(".sidebar-btn").forEach(btn => btn.classList.remove("active-btn"));

    // Add active class to the clicked button
    document.querySelector(`button[onclick="toggleSection('${section}')"]`).classList.add("active-btn");
}

// -------------------------ActiveButton-ReloadCondition-------------------------
document.addEventListener("DOMContentLoaded", function () {
    let showProfile = sessionStorage.getItem("showProfile"); // Check stored value

    if (showProfile === "true") {
        toggleSection("profile");  // Show Profile section
        sessionStorage.setItem("showProfile", "false");  // Reset it after reload
    } else {
        toggleSection("generate"); // Default section on normal reload
    }
});

// -------------------------Detect-ChangePassword-Button-------------------------
document.querySelector("button[name='change_password']").addEventListener("click", function () {
    sessionStorage.setItem("showProfile", "true");  // Set flag to show Profile after reload
});

// -------------------------QR-Generation-Form-------------------------
function showForm(type) {
    let inputField = document.getElementById("dynamicInput");
    document.getElementById("qrType").value = type; // Set hidden input for backend

    if (type === "url") {
        inputField.innerHTML = `<label>Enter URL</label><input type="text" id="qr-content" name="content" required>`;
    } else {
        inputField.innerHTML = `<label>Upload ${type}</label><input type="file" id="qr-content" name="content" accept="${getFileType(type)}" required>`;
    }
}

// Function to return correct file type
function getFileType(type) {
    return type === "image" ? "image/*" :
        type === "video" ? "video/*" :
            type === "pdf" ? "application/pdf" : "";
}