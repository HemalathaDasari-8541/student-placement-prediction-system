document.addEventListener("DOMContentLoaded", function () {

    const registerForm = document.querySelector(
        'form[action="/register"][method="POST"]'
    );

    if (registerForm) {

        registerForm.addEventListener("submit", function (event) {

            const password =
                document.getElementById("password").value;

            const confirmPassword =
                document.getElementById("confirmPassword").value;

            if (password !== confirmPassword) {

                event.preventDefault();

                alert("Passwords do not match!");

                return;
            }

            alert("Account Created Successfully!");

        });

    }

});