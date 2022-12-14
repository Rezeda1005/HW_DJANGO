# Generated by Django 3.1.2 on 2022-10-11 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Датчик',
                'verbose_name_plural': 'Датчики',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Температура')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Снимок')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor', verbose_name='Датчик')),
            ],
            options={
                'verbose_name': 'Показание',
                'verbose_name_plural': 'Показания',
                'ordering': ['-date'],
            },
        ),
    ]
