# Generated by Django 3.2.5 on 2021-11-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='C:\\Django-blog\\django-blog\\projects\\static\\img'),
        ),
    ]