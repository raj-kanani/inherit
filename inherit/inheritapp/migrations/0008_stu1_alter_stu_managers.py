# Generated by Django 4.0.3 on 2022-03-16 05:19

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('inheritapp', '0007_stu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stu1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField()),
            ],
            managers=[
                ('stud', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='stu',
            managers=[
                ('Students', django.db.models.manager.Manager()),
            ],
        ),
    ]
