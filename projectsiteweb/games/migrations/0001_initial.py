# Generated by Django 5.1.3 on 2024-11-27 15:31

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            managers=[
                ('sorted_genres', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, null=True, verbose_name='image_game')),
                ('title', models.CharField(help_text='Name of game goes here', max_length=200, unique=True, verbose_name='name game')),
                ('languages', models.CharField(default='English', help_text='Here goes language of game', max_length=100)),
                ('size', models.DecimalField(decimal_places=2, max_digits=100)),
                ('format', models.CharField(blank=True, choices=[('ISO', 'Iso'), ('WBFS', 'Wbfs'), ('RGH', 'Rgh')], max_length=100, null=True)),
                ('platform', models.CharField(blank=True, choices=[('PC', 'Pc'), ('XBOX360', 'Xbox'), ('PLAYSTATION 4', 'Ps4'), ('PLAYSTATION 3', 'Ps3'), ('PLAYSTATION 2', 'Ps2'), ('GAMEBOY ADVANCE', 'Gba'), ('NINTENDO DS', 'Nds')], max_length=100, null=True)),
                ('version', models.CharField(blank=True, max_length=10, null=True)),
                ('genre', models.ManyToManyField(related_name='genres', related_query_name='genre', to='games.genre')),
            ],
        ),
    ]
