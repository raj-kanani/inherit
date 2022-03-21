from django.contrib import admin
from .models import student, teacher, builder, exam, student1,\
        examcenter, myexam, Stu, Stu1, proxystudent


# Register your models here.
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'fees']


@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'salary']


@admin.register(builder)
class builderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'payment']

@admin.register(exam)
class examAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']

@admin.register(student1)
class student1Admin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city', 'name', 'roll']

@admin.register(myexam)
class myexamAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


@admin.register(examcenter)
class examcenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']

@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']


@admin.register(Stu1)
class StuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']


@admin.register(proxystudent)
class proxystudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']