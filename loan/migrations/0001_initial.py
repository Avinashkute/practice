# Generated by Django 4.2.3 on 2023-08-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crop_loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('Acres', models.IntegerField()),
            ],
        ),
    ]