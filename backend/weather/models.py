from django.db import models

# Create your models here.
class Icon_Weather(models.Model):
    image_code = models.CharField(max_length=10, primary_key=True)
    image_url = models.CharField(max_length=20)

    def __str__(self):
        return self.image_url