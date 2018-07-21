# Generated by Django 2.0.6 on 2018-07-21 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20180721_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_details',
            name='contact_form',
            field=models.CharField(choices=[('email', 'Email'), ('facebook', 'Facebook'), ('twitter', 'Twitter'), ('instagram', 'Instagram'), ('reddit', 'Reddit')], default='email', max_length=20),
        ),
        migrations.AlterField(
            model_name='queue',
            name='guest',
            field=models.CharField(max_length=200),
        ),
    ]
