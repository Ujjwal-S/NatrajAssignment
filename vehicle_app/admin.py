from django.contrib import admin
from . models import Vehicle

# Admin Site Header
admin.site.site_header = "Natraj Packaging Admin"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'engine_status', 'date_added')
    list_filter = ('engine_status', 'date_added',)
