from django.contrib import admin

# Register your models here.
from .models import Guru, Course, Student

class StudentInline(admin.StackedInline):
    model = Student.scourses.through
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("scourses",)

admin.site.register(Guru)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)