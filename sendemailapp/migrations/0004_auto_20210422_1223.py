# Generated by Django 3.1.7 on 2021-04-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendemailapp', '0003_auto_20210422_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmail',
            name='namereceiver',
            field=models.CharField(max_length=200),
        ),
    ]
