from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False,unique=True)
    
    profile_image = models.ImageField(
        upload_to='profile_images/', 
        blank=True, 
        null=True, 
        default='profile_images/default.png'
    )


    REQUIRED_FIELDS = ["email", "first_name", "last_name"]







 


    