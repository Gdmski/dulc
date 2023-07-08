from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, date

# Create your models here.

class Dulcinea(models.Model):
      date_1 = models.DateField()
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      desc = models.TextField(max_length=500)
      RS_rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default='10')
      GM_rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],default='10')
      event_image = models.ImageField(null=True, blank=True,  upload_to='images/')

      class Meta:
            ordering = ['date_1']
            
      

      def __str__(self):
            return str(self.user) + ' | ' + str(self.date_1)

      def get_absolute_url(self):
            return reverse('event-detail', args=[str(self.id)])
            
