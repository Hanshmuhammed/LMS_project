from django.db import models
from courses.models import Course
from user.models import User

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.course.title}"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    submission_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='assignments/')

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"

