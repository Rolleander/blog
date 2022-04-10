# Generated by Django 4.0.3 on 2022-04-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_codeexp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('link', models.CharField(max_length=50, unique=True)),
                ('previewFolder', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
