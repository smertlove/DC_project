# Generated by Django 4.2.2 on 2023-07-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inopolis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='film',
            name='data',
            field=models.ImageField(upload_to=''),
        ),
    ]
