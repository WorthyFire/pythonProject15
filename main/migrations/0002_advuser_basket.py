# Generated by Django 4.2.8 on 2023-12-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advuser',
            name='basket',
            field=models.ManyToManyField(blank=True, related_name='basket', to='main.product'),
        ),
    ]
