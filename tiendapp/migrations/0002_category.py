# Generated by Django 5.1.4 on 2024-12-10 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]