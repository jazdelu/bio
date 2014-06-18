from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from banner.models import Banner
from django.core.mail import EmailMultiAlternatives

def home(request):
	banners = Banner.objects.all()
	return render_to_response("index.html",{ "banners":banners },context_instance=RequestContext(request))


def coming(request):
	return render_to_response("coming.html",{ "language":"en" },context_instance=RequestContext(request))

def coming_cn(request):
	return render_to_response("coming_cn.html",{ "language":"cn" },context_instance=RequestContext(request))

def sendmail(request):
	status = 1
	if request.POST:
		content = request.POST['email']
		language = request.POST['language']
		subject = 'A new email is submitted from www.bio-inbev.com'
		msg = EmailMultiAlternatives(subject, content, 'robot@minibobi.com', ['contact@bio-inbev.com'])
		msg.send()
		status = 0
		if language == 'en':
			return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/cn/")

	else:
		return HttpResponseRedirect("/")

