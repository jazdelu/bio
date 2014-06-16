from django.db import models

# Create your models here.

BRAND_TYPE_CHOICES = (
		("wine","BIO IN WINE"),
)

class Brand(models.Model):
	title = models.CharField(max_length = 128, verbose_name= "Brand Title")
	taxonomy = models.CharField(max_length = 128,verbose_name = "Brand Type",choices = BRAND_TYPE_CHOICES, blank = True, null = True)
	short_description = models.CharField(max_length = 128, verbose_name="Short Description")
	banner = models.ImageField(upload_to = "banner/",blank = True, null = True, verbose_name = "Banner", help_text = "780x280 recommend")
	long_description = models.TextField(verbose_name = "Long Description")


	class Meta:
		verbose_name = "Brand"
		verbose_name_plural = "Brand"

	def __unicode__(self):
		return self.title


class Product(models.Model):
	name = models.CharField(max_length = 128, verbose_name  ="Product Name")
	image = models.ImageField(upload_to = "product/", verbose_name = "Product Image")
	attach = models.FileField(upload_to = "file/", verbose_name = "Attachment",blank = True, null = True)
	brand = models.ForeignKey(Brand,verbose_name = "Brand",related_name = "products")
	description = models.TextField(verbose_name = "Description")
	pub_date = models.DateTimeField(auto_now_add = True,verbose_name='Publish Date')
	last_modified = models.DateTimeField(auto_now = True,verbose_name='Last Modified Date')

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Product"

	def __unicode__(self):
		return self.name


