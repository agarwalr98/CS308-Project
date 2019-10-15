from django.db import models
from accounts.models import User
import datetime as Datetime
from datetime import datetime
from django.core.validators import MinValueValidator
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    teacher = models.ForeignKey(User, related_name='courses', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE, null=False)
    student = models.ForeignKey(User, related_name='enrollments', on_delete=models.CASCADE, null=False)

class Lecture(models.Model):
    course = models.ForeignKey(Course, related_name='lectures', on_delete=models.CASCADE, null=False)
    time = models.DateTimeField(null=True)
    duration = models.DurationField(default=Datetime.timedelta(days=0, hours=1),
                validators=[MinValueValidator(Datetime.timedelta(days=0, hours=0, minutes=30))])
    class_no = models.IntegerField()

class Attendance(models.Model):
    student = models.ForeignKey(User, related_name='attendances', on_delete=models.CASCADE, null=False)
    lecture = models.ForeignKey(Lecture, related_name='attendances', on_delete=models.CASCADE, null=False)