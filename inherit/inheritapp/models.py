from django.db import models
from .managers import Custommanager

# Create your models here.
'''model inheritance  with abstract based class..'''


class Commonfield(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=False)
    date = models.DateField()

    class Meta:
        abstract = True


class Student(Commonfield):
    fees = models.IntegerField()
    date = None  # student ne date no joti hoy to....


class Teacher(Commonfield):
    salary = models.IntegerField()


class Builder(Commonfield):
    date = models.DateTimeField()
    payment = models.IntegerField()


''' multiple inheritance..... and one-to-one relationship.'''


class Exam(models.Model):
    cname = models.CharField(max_length=50)
    city = models.CharField(max_length=80)

    def __str__(self):
        return self.cname


class Student1(Exam):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()

    def __str__(self):
        return self.name


'''proxy models (1 model mathi data delete kri to bey ma thy)..'''


class Examcenter(models.Model):
    cname = models.CharField(max_length=50)
    city = models.CharField(max_length=80)

    def __str__(self):
        return self.cname


class Myexam(Examcenter):
    class Meta:
        proxy = True
        ordering = ['city']


'''model manager...'''


class Stu(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    ''' this name pass replace to Stu.objects.all in view.. '''
    '''Stu.Students.all()'''
    Students = models.Manager()


# custom manager..
class Stu1(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    '''stud = custommanager()'''


class Proxystudent(Stu1):
    stud = Custommanager()

    class Meta:
        proxy = True
        ordering = ['-name']
