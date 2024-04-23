from django.db import models
from utils.helpers.timestamp_model import TimeStampedModel

class TreatmentModel(TimeStampedModel):
    treatment = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.treatment
    
    class Meta:
        ordering = ['id']

class SkinTypeModel(TimeStampedModel):
    skin_type = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.skin_type
    
    class Meta:
        ordering = ['id']
    
class AgeModel(TimeStampedModel):
    age = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.age
    
    class Meta:
        ordering = ['id']

class SkinConernModel(TimeStampedModel):
    skin_concern = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.skin_concern
    
    class Meta:
        ordering = ['id']
    
class ReactToNewProductsModel(TimeStampedModel):
    react_to_new_products = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.react_to_new_products
    
    class Meta:
        ordering = ['id']
        

class SleepCycleModel(TimeStampedModel):
    sleep_cycle = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.sleep_cycle
    
    class Meta:
        ordering = ['id']

class SkinCareTextureModel(TimeStampedModel):
    skin_texture = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.skin_texture
    
    class Meta:
        ordering = ['id']