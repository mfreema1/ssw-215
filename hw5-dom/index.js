jump_ctr = 0;

function jumpChristmasHeader() {
	var header = document.getElementById("king");
	function jump() {
		if(jump_ctr % 2 == 0) {
			header.style.color = "green";
			header.style.float = "right";
		}
		else {
			header.style.color = "red";
			header.style.float = "left";
		}
		jump_ctr += 1;
	};
	window.setInterval(jump, 500);
};

function knightRainbowRun() {
	var knightsArr = [].slice.call(document.getElementsByClassName("knight"));
	var colors = ['blue', 'gray', 'green', 'orange', 'red', 'purple'];
	//that's some nice scoping there
	knightsArr.forEach(function(element) {
		index = knightsArr.indexOf(element);
		element.style.color = colors[index];
	});
	function jump() {
		//shift the colors one space right
		knightsArr.forEach(function(element) {
			new_index = colors.indexOf(element.style.color) + 1;
			if(new_index == 6)
				new_index = 0;
			element.style.color = colors[new_index];
		});
	};
	window.setInterval(jump, 100);
};