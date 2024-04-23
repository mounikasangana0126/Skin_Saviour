from django.shortcuts import render
# Create your views here.

def AboutAPI(request):
    return render(request, 'about.html',{'active_tab': 'about'})