from django.db import models
from courses.models import Course

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"

