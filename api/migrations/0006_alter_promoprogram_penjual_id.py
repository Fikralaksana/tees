# Generated by Django 3.2.8 on 2021-11-07 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_promoprogram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promoprogram',
            name='penjual_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promo', to='api.penjual'),
        ),
    ]
