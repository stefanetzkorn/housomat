# Generated by Django 4.0 on 2022-06-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempreading',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
