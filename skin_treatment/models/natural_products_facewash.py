from django.db import models
from skin_treatment.models.treatment import TreatmentModel
from utils.helpers.image_file_path import facewash_image
from utils.helpers.timestamp_model import TimeStampedModel

class NaturalProductsFacewashModel(TimeStampedModel):
    disclaimer = models.TextField()
    treatment = models.ForeignKey(TreatmentModel, on_delete=models.CASCADE)
    facewash1 = models.CharField(max_length=100)
    facewash1_image = models.ImageField(upload_to=facewash_image)
    facewash1_application = models.TextField()
    facewash1_benefits = models.TextField()
    facewash2 = models.CharField(max_length=100)
    facewash2_image = models.ImageField(upload_to=facewash_image)
    facewash2_application = models.TextField()
    facewash2_benefits = models.TextField()

    def __str__(self) -> str:
        return self.treatment.treatment
    
    class Meta:
        ordering = ['id']