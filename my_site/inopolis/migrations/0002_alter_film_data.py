# Generated by Django 4.2.2 on 2023-07-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inopolis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='data',
            field=models.ImageField(upload_to=''),
        ),
    ]
