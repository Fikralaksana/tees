# Generated by Django 3.2.8 on 2021-11-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211102_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembeli',
            name='address',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pembeli',
            name='phone',
            field=models.CharField(max_length=16, null=True),
        ),
    ]