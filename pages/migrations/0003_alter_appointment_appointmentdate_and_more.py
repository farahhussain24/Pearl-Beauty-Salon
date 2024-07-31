# Generated by Django 4.1.4 on 2023-01-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_appointment_alter_stylist_bookeddates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentdate',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='package',
            field=models.CharField(default='Barat Makeup', max_length=25),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='stylistname',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='bookeddates',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]