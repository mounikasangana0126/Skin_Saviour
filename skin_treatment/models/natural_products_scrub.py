from django.db import models
from skin_treatment.models.treatment import TreatmentModel
from utils.helpers.image_file_path import scrub_image
from utils.helpers.timestamp_model import TimeStampedModel

class NaturalProductsScrubModel(TimeStampedModel):
    treatment = models.ForeignKey(TreatmentModel, on_delete=models.CASCADE)
    scrub1 = models.CharField(max_length=100)
    scrub1_preperation = models.TextField()
    scrub1_image = models.ImageField(upload_to=scrub_image)
    scrub1_application = models.TextField()
    scrub1_benefits = models.TextField()
    scrub2 = models.CharField(max_length=100)
    scrub2_preperation = models.TextField()
    scrub2_image = models.ImageField(upload_to=scrub_image)
    scrub2_application = models.TextField()
    scrub2_benefits = models.TextField()

    def __str__(self) -> str:
        return self.treatment.treatment
    
    class Meta:
        ordering = ['id']