from django.contrib import admin
from weather.models import Icon_Weather

# Register your models here.
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('image_code', 'image_url')
    list_filter = ('image_code',)
    search_fields = ('image_code', 'image_url')

admin.site.register(Icon_Weather, WeatherAdmin)
