from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget
from page.models import Page, Section,Image
from modeltranslation.forms import TranslationModelForm
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
# Register your models here.

class SectionForm(ModelForm):
	model = Section
	class Meta:
		widgets = {
			'content_en':RedactorWidget(editor_options = { 'lang': 'en' }),
			'content_zh_cn':RedactorWidget(editor_options = { 'lang': 'en' }),
		}
	class Media:
		js = ('/static/bio/js/url_parameter.js',)

class TranslationSectionAdminInline(TranslationStackedInline):
	model = Section
	form = SectionForm
	extra = 1

class ImageAdminInline(admin.TabularInline):
	model = Image
	extra = 1

class TranslationPageAdmin(TranslationAdmin):
	list_display = ("title","s_title","pub_date",)
	fields = ("title","s_title","banner","url_parameter",)
	inlines = (ImageAdminInline,TranslationSectionAdminInline,)

	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(TranslationPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		self.patch_translation_field(db_field, field, **kwargs)
		return field

admin.site.register(Page,TranslationPageAdmin)

