# Generated by Django 2.0.7 on 2018-07-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='user_pw',
            field=models.CharField(max_length=10),
        ),
    ]