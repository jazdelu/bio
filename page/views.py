from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from page.models import Page
# Create your views here.
def get_page_by_title(request, title):
	page = ''
	title = title.replace('-',' ')
	print title
	page = Page.objects.get(title_en = title)

	return render_to_response("page.html",{ "page":page },context_instance=RequestContext(request))