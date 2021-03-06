# Generated by Django 4.0.4 on 2022-05-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_attraction_options_alter_attraction_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='опубликован'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='work_time',
            field=models.CharField(max_length=100, verbose_name='Время работы'),
        ),
    ]
