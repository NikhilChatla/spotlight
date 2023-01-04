# Generated by Django 3.2.16 on 2023-01-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20230104_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='dump_layer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='file_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='file_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='records_inserted',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='transformation_layer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upoload_layer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='valid_file_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]