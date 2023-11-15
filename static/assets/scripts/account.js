window.onload = function() {
    function openLoginForm() {
        document.getElementById("login-form-container").style.display = "flex";
        document.getElementById("overlay").style.display = "block";
    }

    function closeLoginForm() {
        document.getElementById("login-form-container").style.display = "none";
        document.getElementById("overlay").style.display = "none";
    }

    document.getElementById("login-button").onclick = function () {
        openLoginForm();
    };

      function openSignupForm() {
        document.getElementById("signup-form-container").style.display = "flex";
        document.getElementById("overlay").style.display = "block";
    }

    function closeSignupForm() {
        document.getElementById("signup-form-container").style.display = "none";
        document.getElementById("overlay").style.display = "none";
    }

    document.getElementById("signup-button").onclick = function () {
        openSignupForm();
    };
};