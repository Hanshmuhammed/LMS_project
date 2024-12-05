from django.db import models

# Create your models here.
class core(models.Model):
    hey=models.CharField(max_length=50)


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    testimonial_text = models.TextField()

    def __str__(self):
        return self.client_name
