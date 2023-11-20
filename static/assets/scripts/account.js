document.addEventListener('DOMContentLoaded', function() {
    checkLoginStatus();
});
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

        document.getElementById("login-close-button").onclick = function () {
            closeLoginForm();
        };

        document.getElementById("login-form").onsubmit = submitLoginForm;

        function submitLoginForm(event) {
            // prevent the form from submitting in the traditional way
            event.preventDefault();

            var username = document.getElementById("login-username").value;
            var password = document.getElementById("login-password").value;

            // create data object to send with AJAX request
            var data = {
                "login-username": username,
                "login-password": password
            };

            // send AJAX request to Flask server
            fetch("/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Successful login, close the form
                    closeLoginForm();
                    updateNavigationForLoggedInUser(username);
                    //location.reload()
                } else {
                    // Failed login, display the error message
                    document.querySelector('.error-message').innerHTML = data.error || "Invalid username or password";
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }

        function updateNavigationForLoggedInUser(username) {
            var loginButton = document.getElementById("login-button");
            var signupButton = document.getElementById("signup-button");
            var usernameButton = document.createElement("span");
            var logoutButton = document.createElement("a");

            loginButton.style.display = "none";
            signupButton.style.display = "none";

            usernameButton.className = "nav-link link-body-emphasis px-2";
            logoutButton.className = "nav-link link-body-emphasis px-2";

            var nav = document.querySelector('.nav');

            if (username === "admin") {
                // Create a dropdown for admin
                var adminDropdown = document.createElement("div");
                adminDropdown.className = "nav-item dropdown";

                var adminDropdownToggle = document.createElement("button");
                adminDropdownToggle.className = "nav-link link-body-emphasis px-2 dropdown-toggle";
                adminDropdownToggle.setAttribute("data-bs-toggle", "dropdown");
                adminDropdownToggle.innerText = username;

                var adminDropdownMenu = document.createElement("div");
                adminDropdownMenu.className = "dropdown-menu";

                var adminOption1 = document.createElement("a");
                adminOption1.className = "dropdown-item";
                adminOption1.innerText = "Option 1";

                var adminOption2 = document.createElement("a");
                adminOption2.className = "dropdown-item";
                adminOption2.innerText = "Option 2";

                var adminOption3 = document.createElement("a");
                adminOption2.className = "dropdown-item";
                adminOption2.innerText = "Option 3";

                adminDropdownMenu.appendChild(adminOption1);
                adminDropdownMenu.appendChild(adminOption2);
                adminDropdownMenu.appendChild(adminOption3);

                adminDropdown.appendChild(adminDropdownToggle);
                adminDropdown.appendChild(adminDropdownMenu);

                nav.appendChild(adminDropdown);
            } else {
                // Display regular username
                usernameButton.innerText = username;
                nav.appendChild(usernameButton);
            }

            logoutButton.href = "/logout";
            logoutButton.innerText = "Log out";
            nav.appendChild(logoutButton);
        }

        //makes sure that if someone is logged in, they don't sign out for any reason
        function checkLoginStatus() {
        fetch("/check_login_status")
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Update navigation if the user is logged in
                    updateNavigationForLoggedInUser(data.username);
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }

        //checkLoginStatus();

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
                document.getElementById("signup-form").reset();
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