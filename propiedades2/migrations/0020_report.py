# Generated by Django 2.2 on 2019-11-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades2', '0019_remove_rent_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='Reportes/')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
