window.onload = function() {
    function openForm() {
        document.getElementById("login-form-container").style.display = "flex";
        document.getElementById("overlay").style.display = "block";
    }

    function closeForm() {
        document.getElementById("login-form-container").style.display = "none";
        document.getElementById("overlay").style.display = "none";
    }

    document.getElementById("login-button").onclick = function () {
        openForm();
    };
};