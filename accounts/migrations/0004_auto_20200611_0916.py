# Generated by Django 3.0.7 on 2020-06-11 09:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200611_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=15, region=None),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='surname',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='patient',
            name='day_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=15, region=None),
        ),
        migrations.AlterField(
            model_name='patient',
            name='street',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='patient',
            name='surname',
            field=models.CharField(max_length=80),
        ),
    ]
