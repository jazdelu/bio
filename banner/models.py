from django.db import models

# Create your models here.
class Banner(models.Model):
	image = models.ImageField(upload_to = 'home/',verbose_name = "Image")
	weight = models.IntegerField(verbose_name = "Weight", help_text = "Matters the order of homepage sliders")

	class Meta:
		verbose_name = "Banner"
		verbose_name_plural = "Banner"
		ordering = ["-weight",]

	def __unicode__(self):
		return self.image.url