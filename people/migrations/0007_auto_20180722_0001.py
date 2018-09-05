# Generated by Django 2.0.6 on 2018-07-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20180721_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='queue',
            name='guest_contact',
            field=models.ManyToManyField(blank=True, related_name='guest_queue', to='people.contact_details'),
        ),
    ]