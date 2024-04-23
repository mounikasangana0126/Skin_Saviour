import time
from django.db import IntegrityError
from django.shortcuts import render,redirect
from rest_framework import status
from quiz.models import QuizModel
from skin_treatment.models.face_wash import FaceWashModel
from skin_treatment.models.treatment import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def QuizAPI(request):
    user=request.user
    data = QuizModel.objects.filter(user=user)
    if data:
        data = QuizModel.objects.get(user=user)
        context={
            "user":data.user,
            "treatment":data.treatment,
            "age":data.age,
            "skin_type":data.skin_type,
            "skin_concerns":data.skin_concerns,
            "react_to_new_products":data.react_to_new_products,
            "sleep_cycle":data.sleep_cycle,
            "skincare_texture":data.skincare_texture,
        }
        return render(request, 'quiz.html',{"context":context,'active_tab': 'quiz',})

    return render(request, 'quiz.html',{'active_tab': 'quiz'})

def save_data(request):
    suggested_facewash = None
    if request.method == 'POST':
        user = request.user
        treatment = request.POST.get('treatment')
        age = request.POST.get('age')
        skin_type = request.POST.get('skin_type')
        skin_concerns = ','.join(request.POST.getlist('skin_concerns'))
        react_to_new_products = request.POST.get('react_to_new_products')
        sleep_cycle = request.POST.get('sleep_cycle')
        skincare_texture = request.POST.get('skincare_texture')
        
        data=QuizModel.objects.filter(user=user)
        if not data:
            quiz_data= QuizModel(
                user=user,
                treatment=treatment,
                age=age,
                skin_type=skin_type,
                skin_concerns=skin_concerns,
                react_to_new_products=react_to_new_products,
                sleep_cycle=sleep_cycle,
                skincare_texture=skincare_texture
            )
            quiz_data.save()
        elif data.exists:
            # Update the existing data
            data.update(
            treatment=treatment,
            age=age,
            skin_type=skin_type,
            skin_concerns=skin_concerns,
            react_to_new_products=react_to_new_products,
            sleep_cycle=sleep_cycle,
            skincare_texture=skincare_texture
        )

        time.sleep(3)
        return redirect('quiz')
        

    return render(request, 'quiz.html',{'active_tab': 'quiz'})
