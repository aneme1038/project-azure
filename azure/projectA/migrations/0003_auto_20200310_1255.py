# Generated by Django 2.2.10 on 2020-03-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectA', '0002_auto_20200303_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
