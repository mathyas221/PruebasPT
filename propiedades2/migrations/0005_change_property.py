# Generated by Django 2.2 on 2019-09-10 20:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades2', '0004_historicalacquisition_historicalrent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change_property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_property', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=20)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='propiedades2.Staff')),
            ],
        ),
    ]
