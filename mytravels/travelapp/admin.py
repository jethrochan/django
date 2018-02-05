from django.contrib import admin
from . models import *

# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    list_display = ["city"]
    search_fields = ["city"]
        
class ReportAdmin(admin.ModelAdmin):
    list_display = ["destination"]
    search_fields = ["destination"]     
            
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Report, ReportAdmin)