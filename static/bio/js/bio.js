	$(function(){
		var timeout="";
		$(".sub").mouseover(function(){
			$(".sub-nav-holder").fadeIn();
		}).mouseleave(function(){
			timeout = setTimeout(function(){$(".sub-nav-holder").fadeOut();},1000);
		});
		$(".sub-nav-holder").mouseover(function(){
			clearTimeout(timeout);
		}).mouseleave(function(){
			setTimeout(function(){$(".sub-nav-holder").fadeOut();},500);
		});
	});