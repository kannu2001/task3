from django.contrib import admin

from t3app.models import course

# Register your models here.
class courceAdmin(admin.ModelAdmin):
    list_display=['id','name','cat','loc','cdetail','cimage','is_active']
    list_filter=['cat','is_active']


admin.site.register(course,courceAdmin)