function showAlert(type, message) {
    if (type === "success") {
        alert(`Success: ${message}`);
    } else if (type === "error") {
        alert(`Error: ${message}`);
    }
}