from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from page.models import Page
# Create your views here.
def get_page_by_url_parameter(request, url_parameter):
	page = ''
	try:
		page = Page.objects.get(url_parameter = url_parameter)
	except:
		raise Http404

	return render_to_response("page.html",{ "page":page },context_instance=RequestContext(request))