from django.contrib import admin
from .models import ContactUSModel
# Register your models here.

@admin.register(ContactUSModel)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'rating', 'feedback']
    list_filter = ['rating']
    search_fields = ['user']
    list_per_page = 10