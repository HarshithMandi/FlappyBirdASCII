import { getProperty } from "./generisProps";

const user = {
    name: "John",
    age: 30,
    location: "New York"
};

const userName = getProperty(user, "name");
const userAge = getProperty(user, "age");
const userLocation = getProperty(user, "location");
console.log(`Name: ${userName}, Age: ${userAge}, Location: ${userLocation}`);