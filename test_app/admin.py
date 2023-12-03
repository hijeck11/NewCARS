from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Autohaus, AutoOptions

class CustomAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_auto', 'model_auto', 'engine_fuel', 'engine_volume')
    list_per_page = 5
    readonly_fields = ["preview", "links"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.auto_img.url}">')

    def links(self, obj):
        return mark_safe(f'<a href="{obj.link}">link<a>')


admin.site.register(Autohaus, CustomAdmin)


class CustomAdmin(admin.ModelAdmin):
    list_display = ('id', 'option_name', 'option_description')


admin.site.register(AutoOptions, CustomAdmin)