# Generated by Django 2.2 on 2019-09-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades2', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rent',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
