# Generated by Django 4.0.4 on 2022-05-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passangers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
