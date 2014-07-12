from django.contrib import admin
from partner.models import Partner
# Register your models here.
class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name', 'link')

admin.site.register(Partner,PartnerAdmin)