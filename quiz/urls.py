from django.urls import path
from .views import save_data

urlpatterns = [
    path('save_data/', save_data, name='save_data'),
]
