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
	}
	window.setInterval(jump, 500);
}

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
	}
	window.setInterval(jump, 100);
}

function bigLIs() {
	var li_arr = [].slice.call(document.getElementsByTagName("LI"));
	li_arr.forEach(function(element) {
		element.style.fontSize = '32px';
	});
}

function changeCamelot(str) {
	var camelot_arr = [].slice.call(document.querySelectorAll('.camelot'));
	camelot_arr.forEach(function(element) {
		element.style.visibility = str;
	});
}

function invisibleCamelot() {
	changeCamelot('hidden');
	document.getElementById('visible-camelot').style.visibility = 'visible';
	document.getElementById('invisible-camelot').style.visibility = 'hidden';
}

function visibleCamelot() {
	changeCamelot('visible')
	document.getElementsByClassName('camelot-roof')[0].style.visibility = 'hidden';
	var construction_sign = document.querySelector('div p');
	construction_sign.innerHTML = "Whoops, looks like we had some issues rebuilding the castle...";
	construction_sign.style.color = "red";
}