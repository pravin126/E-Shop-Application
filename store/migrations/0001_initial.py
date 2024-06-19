# Generated by Django 5.0.6 on 2024-06-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(default=' ', max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
