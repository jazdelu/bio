from django.contrib.sitemaps import Sitemap
from brand.models import Brand

class BrandSitemap(Sitemap):
	changefreq = 'monthly'
	priority = 0.5

	def items(self):
		return Brand.objects.all()

	def location(self,obj):
		return '/brand/%s/' % obj.title