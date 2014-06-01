from django.shortcuts import render_to_response

def home(request):
	return render_to_response("index.html")

def brand(request):
	return render_to_response("brand.html")

def consumption(request):
	return render_to_response("consumption.html")

def about(request):
	return render_to_response("about.html")