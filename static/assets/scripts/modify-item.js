document.addEventListener('DOMContentLoaded', function() {
    populateBooksTable(booksData);
    populateAccessoriesTable(accessoriesData);
});

function populateBooksTable(books) {
    var booksTableBody = document.querySelector('#books-table tbody');

    // Clear existing content
    booksTableBody.innerHTML = '';

    // Loop through the books and add rows to the table
    books.forEach(function(book) {
        var row = booksTableBody.insertRow();

        // Create cells for each column
        var imageCell = row.insertCell(0);
        var detailsCell = row.insertCell(1);
        var actionsCell = row.insertCell(2);

        // Add content to cells
        imageCell.innerHTML = `<img src="${book.img}" alt="Book Image" height="50">`;
        detailsCell.innerHTML = `
            <div>
                <strong>${book.title}</strong><br>
                <small>${book.author}</small>
            </div>
            <div>
                Genre: ${book.genre}<br>
                Price: ${book.price}<br>
                Availability: ${book.availability}
            </div>`;
        actionsCell.innerHTML = `<a href="/modify-item?item_type=book&item_id=${book.id}" class="btn btn-primary btn-sm">Edit</a>`;
    });
}

// Function to populate the Accessories table
function populateAccessoriesTable(accessories) {
    var accessoriesTableBody = document.querySelector('#accessories-table tbody');

    // Clear existing content
    accessoriesTableBody.innerHTML = '';

    // Loop through the accessories and add rows to the table
    accessories.forEach(function(accessory) {
        var row = accessoriesTableBody.insertRow();

        // Create cells for each column
        var imageCell = row.insertCell(0);
        var detailsCell = row.insertCell(1);
        var actionsCell = row.insertCell(2);

        // Add content to cells
        imageCell.innerHTML = `<img src="${accessory.img}" alt="Accessory Image" height="50">`;
        detailsCell.innerHTML = `
            <div>
                <strong>${accessory.item_name}</strong>
            </div>
            <div>
                Price: ${accessory.price}<br>
                Availability: ${accessory.availability}
            </div>`;
        actionsCell.innerHTML = `<a href="/modify-item?item_type=accessory&item_id=${accessory.id}" class="btn btn-primary btn-sm">Edit</a>`;
    });
}

function toggleEdit(type, id) {
    var infoDiv = document.getElementById(`${type}-info-${id}`);
    var detailsDiv = document.getElementById(`${type}-details-${id}`);
    var editButton = document.querySelector(`#${type}-edit-${id}`);
    var submitButton = document.querySelector(`#${type}-submit-${id}`);
    var cancelButton = document.querySelector(`#${type}-cancel-${id}`);

    // Toggle contenteditable attribute
    infoDiv.querySelectorAll('span').forEach(element => {
        element.contentEditable = (element.contentEditable === 'true') ? 'false' : 'true';
    });

    detailsDiv.querySelectorAll('span').forEach(element => {
        element.contentEditable = (element.contentEditable === 'true') ? 'false' : 'true';
    });

    // Toggle visibility of buttons
    editButton.style.display = 'none';
    submitButton.style.display = 'block';
    cancelButton.style.display = 'block';
}

function submitBookChanges(type, id) {
    console.log('Submit button clicked:', type, id);
    var infoDiv = document.getElementById(`${type}-info-${id}`);
    var detailsDiv = document.getElementById(`${type}-details-${id}`);
    var editButton = document.querySelector(`#${type}-edit-${id}`);
    var submitButton = document.querySelector(`#${type}-submit-${id}`);
    var cancelButton = document.querySelector(`#${type}-cancel-${id}`);

    console.log('infoDiv:', infoDiv);
    console.log('detailsDiv:', detailsDiv);
    console.log('editButton:', editButton);
    console.log('submitButton:', submitButton);
    console.log('cancelButton:', cancelButton);

    // Get updated values
    var newGenre = detailsDiv.querySelector('span[data-field="genre"]').innerText;
    var newPrice = detailsDiv.querySelector('span[data-field="price"]').innerText;
    var newAvailability = detailsDiv.querySelector('span[data-field="availability"]').innerText;

    console.log('newGenre:', newGenre);
    console.log('newPrice:', newPrice);
    console.log('newAvailability:', newAvailability);

    // Make a fetch request to update the item in the database
    fetch('/modify-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            item_type: type,
            item_id: id,
            genre: newGenre,
            price: newPrice,
            availability: newAvailability,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        if (data.success) {
            console.log(data.message);
            // Update the UI if needed
        } else {
            console.error(data.message);
            // Handle the error
        }
    })
    .catch(error => {
        console.error('Error submitting changes:', error);
    });

    // Toggle contenteditable attribute back to false
    infoDiv.querySelectorAll('span').forEach(element => {
        element.contentEditable = 'false';
    });

    detailsDiv.querySelectorAll('span').forEach(element => {
        element.contentEditable = 'false';
    });

    // Toggle visibility of buttons
    editButton.style.display = 'block';
    submitButton.style.display = 'none';
    cancelButton.style.display = 'none';
}

