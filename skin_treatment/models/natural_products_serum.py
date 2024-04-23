from django.db import models
from skin_treatment.models.treatment import TreatmentModel
from utils.helpers.image_file_path import serum_image
from utils.helpers.timestamp_model import TimeStampedModel

class NaturalProductsSerumModel(TimeStampedModel):
    treatment = models.ForeignKey(TreatmentModel, on_delete=models.CASCADE)
    serum1 = models.CharField(max_length=100)
    serum1_image = models.ImageField(upload_to=serum_image)
    serum1_application = models.TextField()
    serum1_benefits = models.TextField()
    serum2 = models.CharField(max_length=100)
    serum2_image = models.ImageField(upload_to=serum_image)
    serum2_application = models.TextField()
    serum2_benefits = models.TextField()

    def __str__(self) -> str:
        return self.treatment.treatment
    
    class Meta:
        ordering = ['id']