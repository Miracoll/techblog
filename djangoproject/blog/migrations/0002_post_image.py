# Generated by Django 4.1 on 2022-09-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='tech_blog_01.jpg', null=True, upload_to='post'),
        ),
    ]
