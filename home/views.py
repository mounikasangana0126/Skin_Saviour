from django.shortcuts import render
# Create your views here.

def HomeAPI(request):
    return render(request, 'home.html',{'active_tab': 'home'})
