from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264, blank=True)
    last_name = models.CharField(max_length=264, blank=True)
    email = models.EmailField(max_length=24,blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
