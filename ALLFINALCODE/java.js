// Function to generate random number between min and max (inclusive)
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Function to generate password
function generatePassword() {
    var word1 = document.getElementById("word1").value.substring(0, 6); // Limit to 6 characters
    var word2 = document.getElementById("word2").value.substring(0, 6); // Limit to 6 characters

    // Generate random numbers to add to the password
    var randomNumber1 = getRandomNumber(0, 99);
    var randomNumber2 = getRandomNumber(100, 999);

    // Concatenate the words and random numbers together to form the password
    var password = word1 + randomNumber1 + word2 + randomNumber2;

    // Display the generated password
    var passwordDiv = document.getElementById("password");
    passwordDiv.innerHTML = "<h2>Generated Password</h2>";
    passwordDiv.innerHTML += "<p><strong>Password:</strong> " + password + "</p>";

    // Clear input fields after displaying the password
    document.getElementById("word1").value = "";
    document.getElementById("word2").value = "";
}
