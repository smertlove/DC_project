# Generated by Django 4.2.2 on 2023-06-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_image_profile_bio_profile_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='avatarka/'),
        ),
    ]
