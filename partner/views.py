from django.shortcuts import render_to_response
from partner.models import Partner
from django.template import RequestContext
# Create your views here.
def get_partners(request):
	partners = Partner.objects.all()
	return render_to_response("partner.html",{ "partners":partners },context_instance=RequestContext(request))