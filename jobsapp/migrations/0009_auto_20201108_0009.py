# Generated by Django 3.0.7 on 2020-11-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0008_auto_20200810_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=100),
        ),
    ]