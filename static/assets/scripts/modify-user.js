document.addEventListener('DOMContentLoaded', function() {
    populateUsersTable(usersData);
});

function populateUsersTable(users) {
    var usersTableBody = document.querySelector('#users-table tbody');

    // Clear existing content
    usersTableBody.innerHTML = '';

    // Loop through the users and add rows to the table
    users.forEach(function(user) {
        var row = usersTableBody.insertRow();

        // Create cells for each column
        var idCell = row.insertCell(0);
        var usernameCell = row.insertCell(1);
        var passwordCell = row.insertCell(2);
        var adminCell = row.insertCell(3);
        var actionsCell = row.insertCell(4);

        // Add content to cells
        idCell.innerText = user.id;
        usernameCell.innerHTML = `<div id="user-username-${user.id}" class="editable-info">${user.username}</div>`;
        passwordCell.innerHTML = `<div id="user-password-${user.id}" class="editable-info">${user.password}</div>`;
        adminCell.innerHTML = `<div id="user-admin-${user.id}" class="editable-info">${user.admin}</div>`;
        actionsCell.innerHTML = `<a href="/modify-user?user_id=${user.id}" class="btn btn-primary btn-sm">Edit</a>`;
    });
}

function deleteUser(userId) {
    if (confirm("Are you sure you want to delete this user?")) {
        // Perform deletion logic, for example, send an AJAX request to the server
        // to delete the user with the given ID
        // After successful deletion, you may want to remove the row from the table
        // using JavaScript DOM manipulation

        // Example AJAX request using fetch:
        fetch(`/modify-users`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userId }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Assuming you have a function to remove the row by user ID
                removeUserRow(userId);
            } else {
                alert('Failed to delete user.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while deleting the user.');
        });
    }
}

function removeUserRow(userId) {
    // Implement the logic to remove the row from the table using JavaScript DOM manipulation
    const userRow = document.getElementById(`user-row-${userId}`);
    if (userRow) {
        userRow.remove();
    }
}
