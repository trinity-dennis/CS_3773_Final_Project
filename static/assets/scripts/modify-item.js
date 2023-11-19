document.addEventListener('DOMContentLoaded', function() {
    // No need to fetch books, as you have them in the template
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
                Quantity: ${book.quantity}<br>
                Price: ${book.price}<br>
                Availability: ${book.availability}
            </div>`;
        actionsCell.innerHTML = `<a href="/modify_item/${book.id}" class="btn btn-primary btn-sm">Edit</a>`;
    });
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

// Attach the toggleItemTable function to the change event of the item type dropdown
document.getElementById("item-type").addEventListener("change", toggleItemTable);