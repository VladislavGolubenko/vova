# Generated by Django 4.0.4 on 2022-06-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='amount_commission',
        ),
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(verbose_name='Цена на момент покупки'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_start',
            field=models.DateField(verbose_name='Дата начала'),
        ),
    ]
