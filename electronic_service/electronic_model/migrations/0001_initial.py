# Generated by Django 4.1.7 on 2023-03-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electronic_id', models.CharField(max_length=10)),
                ('electronic_category', models.CharField(max_length=50)),
                ('electronic_name', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
