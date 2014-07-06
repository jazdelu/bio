from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget
from brand.models import Brand, Product, Region, Winery
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
# Register your models here.


class BrandAdminForm(ModelForm):
	model = Brand
	class Meta:
		widgets = {
			'long_description_en':RedactorWidget(editor_options = { 'lang': 'en' }),
			'long_description_zh_cn':RedactorWidget(editor_options = { 'lang': 'en' })
		}

class ProductAdminForm(ModelForm):
	model = Product
	class Meta:
		widgets = {
			'description_en':RedactorWidget(editor_options = { 'lang': 'en'}),
			'description_zh_cn':RedactorWidget(editor_options = { 'lang': 'en'})
		}

class BrandAdmin(TranslationAdmin):
	list_display = ('title','short_description',)
	form = BrandAdminForm
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(BrandAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		self.patch_translation_field(db_field, field, **kwargs)
		return field

admin.site.register(Brand, BrandAdmin)


class WineryAdminForm(ModelForm):
	model = Region
	class Meta:
		widgets = {
			'description_en':RedactorWidget(editor_options = { 'lang': 'en'}),
			'description_zh_cn':RedactorWidget(editor_options = { 'lang': 'en'})
		}

class WineryAdminInline(TranslationStackedInline):
	model = Winery
	form = WineryAdminForm

class RegionAdmin(TranslationAdmin):
	inlines = (WineryAdminInline,)
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(RegionAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		self.patch_translation_field(db_field, field, **kwargs)
		return field

admin.site.register(Region, RegionAdmin)



class ProductAdmin(TranslationAdmin):
	list_display = ('name','brand','pub_date')
	form = ProductAdminForm
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(ProductAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		self.patch_translation_field(db_field, field, **kwargs)
		return field

admin.site.register(Product,ProductAdmin)