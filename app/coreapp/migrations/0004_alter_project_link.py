# Generated by Django 4.0.3 on 2022-04-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
