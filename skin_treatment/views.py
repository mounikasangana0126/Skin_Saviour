from django.shortcuts import render

from quiz.models import QuizModel
from skin_treatment.models.face_wash import FaceWashModel
from skin_treatment.models.serum import SerumModel
from skin_treatment.models.moisturizer import MoisturizerModel
from skin_treatment.models.sunscreen import SunscreenModel
from skin_treatment.models.natural_products_facewash import NaturalProductsFacewashModel
from skin_treatment.models.natural_products_serum import NaturalProductsSerumModel
from skin_treatment.models.natural_products_moisturizer import NaturalProductsMoisturizerModel
from skin_treatment.models.natural_products_scrub import NaturalProductsScrubModel
from skin_treatment.models.natural_products_facemask import NaturalProductsFacemaskModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def SkinTreatmentAPI(request):
       user=request.user
       if QuizModel.objects.filter(user=user):
            data = QuizModel.objects.filter(user=user).first()
            if data.treatment=='Conventional Products':
                  suggested_serum=''
                  if data.age=='25-40' or data.skin_concerns=='Wrinkles/Open pores':
                        suggested_serum = SerumModel.objects.filter(id=6)
                        data.age='< 25'
                  if data.skin_concerns== 'Sensitivity and redness' or data.react_to_new_products=='Gets irritated and red easily' or data.skin_type=='Sensitive':
                        data.skin_type='Sensitive'
                        data.skin_concerns='Sensitivity and redness'
                        data.react_to_new_products='Gets irritated and red easily'
                        data.skincare_texture='Gel'
                  elif data.skin_concerns=='Active Acne' or data.skin_concerns=="Oil Control":
                        data.skin_concerns='Oil Control'
                        data.react_to_new_products='Adapts Well'
                        data.skincare_texture='Gel'
                        data.skin_type='Oily'
                  elif data.skin_concerns=='Dry Patches'  or  data.react_to_new_products=='Breaks out' and data.skincare_texture=='Cream' or data.skin_concerns=='Wrinkles/Open pores':
                        data.skin_concerns='Dehydration/ Breakouts'
                        data.react_to_new_products='Adapts Well'
                        data.skin_type='Dry'
                        data.skincare_texture='Cream'
                  elif data.skin_concerns=='Acne Marks' or data.skin_concerns=='Hyper Pigmentation':
                        data.react_to_new_products='Adapts Well'
                        data.skincare_texture='Light Weight'
                        data.skin_type='Combination(Oily at T junction and Dry at cheeks)'
                        data.skin_concerns='Acne Marks'
                  if not suggested_serum:
                        suggested_serum = SerumModel.objects.filter(
                        treatment__treatment=data.treatment,
                        age__age=data.age,
                        skin_type__skin_type=data.skin_type,
                        skin_concern__skin_concern=data.skin_concerns,
                        react_to_new_products__react_to_new_products=data.react_to_new_products,
                        skincare_texture__skin_texture=data.skincare_texture,
                            )

                  suggested_facewash = FaceWashModel.objects.filter(
                    treatment__treatment=data.treatment,
                    age__age=data.age,
                    skin_type__skin_type=data.skin_type,
                    skin_concern__skin_concern=data.skin_concerns,
                    react_to_new_products__react_to_new_products=data.react_to_new_products,
                    skincare_texture__skin_texture=data.skincare_texture,
                        )
                  suggested_moisturizer = MoisturizerModel.objects.filter(
                    treatment__treatment=data.treatment,
                    age__age=data.age,
                    skin_type__skin_type=data.skin_type,
                    skin_concern__skin_concern=data.skin_concerns,
                    react_to_new_products__react_to_new_products=data.react_to_new_products,
                    skincare_texture__skin_texture=data.skincare_texture,
                        )
                  suggested_sunscreen = SunscreenModel.objects.filter(
                    treatment__treatment=data.treatment,
                    age__age=data.age,
                    skin_type__skin_type=data.skin_type,
                    skin_concern__skin_concern=data.skin_concerns,
                    react_to_new_products__react_to_new_products=data.react_to_new_products,
                    skincare_texture__skin_texture=data.skincare_texture,
                        )
                  if not (suggested_facewash and suggested_moisturizer and suggested_serum and suggested_sunscreen):
                        suggested_facewash=FaceWashModel.objects.filter(id='2')
                        suggested_moisturizer=MoisturizerModel.objects.filter(id='2')
                        suggested_serum=SerumModel.objects.filter(id='2')
                        suggested_sunscreen=SunscreenModel.objects.filter(id='2')
                        

                  return render(request, 'skin_treatment.html', {'suggested_facewash': suggested_facewash,'active_tab': 'skin_treatment', 'suggested_serum': suggested_serum, 'suggested_moisturizer': suggested_moisturizer, 'suggested_sunscreen': suggested_sunscreen, 'skin_type':data}) 
            elif data.treatment=='Natural Products':
                  facewash = NaturalProductsFacewashModel.objects.all()
                  serum = NaturalProductsSerumModel.objects.all()
                  moisturizer = NaturalProductsMoisturizerModel.objects.all()
                  scrub = NaturalProductsScrubModel.objects.all()
                  facemask = NaturalProductsFacemaskModel.objects.all()
                  return render(request, 'skin_treatment.html', {'facewash': facewash, 'serum':serum, 'moisturizer':moisturizer, 'scrub':scrub, 'facemask':facemask})
       return render(request, 'skin_treatment.html',{'active_tab': 'skin_treatment', 'message': 'PLEASE TAKE YOUR QUIZ TO GET YOUR TREATMENT'})  

