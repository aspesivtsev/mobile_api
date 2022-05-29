from django.contrib import admin
from .models import Attraction, AttractionType, ParkLocation

class AttractionAdmin(admin.ModelAdmin):
    list_display = ['title',  'is_active', 'is_working', 'sorting', 'wait_time', 'work_time']
    list_editable = ['is_active', 'is_working', 'sorting', 'wait_time', 'work_time']
    list_filter = ['location']  # left filters in admin page
    search_fields = ['title', ]
    list_per_page = 50
    #prepopulated_fields = {'slug': ('title',)}
admin.site.register(Attraction, AttractionAdmin)


class AttractionTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(AttractionType, AttractionTypeAdmin)


class ParkLocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(ParkLocation, ParkLocationAdmin)