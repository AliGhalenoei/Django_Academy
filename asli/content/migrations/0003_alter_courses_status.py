# Generated by Django 4.2.1 on 2023-07-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_courses_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='status',
            field=models.CharField(choices=[('تکمیل', 'تکمیل'), ('imperfect', 'درحال ظبط')], default='تکمیل', max_length=20, verbose_name='وضعیت دوره'),
        ),
    ]
