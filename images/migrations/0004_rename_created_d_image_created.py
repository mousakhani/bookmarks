# Generated by Django 3.2.6 on 2021-08-30 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_rename_created_image_created_d'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='created_d',
            new_name='created',
        ),
    ]
