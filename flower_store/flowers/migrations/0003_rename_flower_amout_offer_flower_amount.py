# Generated by Django 4.2.1 on 2023-05-10 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='flower_amout',
            new_name='flower_amount',
        ),
    ]
