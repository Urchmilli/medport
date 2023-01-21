from django.db import models

# Create your models here.
class AdmissionForm(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    residential_address = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50)
    date_admitted = models.DateField()
    ward = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    patient_id = models.IntegerField()
    symptoms = models.TextField()
    
    

    def __str__(self):
        return self.first_name
