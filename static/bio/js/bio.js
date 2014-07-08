	$(function(){
		var timeout = "";
		var sub = ""
		$(".sub").mouseover(function(){
			sub = $(this).attr("data");
			$(sub).show('slide', {direction: 'left'}, 300);
		}).mouseleave(function(){
			sub = $(this).attr("data");
			timeout  = setTimeout(function(){$(sub).hide('slide', {direction: 'left'}, 300);},50);
		});
		$(".sub-nav-holder").mouseover(function(){
			clearTimeout(timeout);
		}).mouseleave(function(){
			$(".sub-nav-holder").hide('slide', {direction: 'left'}, 300);
		});
	});