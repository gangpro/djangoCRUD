# Generated by Django 2.2.2 on 2019-06-13 07:49

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='boards/images'),
        ),
    ]