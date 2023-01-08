# Generated by Django 3.2.16 on 2023-01-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataQualityCheck',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data_source', models.CharField(blank=True, max_length=200, null=True)),
                ('column_name', models.CharField(blank=True, max_length=200, null=True)),
                ('null_check', models.BooleanField(blank=True, default=False, null=True)),
                ('date_check', models.BooleanField(blank=True, default=False, null=True)),
                ('special_character_check', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
