# Generated by Django 4.0.2 on 2022-03-13 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttractionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Тип аттракциона',
                'verbose_name_plural': 'Типы аттракционов',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ParkLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тематическая земля',
                'verbose_name_plural': 'Тематические земли',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image_url', models.ImageField(blank=True, help_text='690х388 *.jpg или *.png', upload_to='attraction', verbose_name='Изображение JPG, PNG')),
                ('short_description', models.CharField(max_length=600)),
                ('description', models.TextField(blank=True, help_text='текст', verbose_name='Описание')),
                ('work_time', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=6, verbose_name='Возраст')),
                ('height', models.IntegerField(default=100, verbose_name='Сортировка')),
                ('with_adults', models.BooleanField(default=False, verbose_name='посещение со взрослыми')),
                ('is_purchased_separately', models.BooleanField(default=False, verbose_name='покупается отдельно')),
                ('specs', models.CharField(blank=True, max_length=400, verbose_name='Специальная информация')),
                ('is_active', models.BooleanField(default=False, verbose_name='активен')),
                ('is_working', models.BooleanField(default=False, verbose_name='работает')),
                ('sorting', models.IntegerField(default=500, verbose_name='Сортировка')),
                ('wait_time', models.IntegerField(default=10, verbose_name='Время ожидания минут')),
                ('attr_types', models.ManyToManyField(blank=True, to='api.AttractionType')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.parklocation')),
            ],
            options={
                'verbose_name': 'Аттракцион',
                'verbose_name_plural': 'Аттракционы',
                'ordering': ('title',),
            },
        ),
    ]
