from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from brand.models import Brand, Product

# Create your views here.
def get_brand_by_title(request, title):
	brand = ''
	try:
		brand = Brand.objects.get(title = title)
	except:
		raise Http404
	return render_to_response("brand.html",{ "brand":brand },context_instance=RequestContext(request))