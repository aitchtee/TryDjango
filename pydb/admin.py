from django.contrib import admin
from .models import Style
from .models import Crew
from .models import Dancer

# Register your models here.


class StyleModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'style_name']
    list_display_links = ['id', 'style_name']
    ordering = ['id']

    class Meta:
        model = Style


class CrewModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'crew_name']
    list_display_links = ['id', 'crew_name']
    ordering = ['id']

    class Meta:
        model = Crew


class DancerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'crew_id', 'style_id', 'dancer_name']
    list_display_links = ['id', 'crew_id', 'style_id', 'dancer_name']
    ordering = ['id']

    class Meta:
        model = Dancer


admin.site.register(Style, StyleModelAdmin)
admin.site.register(Crew, CrewModelAdmin)
admin.site.register(Dancer, DancerModelAdmin)
