from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
import random


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=4, blank=True, unique=True)
    is_confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = self.generate_confiramtion_code()
        super(Profile, self).save(*args, **kwargs)

    def generate_confiramtion_code(self):
        return str(random.randint(1000, 9999))
    
    def __str__(self) -> str:
        return self.user.username