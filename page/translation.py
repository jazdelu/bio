from modeltranslation.translator import translator, TranslationOptions
from page.models import *

class PageTranslationOptions(TranslationOptions):
	fields = ('title','s_title',)

translator.register(Page,PageTranslationOptions)

class SectionTranslationOptions(TranslationOptions):
	fields = ('title','content')

translator.register(Section,SectionTranslationOptions)