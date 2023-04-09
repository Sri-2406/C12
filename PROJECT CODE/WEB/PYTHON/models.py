
# Create your models here.
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class UserPredictDataModel(models.Model):

    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    hypertension = models.CharField(max_length=100)
    heart_disease = models.CharField(max_length=100)
    avg_glucose_level = models.CharField(max_length=100)
    bmi = models.CharField(max_length=100)
    smoking_status = models.CharField(max_length=100)
    stroke = models.CharField(max_length=100)
    

def __str__(self):
    return self.gender, self.age,self.hypertension, self.heart_disease,self.avg_glucose_level,self.bmi,self.smoking_status,self.stroke

class FeedModel(models.Model):
    Feedback = models.TextField(max_length=100)

    def __str__(self):
        return str(self.Feedback)
