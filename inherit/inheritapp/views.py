from django.shortcuts import render
from .models import student, teacher, builder, student1, exam, myexam, examcenter, Stu, Stu1, proxystudent


# Create your views here.

def home(request):
    s = student.objects.all()
    t = teacher.objects.all()
    b = builder.objects.all()
    s1 = student1.objects.all()
    e = exam.objects.all()
    me = myexam.objects.all()
    ec = examcenter.objects.all()
    stu = Stu.Students.all()
    # stu1 = Stu1.stud.all()
    # stu1 = Stu1.stud.get_stu_roll_range(0, 101)
    stu1 = proxystudent.stud.get_stu_roll_range(101, 105)
    return render(request, 'home.html', {'s': s, 't': t, 'b': b,
                                         's1': s1, 'e': e, 'me': me, 'ec': ec,
                                         'stu': stu, 'stu1': stu1, })
