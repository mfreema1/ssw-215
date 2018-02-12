var myComputer = {
	year_of_manufacture: 2015,
	vendor: 'HP',
	operating_system: 'linux',
	model: 'Spectre x360',
	calculate_age: function() {
		return 2018 - this.year_of_manufacture;
	}
};

//really wish js had a built-in range function like python
first_10_numbers = [1,2,3,4,5,6,7,8,9,10];
function squareElements(arr) {
	return arr.map(function(x) {return x * x});
}
first_10_squares = squareElements(first_10_numbers);

var inventory = {
	store_name: 'Costco',
	store_address: '123 Fake Street',
	stock: [
	{
		title: 'The Little Engine that Could',
		author: 'Johnny McWriterman',
		price: 4.50
	},
	{
		title: 'A Farewell to Arms',
		author: 'Steve Importantguy',
		price: 10.25
	},
	{
		title: 'Why Ducks are So Mean',
		author: 'Liam Duckworth',
		price: 6.50
	},
	{
		title: 'Rocket Surgery for Dummies',
		author: 'Neel Degrass Dyson',
		price: 5.00
	},
	{
		title: 'The Fifth Book',
		author: 'Cameron James-Dean V',
		price: 5.50
	}]
};