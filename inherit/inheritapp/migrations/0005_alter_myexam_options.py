# Generated by Django 4.0.3 on 2022-03-15 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inheritapp', '0004_examcenter_myexam'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myexam',
            options={'ordering': ['id']},
        ),
    ]
