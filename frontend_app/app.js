function loadForm(action) {
    const formContainer = document.getElementById('formContainer');
    const response = document.getElementById('response');
    response.innerHTML = ''; // Clear previous response

    let formHTML = `<h3>${action}</h3><form onsubmit="submitForm(event, '${action}')">`;

    switch(action) {
        case 'createUser':
            formHTML += `
                <label>Name: <input type="text" name="name"></label>
                <label>Email: <input type="email" name="email" required></label>
                <label>Gender: <input type="text" name="gender"></label>
                <label>Phone Number: <input type="text" name="phone_number"></label>
                <label>Password: <input type="password" name="password" required></label>`;
            break;
        
        case 'loginUser':
            formHTML += `
                <label>Email: <input type="email" name="email"></label>
                <label>Phone Number: <input type="text" name="phone_number"></label>
                <label>Password: <input type="password" name="password" required></label>`;
            break;
        
        case 'bookTicket':
            formHTML += `
                <label>User ID: <input type="number" name="user_id" required></label>
                <label>Route ID: <input type="number" name="route_id"></label>
                <label>Starting Stop Number: <input type="number" name="starting_stop_number" required></label>
                <label>Ending Stop Number: <input type="number" name="ending_stop_number" required></label>
                <label>Gender: <input type="text" name="gender"></label>
                <label>Category: <input type="text" name="category" required></label>`;
            break;

        case 'getFare':
            formHTML += `
                <label>Bus Number: <input type="text" name="bus_number"></label>
                <label>Starting Stop Number: <input type="number" name="starting_stop_number" required></label>
                <label>Ending Stop Number: <input type="number" name="ending_stop_number" required></label>
                <label>Category: <input type="text" name="category" required></label>`;
            break;
        
        case 'createEmployee':
            formHTML += `
                <label>Username: <input type="text" name="user_name"></label>
                <label>First Name: <input type="text" name="first_name"></label>
                <label>Last Name: <input type="text" name="last_name"></label>
                <label>Email: <input type="email" name="official_email" required></label>
                <label>Password: <input type="password" name="password" required></label>
                <label>Phone Number: <input type="text" name="phone_number"></label>
                <label>Access Level ID: <input type="text" name="access_level_id"></label>
                <label>Salary: <input type="number" step="0.01" name="salary"></label>`;
            break;
        
        case 'loginEmployee':
        case 'logoutEmployee':
            formHTML += `
                <label>Email: <input type="email" name="official_email" required></label>
                <label>Password: <input type="password" name="password" required></label>`;
            break;
    }

    formHTML += `<button type="submit" class="submit-btn">Submit</button></form>`;
    formContainer.innerHTML = formHTML;
}

const routeMapping = {
    createUser: 'create',
    loginUser: 'login',
    bookTicket: 'ticket',
    getFare: 'fare',
    createEmployee: 'create',
    loginEmployee: 'login',
    logoutEmployee: 'logout'
};

// Function to submit the form data
function submitForm(event, action) {
    event.preventDefault(); // Prevents page refresh
    const form = event.target; // Form being submitted
    const formData = new FormData(form); // Form data
    const data = {};

    // Convert form data to a JavaScript object
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Base URL for the backend server
    const baseUrl = 'http://127.0.0.1:5002/';
    const endpoint = routeMapping[action] || action.toLowerCase();

    // Determine URL and options based on action type
    let url = `${baseUrl}user/${endpoint}`;
    let options = {
        headers: { 'Content-Type': 'application/json' },
    };

    if (action === 'getFare') {
        // For `GET` request, add query parameters
        const queryParams = new URLSearchParams(data).toString();
        url += `?${queryParams}`;
        options.method = 'GET';
    } else {
        // For `POST` request
        options.method = 'POST';
        options.body = JSON.stringify(data);
    }

    // Fetch request to backend
    fetch(url)
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw err; });
            }
            return response.json();
        })
        .then(result => {
            document.getElementById('response').innerHTML = JSON.stringify(result, null, 2);
        })
        .catch(error => {
            document.getElementById('response').innerHTML = `Error: ${error.message || error}`;
        });
}