from django.db import models
from skin_treatment.models.treatment import TreatmentModel
from utils.helpers.image_file_path import facemask_image
from utils.helpers.timestamp_model import TimeStampedModel

class NaturalProductsFacemaskModel(TimeStampedModel):
    treatment = models.ForeignKey(TreatmentModel, on_delete=models.CASCADE)
    facemask1 = models.CharField(max_length=100)
    facemask1_image = models.ImageField(upload_to=facemask_image)
    facemask1_application = models.TextField()
    facemask1_benefits = models.TextField()
    facemask2 = models.CharField(max_length=100)
    facemask2_image = models.ImageField(upload_to=facemask_image)
    facemask2_application = models.TextField()
    facemask2_benefits = models.TextField()

    def __str__(self) -> str:
        return self.treatment.treatment
    
    class Meta:
        ordering = ['id']