from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Page(MPTTModel):
	title = models.CharField(max_length = 128, verbose_name = "Page Title")
	s_title = models.CharField(max_length = 128, verbose_name = "Page Second Title", blank = True, null = True)
	parent = TreeForeignKey('self', verbose_name = "Parent Page", blank = True, null = True)
	banner = models.ImageField(upload_to = "banner/",verbose_name = "Page Fix Picture", help_text = "1020x300 recommend", blank = True, null = True)
	url_parameter = models.CharField(max_length = 256, verbose_name = "URL", help_text = "Auto generate based on page title")
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
		