# Generated by Django 2.2.6 on 2019-11-13 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20191110_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
    ]
