# Generated by Django 2.0.6 on 2018-07-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='detail',
            field=models.TextField(blank=True, default='', max_length=23000, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='source_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
