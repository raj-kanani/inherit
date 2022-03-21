from django.shortcuts import render
from .models import Student, Teacher, Builder, Student1, Exam, Myexam, Examcenter, Stu, Proxystudent


# Create your views here.

def home(request):
    s = Student.objects.all()
    t = Teacher.objects.all()
    b = Builder.objects.all()
    s1 = Student1.objects.all()
    e = Exam.objects.all()
    me = Myexam.objects.all()
    ec = Examcenter.objects.all()
    stu = Stu.Students.all()
    '''stu1 = Stu1.stud.all()'''
    '''stu1 = Stu1.stud.get_stu_roll_range(0, 101)'''
    stu1 = Proxystudent.stud.get_stu_roll_range(101, 105)
    return render(request, 'home.html', {'s': s, 't': t, 'b': b,
                                         's1': s1, 'e': e, 'me': me, 'ec': ec,
                                         'stu': stu, 'stu1': stu1, })
