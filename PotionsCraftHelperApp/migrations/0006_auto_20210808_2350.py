# Generated by Django 3.2.5 on 2021-08-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PotionsCraftHelperApp', '0005_alter_potion_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='potion',
            name='time_plus',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='potion',
            name='ingredients',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='potion',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='potion',
            name='time',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
