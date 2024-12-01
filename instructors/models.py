from django.db import models
from user.models import User

class InstructorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'},  # Only allow users with the 'teacher' role
    )
    photo = models.ImageField(upload_to='instructors/', blank=True, null=True)
    qualifications = models.TextField()

    def __str__(self):
        return self.user.username

    
   

