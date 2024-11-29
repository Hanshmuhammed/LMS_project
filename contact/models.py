from django.db import models

class Contact(models.Model):  # Use PascalCase for the class name
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
