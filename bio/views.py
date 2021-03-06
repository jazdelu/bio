from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from banner.models import Banner
from django.utils import translation
from django.core.mail import EmailMultiAlternatives
import re
def home(request):
	banners = Banner.objects.all()
	return render_to_response("index.html",{ "banners":banners },context_instance=RequestContext(request))


def coming(request):
	return render_to_response("coming.html",{ "language":"en" },context_instance=RequestContext(request))

def coming_cn(request):
	return render_to_response("coming_cn.html",{ "language":"cn" },context_instance=RequestContext(request))

def sendmail(request):
	error = ''
	if request.POST:
		content = request.POST['email']
		language = request.POST['language']
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", content) != None:
			subject = 'A new email is submitted from www.bio-inbev.com'
			msg = EmailMultiAlternatives(subject, content, 'robot@minibobi.com', ['contact@bio-inbev.com'])
			msg.send()
		else:
			error = 'Please submit a valid E-mail!'

		if language == 'en':
			return render_to_response("coming.html",{'error':error,'language':'en'},context_instance=RequestContext(request))
		else:
			return render_to_response("coming_cn.html",{'error':error,'language':'cn'},context_instance=RequestContext(request))


	else:
		return HttpResponseRedirect("/")


def contact(request):
	return render_to_response("contact.html",context_instance=RequestContext(request))

def set_language(request):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get('language', None)
        if lang_code and translation.check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            print translation.activate(lang_code)
    return response