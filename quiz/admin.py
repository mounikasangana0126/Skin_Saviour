from django.contrib import admin
from .models import QuizModel
# Register your models here.
@admin.register(QuizModel)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'treatment', 'skin_type', 'skincare_texture']
    list_filter = ['treatment', 'skin_type',]
    search_fields = ['skin_type']
    list_per_page = 10
