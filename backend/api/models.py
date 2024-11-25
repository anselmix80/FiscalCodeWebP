from django.db import models

# Create your models here.
class Common(models.Model):
    common_name = models.CharField(max_length=60)
    common_code = models.CharField(max_length=4, primary_key=True)

    def __str__(self):
        return self.common_name
