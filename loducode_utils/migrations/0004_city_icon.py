# Generated by Django 3.2 on 2023-02-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loducode_utils', '0003_auto_20210701_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='cities/', verbose_name='icon'),
        ),
    ]
