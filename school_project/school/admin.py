from django.contrib import admin
from school.models import Teacher, Student, Class
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
