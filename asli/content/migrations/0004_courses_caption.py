# Generated by Django 4.2.1 on 2023-07-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_courses_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
