from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=200)
# Esta línea especifica que el campo de correo electrónico se utilizará como el campo de nombre de usuario principal
# para la autenticación.
    USERNAME_FIELD = "email"
# Le dice a django que username va a ser obligatorio al crear el usuario
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username