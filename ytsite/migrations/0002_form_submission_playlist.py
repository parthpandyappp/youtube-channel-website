# Generated by Django 3.0.6 on 2020-06-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ytsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_submission',
            name='playlist',
            field=models.CharField(default='comp_tech', max_length=100),
        ),
    ]
