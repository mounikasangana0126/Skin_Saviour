from django.shortcuts import render
# Create your views here.

def TipsAPI(request):
    return render(request, 'tips.html',{'active_tab': 'tips'})