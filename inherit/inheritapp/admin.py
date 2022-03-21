from django.contrib import admin
from .models import Student, Teacher, Builder, Exam, Student1, Examcenter, Myexam, Stu, Stu1, Proxystudent


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'fees']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'salary']


@admin.register(Builder)
class BuilderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'payment']


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


@admin.register(Student1)
class Student1Admin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city', 'name', 'roll']


@admin.register(Myexam)
class MyexamAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


@admin.register(Examcenter)
class ExamcenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']


@admin.register(Stu1)
class StuAdmin1(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']


@admin.register(Proxystudent)
class ProxystudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']
