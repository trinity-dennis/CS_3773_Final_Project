document.addEventListener('DOMContentLoaded', function() {
    // Ensure proper initial display based on the selected item type
    toggleFormFields();

    // Add change event listener to update form fields dynamically
    document.getElementById("item-type").addEventListener("change", toggleFormFields);

    function toggleFormFields() {
        var itemType = document.getElementById("item-type").value;
        var itemNameContainer = document.getElementById("item-name-container");
        var genreContainer = document.getElementById("genre-container");
        var titleContainer = document.getElementById("title-container");
        var authorContainer = document.getElementById("author-container");
        var quantityContainerBooks = document.getElementById("quantity-container-books");
        var priceContainerBooks = document.getElementById("price-container-books");
        var availabilityContainerBooks = document.getElementById("availability-container-books");
        var quantityContainer = document.getElementById("quantity-container");
        var priceContainer = document.getElementById("price-container");
        var availabilityContainer = document.getElementById("availability-container");

        // Reset all form fields
        itemNameContainer.style.display = "none";
        genreContainer.style.display = "none";
        titleContainer.style.display = "none";
        authorContainer.style.display = "none";
        quantityContainerBooks.style.display = "none";
        priceContainerBooks.style.display = "none";
        availabilityContainerBooks.style.display = "none";
        quantityContainer.style.display = "none";
        priceContainer.style.display = "none";
        availabilityContainer.style.display = "none";

        // Display relevant form fields based on the selected item type
        if (itemType === "books") {
            genreContainer.style.display = "block";
            titleContainer.style.display = "block";
            authorContainer.style.display = "block";
            quantityContainerBooks.style.display = "block";
            priceContainerBooks.style.display = "block";
            availabilityContainerBooks.style.display = "block";
        } else if (itemType === "accessories") {
            itemNameContainer.style.display = "block";
            quantityContainer.style.display = "block";
            priceContainer.style.display = "block";
            availabilityContainer.style.display = "block";
        }
    }
    document.getElementById("create-item-form").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        // Gather form data
        var formData = new FormData(this);

        // Use fetch to send data to the server
        fetch('/create-item', {
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
            successMessage.innerHTML = "Item added successfully!";
            document.getElementById("create-item-form").appendChild(successMessage);

            // Optionally, you can handle success (e.g., redirect or show a success message)
        })
        .catch((error) => {
            console.error('Error:', error);
            // Handle errors as needed
        });
    });
});