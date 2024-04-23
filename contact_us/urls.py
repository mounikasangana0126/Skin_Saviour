from django.urls import path
from .views import ContactUSData

urlpatterns = [
    path('save_form_data/', ContactUSData, name='save_form_data'),
]
