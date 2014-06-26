$(function(){
	$(".field-winery").hide();
	$("#id_brand").change(function(){
		if ($("#id_brand").find("option:selected").text() == 'bio in wine'){
			$(".field-winery").show();
		}
		else{
			$(".field-winery").hide();
		}
	});
});