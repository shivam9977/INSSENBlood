// This function shows the alert popup with the given message
function showAlertPopup(message) {
    var alertPopup = document.getElementById('alert-popup');
    var alertMessage = document.getElementById('alert-message');
    alertMessage.innerHTML = message;
    alertPopup.style.display = 'block';
}

// This function closes the alert popup
function closeAlertPopup() {
    var alertPopup = document.getElementById('alert-popup');
    alertPopup.style.display = 'none';
}
