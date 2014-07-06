from django.db import models
# Create your models here.
class Page(models.Model):
	title = models.CharField(max_length = 128, verbose_name = "Page Title")
	s_title = models.CharField(max_length = 128, verbose_name = "Page Second Title", blank = True, null = True)
	banner = models.ImageField(upload_to = "banner/",verbose_name = "Page Fix Picture", help_text = "780x230 recommend", blank = True, null = True)
	pub_date = models.DateTimeField(auto_now_add = True,verbose_name='Publish Date')
	last_modified = models.DateTimeField(auto_now = True,verbose_name='Last Modified Date')

	class Meta:
		verbose_name = "Page"
		verbose_name_plural = "Page"
		ordering = ['pub_date','last_modified']

	def __unicode__(self):
		return self.title

class Section(models.Model):
	title = models.CharField(max_length = 128, verbose_name = "Section Title")
	content = models.TextField(verbose_name = "Section Content")
	page = models.ForeignKey(Page,related_name = "sections")

	class Meta:
		verbose_name = "Section"
		verbose_name_plural = "Section"

	def __unicode__(self):
		return self.title

class Image(models.Model):
	title = models.CharField(max_length = 128,verbose_name = "Title",blank = True, null = True)
	image = models.ImageField(upload_to = "page/",verbose_name = "Image")
	page = models.ForeignKey(Page,related_name = "images")
	link = models.URLField(verbose_name = "Link",blank = True, null = True)

	def __unicode__(self):
		return self.image.url
		