from django.db import models
from skin_treatment.models.treatment import TreatmentModel
from utils.helpers.image_file_path import moisturizer_image
from utils.helpers.timestamp_model import TimeStampedModel

class NaturalProductsMoisturizerModel(TimeStampedModel):
    treatment = models.ForeignKey(TreatmentModel, on_delete=models.CASCADE)
    moisturizer1 = models.CharField(max_length=100)
    moisturizer1_image = models.ImageField(upload_to=moisturizer_image)
    moisturizer1_application = models.TextField()
    moisturizer1_benefits = models.TextField()
    moisturizer2 = models.CharField(max_length=100)
    moisturizer2_image = models.ImageField(upload_to=moisturizer_image)
    moisturizer2_application = models.TextField()
    moisturizer2_benefits = models.TextField()

    def __str__(self) -> str:
        return self.treatment.treatment
    
    class Meta:
        ordering = ['id']