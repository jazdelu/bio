from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget
from brand.models import Brand, Product
# Register your models here.


class BrandAdminForm(ModelForm):
	model = Brand
	class Meta:
		widgets = {
			'long_description':RedactorWidget(editor_options = { 'lang': 'en','focus': 'true' })
		}

class ProductAdminForm(ModelForm):
	model = Product
	class Meta:
		widgets = {
			'description':RedactorWidget(editor_options = { 'lang': 'en','focus': 'true' })
		}

class BrandAdmin(admin.ModelAdmin):
	list_display = ('title','short_description',)
	form = BrandAdminForm

admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','brand','pub_date')
	form = ProductAdminForm

admin.site.register(Product,ProductAdmin)