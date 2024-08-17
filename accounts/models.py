from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False)
    is_confirmed = models.BooleanField(default=False)

    
    def __str__(self) -> str:
        return self.user.username