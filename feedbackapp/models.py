from django.db import models

class FeedbackData(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True )
    feedback = models.CharField(max_length=100)
