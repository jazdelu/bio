from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget
from page.models import Page, Section
# Register your models here.

class SectionForm(ModelForm):
	class Meta:
		widgets = {
			'content':RedactorWidget(editor_options = { 'lang': 'en','focus': 'true' })
		}
	class Media:
		js = ('/static/bio/js/url_parameter.js',)

class SectionAdminInline(admin.StackedInline):
	model = Section
	form = SectionForm
	extra = 1

class PageAdmin(admin.ModelAdmin):
	list_display = ("title","s_title","parent","pub_date",)
	fields = ("title","s_title","parent","banner","url_parameter",)
	inlines = (SectionAdminInline,)

admin.site.register(Page,PageAdmin)

