from modeltranslation.translator import translator, TranslationOptions
from brand.models import *

class BrandTranslationOptions(TranslationOptions):
	fields = ('title','short_description','long_description',)
	required_languages = ('en','zh-cn',)

translator.register(Brand, BrandTranslationOptions)

class RegionTranslationOptions(TranslationOptions):
	fields = ('name',)

translator.register(Region,RegionTranslationOptions)

class WineryTranslationOptions(TranslationOptions):
	fields = ('name','description',)

translator.register(Winery,WineryTranslationOptions)

class ProductTranslationOptions(TranslationOptions):
	fields = ('name','description',)

translator.register(Product,ProductTranslationOptions)