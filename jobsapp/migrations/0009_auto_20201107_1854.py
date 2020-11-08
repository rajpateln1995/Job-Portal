# Generated by Django 3.0.7 on 2020-11-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0008_auto_20200810_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_description',
        ),
        migrations.RemoveField(
            model_name='job',
            name='type',
        ),
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('1', 'Plumbing'), ('2', 'Carpentry'), ('3', 'Masonary'), ('4', 'Electrical Repair')], max_length=10),
        ),
    ]
