import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Description(models.Model):
    description_text=models.CharField(max_length=10)
    pub_date=models.DateTimeField('date asked')
    pred_text= models.CharField(max_length=12, default='Null')
    def __str__(self):
        return self.description_text
    def was_sent_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
