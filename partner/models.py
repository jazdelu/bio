from django.db import models

# Create your models here.
class Partner(models.Model):
	name = models.CharField(max_length = 128, verbose_name = 'Name')
	image = models.ImageField(upload_to = 'partner/',verbose_name = 'Image')
	link = models.URLField(verbose_name = "Link")

	class Meta:
		verbose_name_plural = "Partner"
		verbose_name = "Partner"

	def __unicode__(self):
		return self.name