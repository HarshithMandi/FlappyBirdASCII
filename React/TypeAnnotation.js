function validateUserInput(input) {
    if (input.length < 5) {
        console.log("Input is too short.");
        return false;
    }
    if (!/^[a-zA-Z0-9]+$/.test(input)) {
        console.log("Input contains invalid characters.");
        return false;
    }
    return true;
}
var userInput = "abc123";
if (validateUserInput(userInput)) {
    console.log("User input is valid.");
}
else {
    console.log("User input is invalid.");
}
