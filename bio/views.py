from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from banner.models import Banner
from django.core.mail import send_mail

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
		send_mail('A New Email is submiited from www.bio-inbev.com', content, 'contact@bio-inbev.com',
    ['lushizhao@qq.com'])
		status = 0
		if language == 'en':
			return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/cn/")

	else:
		return HttpResponseRedirect("/")

