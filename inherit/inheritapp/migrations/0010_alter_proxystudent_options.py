# Generated by Django 4.0.3 on 2022-03-16 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inheritapp', '0009_proxystudent_alter_stu1_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proxystudent',
            options={'ordering': ['-name']},
        ),
    ]