function submitAccessoryChanges(type, id) {
    console.log('Submit button clicked:', type, id);
    var infoDiv = document.getElementById(`${type}-info-${id}`);
    var detailsDiv = document.getElementById(`${type}-details-${id}`);
    var editButton = document.querySelector(`#${type}-edit-${id}`);
    var submitButton = document.querySelector(`#${type}-submit-${id}`);
    var cancelButton = document.querySelector(`#${type}-cancel-${id}`);

    console.log('infoDiv:', infoDiv);
    console.log('detailsDiv:', detailsDiv);
    console.log('editButton:', editButton);
    console.log('submitButton:', submitButton);
    console.log('cancelButton:', cancelButton);

    // Get updated values
    var newPrice = detailsDiv.querySelector('span[data-field="price"]').innerText;
    var newAvailability = detailsDiv.querySelector('span[data-field="availability"]').innerText;

    console.log('newPrice:', newPrice);
    console.log('newAvailability:', newAvailability);

    // Make a fetch request to update the item in the database
    fetch('/modify-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            item_type: type,
            item_id: id,
            price: newPrice,
            availability: newAvailability,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        if (data.success) {
            console.log(data.message);
            // Update the UI if needed
        } else {
            console.error(data.message);
            // Handle the error
        }
    })
    .catch(error => {
        console.error('Error submitting changes:', error);
    });

    // Toggle contenteditable attribute back to false
    infoDiv.querySelectorAll('span').forEach(element => {
        element.contentEditable = 'false';
    });

    detailsDiv.querySelectorAll('span').forEach(element => {
        element.contentEditable = 'false';
    });

    // Toggle visibility of buttons
    editButton.style.display = 'block';
    submitButton.style.display = 'none';
    cancelButton.style.display = 'none';
}

function cancelEdit(type, id) {
    var infoDiv = document.getElementById(`${type}-info-${id}`);
    var detailsDiv = document.getElementById(`${type}-details-${id}`);
    var editButton = document.querySelector(`#${type}-edit-${id}`);
    var submitButton = document.querySelector(`#${type}-submit-${id}`);
    var cancelButton = document.querySelector(`#${type}-cancel-${id}`);

    // Revert content back to the original state
    infoDiv.querySelectorAll('span').forEach(element => {
        element.innerText = element.dataset.originalValue;
        element.contentEditable = 'false';
    });

    detailsDiv.querySelectorAll('span').forEach(element => {
        element.innerText = element.dataset.originalValue;
        element.contentEditable = 'false';
    });

    // Toggle visibility of buttons
    editButton.style.display = 'block';
    submitButton.style.display = 'none';
    cancelButton.style.display = 'none';
}

// Function to toggle between Books and Accessories
function toggleItemTable() {
    var itemType = document.getElementById("item-type").value;
    var booksTable = document.getElementById("books-table");
    var accessoriesTable = document.getElementById("accessories-table");

    if (itemType === "books") {
        booksTable.style.display = "block";
        accessoriesTable.style.display = "none";
    } else if (itemType === "accessories") {
        booksTable.style.display = "none";
        accessoriesTable.style.display = "block";
    }
}

function applyBookChanges(type, itemId) {
    var priceElement = document.querySelector(`#book-details-${itemId} [data-field="price"]`);
    var reductionDropdown = document.querySelector(`#reduction-dropdown-${itemId}`);
    var moveToHomepageCheckbox = document.querySelector(`#move-to-homepage-${itemId}`);
    var genreElement = document.querySelector(`#book-details-${itemId} [data-field="genre"]`);
    var availabilityElement = document.querySelector(`#book-details-${itemId} [data-field="availability"]`);

    var originalPrice = parseFloat(priceElement.getAttribute('data-original-value'));
    var reductionPercentage = parseFloat(reductionDropdown.value);
    var newPrice = originalPrice - (originalPrice * reductionPercentage);

    // Update the price in the UI
    priceElement.innerText = newPrice.toFixed(2);

    // Send the changes to the server
    fetch("/modify-item", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            item_type: type,
            item_id: itemId,
            price: newPrice,
            move_to_homepage: moveToHomepageCheckbox.checked,
            reduction_percentage: reductionPercentage,
            genre: genreElement.innerText,  // Include genre in the data
            availability: availabilityElement.innerText  // Include availability in the data
        })
    })
    .then(response => response.json())
    .then(data => {
        // Handle success or error from the server if needed
        console.log(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function applyAccessoryChanges(type, itemId) {
    var priceElement = document.querySelector(`#book-details-${itemId} [data-field="price"]`);
    var reductionDropdown = document.querySelector(`#reduction-dropdown-${itemId}`);
    var moveToHomepageCheckbox = document.querySelector(`#move-to-homepage-${itemId}`);
    var genreElement = document.querySelector(`#book-details-${itemId} [data-field="genre"]`);
    var availabilityElement = document.querySelector(`#book-details-${itemId} [data-field="availability"]`);

    var originalPrice = parseFloat(priceElement.getAttribute('data-original-value'));
    var reductionPercentage = parseFloat(reductionDropdown.value);
    var newPrice = originalPrice - (originalPrice * reductionPercentage);

    // Update the price in the UI
    priceElement.innerText = newPrice.toFixed(2);

    // Send the changes to the server
    fetch("/modify-item", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            item_type: type,
            item_id: itemId,
            price: newPrice,
            move_to_homepage: moveToHomepageCheckbox.checked,
            reduction_percentage: reductionPercentage,
            availability: availabilityElement.innerText  // Include availability in the data
        })
    })
    .then(response => response.json())
    .then(data => {
        // Handle success or error from the server if needed
        console.log(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

// Attach the toggleItemTable function to the change event of the item type dropdown
document.addEventListener('DOMContentLoaded', function() {
    // Your existing code here
    document.getElementById("item-type").addEventListener("change", toggleItemTable);
});