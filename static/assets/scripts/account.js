window.onload = function() {
    // login form
    function openLoginForm() {
        document.getElementById("login-form-container").style.display = "flex";
        document.getElementById("login-overlay").style.display = "block";
    }

    function closeLoginForm() {
        document.getElementById("login-form-container").style.display = "none";
        document.getElementById("login-overlay").style.display = "none";
    }

    document.getElementById("login-button").onclick = function () {
        openLoginForm();
    };

    // signup form
    function openSignupForm() {
        document.getElementById("signup-form-container").style.display = "flex";
        document.getElementById("signup-overlay").style.display = "block";
    }

    function closeSignupForm() {
        document.getElementById("signup-form-container").style.display = "none";
        document.getElementById("signup-overlay").style.display = "none";
    }

    function submitSignupForm(event) {
        // prevent the form from submitting in the traditional way
        event.preventDefault();

        var username = document.getElementById("signup-username").value;
        var password = document.getElementById("signup-password").value;

        // create data object to send with AJAX request
        var data = {
            "signup-username": username,
            "signup-password": password
        };

        // send AJAX request to Flask server
        fetch("/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            closeSignupForm();
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }

    document.getElementById("signup-form").onsubmit = submitSignupForm;

    document.getElementById("signup-button").onclick = function () {
        openSignupForm();
    };


};