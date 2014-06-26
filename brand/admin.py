from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget
from brand.models import Brand, Product, Region, Winery
# Register your models here.


class BrandAdminForm(ModelForm):
	model = Brand
	class Meta:
		widgets = {
			'long_description':RedactorWidget(editor_options = { 'lang': 'en' })
		}

class ProductAdminForm(ModelForm):
	model = Product
	class Meta:
		widgets = {
			'description':RedactorWidget(editor_options = { 'lang': 'en'})
		}
	class Media:
		js = ('/static/bio/js/admin_extra.js',)

class BrandAdmin(admin.ModelAdmin):
	list_display = ('title','short_description',)
	form = BrandAdminForm

admin.site.register(Brand, BrandAdmin)


class WineryAdminForm(ModelForm):
	model = Region
	class Meta:
		widgets = {
			'description':RedactorWidget(editor_options = { 'lang': 'en'})
		}

class WineryAdminInline(admin.StackedInline):
	model = Winery
	form = WineryAdminForm

class RegionAdmin(admin.ModelAdmin):
	inlines = (WineryAdminInline,)

admin.site.register(Region, RegionAdmin)



class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','brand','pub_date')
	form = ProductAdminForm

admin.site.register(Product,ProductAdmin)