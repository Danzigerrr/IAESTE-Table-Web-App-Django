# Generated by Django 4.1.1 on 2022-09-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iaesteTable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='Deadline',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='offer',
            name='From',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='offer',
            name='To',
            field=models.CharField(default='', max_length=100),
        ),
    ]