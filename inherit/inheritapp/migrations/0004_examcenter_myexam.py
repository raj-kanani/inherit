# Generated by Django 4.0.3 on 2022-03-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritapp', '0003_exam_student1'),
    ]

    operations = [
        migrations.CreateModel(
            name='examcenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='myexam',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('inheritapp.examcenter',),
        ),
    ]
