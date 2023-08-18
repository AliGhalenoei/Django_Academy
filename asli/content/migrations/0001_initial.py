# Generated by Django 4.2.1 on 2023-07-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images/')),
                ('teacher', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('full', 'تکمیل'), ('imperfect', 'درحال ظبط')], default='full', max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
