# Generated by Django 3.1.7 on 2021-04-23 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cover',
            field=models.CharField(default='https://i.imgur.com/oDxz1yY.png', max_length=200),
        ),
    ]
