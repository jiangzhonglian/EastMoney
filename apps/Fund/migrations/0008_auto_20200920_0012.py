# Generated by Django 3.1.1 on 2020-09-20 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fund', '0007_auto_20200920_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='update_time',
            field=models.DateTimeField(null=True, verbose_name='更新时间'),
        ),
    ]