# Generated by Django 5.0.4 on 2024-05-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conytactdb',
            name='Messege',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
