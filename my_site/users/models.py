from django.db import models
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="avatarka/")
    instagram = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(default=datetime.date.today())  #input_formats=['%d/%m/%Y'],
    def __str__(self):
        return str(self.user)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#
#     def __str__(self):
#         return f'{self.user.username} Profile'


