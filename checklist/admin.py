from django.contrib import admin
from .models import CheckList

# Register your models here.
class CheckListAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'completed','created_on')
    list_filter = ("status",)
    search_fields = ['title',]
  
admin.site.register(CheckList, CheckListAdmin)