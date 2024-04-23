"""
URL configuration for SkinSaviour project.

"""
from django.contrib import admin
from django.urls import path, include
from home.views import HomeAPI
from about.views import AboutAPI
from quiz.views import QuizAPI, save_data
from contact_us.views import ContactUsAPI
from skin_treatment.views import SkinTreatmentAPI
from tips.views import TipsAPI
from core.views import LoginAPI,Logout,SignUp
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header='Skin-Saviour Admin'
admin.site.index_title='Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), 'core')),
    path('home/',HomeAPI,name="home"),
    path('about/',AboutAPI,name="about"),
    path('quiz/',QuizAPI,name="quiz"),
    path('', include('quiz.urls')),
    path('contact_us/',ContactUsAPI,name="contact_us"),
    path('',include('contact_us.urls')),
    path('skin_treatment/',SkinTreatmentAPI,name="skin_treatment"),
    path('tips/',TipsAPI,name="tips"),
    path('login/',LoginAPI,name="login"),
    path('signup/',SignUp,name="signup"),
    path('logout/',Logout,name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
