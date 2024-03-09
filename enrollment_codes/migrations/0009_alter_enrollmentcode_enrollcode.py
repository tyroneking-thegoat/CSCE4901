# Generated by Django 5.0.1 on 2024-03-09 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment_codes', '0008_alter_enrollmentcode_enrollcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollmentcode',
            name='EnrollCode',
            field=models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.'), django.core.validators.MaxLengthValidator(5)]),
        ),
    ]
