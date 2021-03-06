# Generated by Django 4.0.4 on 2022-05-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_about_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(default='When in doubt… I find retracing my steps to be a wise place to begin. — Albus Dumbledore', verbose_name='About me'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='users/photos', verbose_name='Photo'),
        ),
    ]
