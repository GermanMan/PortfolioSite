# Generated by Django 3.1.5 on 2021-01-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='text',
            field=models.TextField(),
        ),
    ]