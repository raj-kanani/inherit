from django.db import models


class Custommanager(models.Manager):
    # we use custom method name

    def get_stu_roll_range(self, r1, r2):
        return super().get_queryset().filter(roll__range=(r1, r2))


'''default get_queryset..'''
# def get_queryset(self):
#     return super().get_queryset().order_by('name')
