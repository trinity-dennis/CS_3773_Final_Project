document.getElementById("create-item-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Gather form data
    var formData = new FormData(this);

    // Use fetch to send data to the server
    fetch('/discounts', {  // Update the endpoint to '/discounts'
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);

        // Clear the form fields
        document.getElementById("create-item-form").reset();

        // Display success message above the submit button
        var successMessage = document.createElement("div");
        successMessage.className = "alert alert-success mt-3";
        successMessage.innerHTML = "Discount added successfully!";
        document.getElementById("create-item-form").appendChild(successMessage);

        // Optionally, you can handle success (e.g., redirect or show a success message)
    })
    .catch((error) => {
        console.error('Error:', error);
        // Handle errors as needed
    });
});