from django.db import models

# Create your models here.



class Brand(models.Model):
	title = models.CharField(max_length = 128, verbose_name= "Brand Title")
	short_description = models.CharField(max_length = 128, verbose_name="Short Description",blank = True, null = True)
	banner = models.ImageField(upload_to = "banner/",blank = True, null = True, verbose_name = "Banner", help_text = "780x280 recommend")
	long_description = models.TextField(verbose_name = "Long Description")


	class Meta:
		verbose_name = "Brand"
		verbose_name_plural = "Brand"

	def __unicode__(self):
		return self.title

class Region(models.Model):
	name = models.CharField(max_length = 128, verbose_name ='Name')

	class Meta:
		verbose_name = "Region"
		verbose_name_plural = "Region"

	def __unicode__(self):
		return self.name

class Winery(models.Model):
	region = models.ForeignKey(Region, verbose_name = "Region",related_name = "wineries")
	name = models.CharField(max_length = 128, verbose_name = "Name")
	image = models.ImageField(upload_to="winery/", verbose_name ='Image',help_text = "350x400 recommend", null = True, blank = True)
	description = models.TextField(verbose_name = "Description",blank = True, null = True) 

	class Meta:
		verbose_name_plural = "Winery"
		verbose_name = "Winery"

	def __unicode__(self):
		return self.region.name+", "+self.name



class Product(models.Model):
	name = models.CharField(max_length = 128, verbose_name  ="Product Name")
	brand = models.ForeignKey(Brand,verbose_name = "Brand",related_name = "products")
	vintage = models.CharField(max_length = 128, verbose_name = 'Vintage', null = True, blank = True)
	image = models.ImageField(upload_to = "product/", verbose_name = "Product Image",help_text = 'Image height have to be 350px')
	attach = models.FileField(upload_to = "file/", verbose_name = "Attachment",blank = True, null = True)
	winery = models.ForeignKey(Winery, related_name = "products", null = True, blank = True)
	quantity = models.CharField(max_length = 128, verbose_name = 'Quantity', null = True, blank = True)
	description = models.TextField(verbose_name = "Description",blank = True, null = True)
	pub_date = models.DateTimeField(auto_now_add = True,verbose_name='Publish Date')
	last_modified = models.DateTimeField(auto_now = True,verbose_name='Last Modified Date')

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Product"

	def __unicode__(self):
		return self.name




