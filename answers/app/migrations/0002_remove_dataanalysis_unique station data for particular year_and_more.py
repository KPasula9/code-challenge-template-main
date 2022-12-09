# Generated by Django 4.1.3 on 2022-12-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='dataanalysis',
            name='unique station data for particular year',
        ),
        migrations.RemoveConstraint(
            model_name='weather',
            name='unique station data for particular day',
        ),
        migrations.AlterField(
            model_name='corn_grain_yield',
            name='corn_yield',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='corn_grain_yield',
            name='year',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='dataanalysis',
            name='max_temp_avg',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dataanalysis',
            name='min_temp_avg',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dataanalysis',
            name='station_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='dataanalysis',
            name='total_precipitation',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dataanalysis',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='max_temp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='min_temp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='precipitation',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='station_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AddConstraint(
            model_name='dataanalysis',
            constraint=models.UniqueConstraint(fields=('station_id', 'year'), name='unique_station_year'),
        ),
        migrations.AddConstraint(
            model_name='weather',
            constraint=models.UniqueConstraint(fields=('station_id', 'date'), name='unique_station_day'),
        ),
    ]
