# Generated by Django 4.0.4 on 2022-05-29 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0019_remove_filter_temperature_x1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='X1',
            field=models.CharField(blank=True, help_text='Please use 12-hour clock if Window is selected', max_length=200, null=True, verbose_name='value to set(X1)'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='X2',
            field=models.CharField(blank=True, help_text='X2 should be greater than X1', max_length=200, null=True, verbose_name='value to set(X2)'),
        ),
    ]
