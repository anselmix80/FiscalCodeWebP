from django.contrib import admin
from api.models import Common
# Register your models here.

class CommonAdmin(admin.ModelAdmin):
    list_display = ('common_code', 'common_name')
    list_filter = ('common_name',)
    search_fields = ('common_code', 'common_name')

admin.site.register(Common, CommonAdmin)
