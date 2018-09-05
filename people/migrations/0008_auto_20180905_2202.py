# Generated by Django 2.0.6 on 2018-09-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20180722_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_details',
            name='contact_form',
            field=models.CharField(choices=[('email', 'Email'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('twitter', 'Twitter'), ('facebook', 'Facebook'), ('reddit', 'Reddit')], default='email', max_length=20),
        ),
        migrations.AlterField(
            model_name='interview',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='work_description',
            field=models.TextField(max_length=100),
        ),
    ]