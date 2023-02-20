# Generated by Django 3.2.16 on 2023-02-20 10:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0034_auto_20230216_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('UID', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('PROJECT_ID', models.IntegerField(default=None)),
                ('DATASOURCE', models.CharField(default=None, max_length=500)),
                ('OPERATION', models.CharField(default=None, max_length=20)),
                ('CREATED_BY', models.CharField(max_length=100, null=True)),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True, null=True)),
                ('CALLED_FUNCTION_NAME', models.CharField(max_length=200, null=True)),
                ('LAYER', models.CharField(default=None, max_length=200, null=True)),
                ('TABLE_NAME', models.CharField(default=None, max_length=200, null=True)),
                ('STATUS', models.CharField(default=None, max_length=10, null=True)),
                ('MESSAGE', models.CharField(default=None, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dataqualitycheck',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='filtersymbol',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='goldlayerdata',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='querylogs',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transformation',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]