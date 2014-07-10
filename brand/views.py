from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from brand.models import Brand, Product,Region,Winery

# Create your views here.
def get_brand_by_title(request, title):
	brand = ''
	title = title.replace("-",' ')
	print title
	brand = Brand.objects.get(title_en = title)
	if brand.title.lower() != 'bio in vine':
		return render_to_response("brand.html",{ "brand":brand },context_instance=RequestContext(request))
	else:
		regions = Region.objects.all()
		if request.GET:
			wineries = []
			key = request.GET['r']
			if key == 'all':
				wineries = Winery.objects.all()
			else:
				wineries = Winery.objects.filter(region = int(key))
			return render_to_response("wineries.html", { "brand":brand, "regions":regions, "wineries":wineries,"key":key }, context_instance = RequestContext(request))
		else:
			return render_to_response("biw.html", { "brand":brand, "regions":regions,}, context_instance = RequestContext(request))



def get_winery_by_id(request, wid):
	winery = ''
	try:
		winery = Winery.objects.get(id = int(wid))
	except:
		raise Http404
	return render_to_response("winery.html",{ "winery":winery }, context_instance = RequestContext(request))