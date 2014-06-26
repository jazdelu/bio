from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from brand.models import Brand, Product,Region,Winery

# Create your views here.
def get_brand_by_title(request, title):
	brand = ''
	title = title.replace("-",' ')
	print title
	brand = Brand.objects.get(title = title)
	if brand.title.lower() != 'bio in wine':
		return render_to_response("brand.html",{ "brand":brand },context_instance=RequestContext(request))
	else:
		regions = Region.objects.all()
		return render_to_response("biw.html", { "brand":brand, "regions":regions }, context_instance = RequestContext(request))


def get_winery_by_id(request,wid):
	winery = ''
	winery = Winery.objects.get(id = int(wid))

	return render_to_response("winery.html",{ "winery":winery }, context_instance = RequestContext(request))
