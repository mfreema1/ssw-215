//1) Strings - concatenation, array indexing, and methods
const EXAMPLE_STRING = "Example";

//concatenation
const NEW_STRING = "Concatenation " + EXAMPLE_STRING;
console.log(NEW_STRING)

//array index
console.log(EXAMPLE_STRING[1]);

//method
EXAMPLE_STRING.split('').forEach(function(letter) {
	console.log(letter + "\n");
});

//2) Prompt, console.log, and alert
prompt(EXAMPLE_STRING);
console.log(EXAMPLE_STRING);
alert(EXAMPLE_STRING);

//3) Logical and comparison operators
console.log(2 < 3);
console.log(3 != 3);
console.log("five" == 5);

//4) If and else-if
if(2 < 3) {
	console.log("I'm a certified mathematician");
}

if("dog" === "cat") {
	console.log("I'm no vet, but this looks fishy");
}
else if('dog' === 'dog') {
	console.log("Aha, now that's a dog");
}

//5) While loop
var i = 0;
while(i < 5) {
	console.log("Going up");
	i++;
}

//6) For loop
for(var j = 0; j < 5; j++) {
	console.log("We're going way up");
}

//7) Functions without arguments
function addTwoAndFive() {
	return 2 + 5;
	//What a useful function!
}

function alertUserBSoD() {
	alert("Whoops! Something happened and Windows needs to restart");
}

//8) Functions with arguments
function addTwoNumbers(num1, num2) {
	return num1 + num2;
}

//fills each value of the array with zero
function zeroArray(arr) {
	arr.forEach(function(v) {
		v = 0;
	});
}

//9) Scoping
function topSecret() {
	const SUPER_SECRET_PASSCODE = "12345";
	const NOT_THE_PASSCODE = "67890";
	return NOT_THE_PASSCODE;
}

function revealSuperSecretPasscode() {
	//If only there was some way I could access the Passcode!
	return topSecret();
}

//10) Declaring arrays and array methods
var myArr = [1, 2, 3];
var myEmptyArr = new Array();

//array methods, reverse the array
myArr.pop();
myArr.push(1);
myArr.shift();
myArr.unshift(3);
console.log(myArr);