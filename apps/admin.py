from django.contrib import admin
from .models import Kitob, Vazifa

# Register your models here.
admin.site.register(Vazifa)

class CustomKitob(admin.ModelAdmin):
    list_display = ('nomi', 'muallifi', 'yili', 'janri', 'rasmi')
    list_filter = ('muallifi', 'janri')
    search_fields = ('nomi', 'muallifi')
    date_hierarchy = 'yili'

admin.site.register(Kitob, CustomKitob)
