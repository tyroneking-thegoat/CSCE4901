# Generated by Django 5.0.3 on 2024-03-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='img',
            field=models.FileField(default='placeholderPreview.jpg', upload_to='pic/%y/'),
        ),
    ]
