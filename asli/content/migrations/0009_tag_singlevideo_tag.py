# Generated by Django 4.2.1 on 2023-07-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_singlevideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='singlevideo',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='content.tag'),
        ),
    ]
