$(function(){
	$("#id_url_parameter").attr("readonly","readonly");
	$("#id_title").change(function(){
		var title = $(this).val();
		var url = title.toLowerCase().replace(/ /g,"-");
		$("#id_url_parameter").val(url);
	});
});