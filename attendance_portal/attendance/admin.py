from django.contrib import admin
from .models import Course, Enrollment, Lecture, Attendance

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lecture)
admin.site.register(Attendance)