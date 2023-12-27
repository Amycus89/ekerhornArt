# Generated by Django 4.2.6 on 2023-12-27 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=46)),
                ('background', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('location_name', models.CharField(max_length=46)),
                ('street', models.CharField(max_length=46)),
                ('city', models.CharField(max_length=46)),
                ('download_file', models.FileField(blank=True, upload_to='files/')),
                ('read_more', models.URLField(blank=True)),
            ],
        ),
    ]