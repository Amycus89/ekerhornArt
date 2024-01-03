# Generated by Django 4.2.6 on 2023-12-31 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.CharField(blank=True, max_length=46),
        ),
        migrations.AlterField(
            model_name='event',
            name='background',
            field=models.ImageField(upload_to='events/images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='download_file',
            field=models.FileField(blank=True, upload_to='events/files'),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
