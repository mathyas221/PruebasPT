# Generated by Django 2.2 on 2019-12-12 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades2', '0025_auto_20191211_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedades2.Region'),
        ),
    ]