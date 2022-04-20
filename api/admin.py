from django.contrib import admin
from .models import Attraction, AttractionType, ParkLocation

class AttractionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Attraction, AttractionAdmin)


class AttractionTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(AttractionType, AttractionTypeAdmin)


class ParkLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(ParkLocation, ParkLocationAdmin)