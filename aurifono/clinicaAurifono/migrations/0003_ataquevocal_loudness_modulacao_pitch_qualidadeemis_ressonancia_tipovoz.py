# Generated by Django 3.2.8 on 2021-11-26 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaAurifono', '0002_auto_20211125_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtaqueVocal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Ataque Vocal',
            },
        ),
        migrations.CreateModel(
            name='Loudness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Loudness',
            },
        ),
        migrations.CreateModel(
            name='Modulacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Modulação',
            },
        ),
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Pitch',
            },
        ),
        migrations.CreateModel(
            name='Qualidadeemis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Qualidade na Emissão',
            },
        ),
        migrations.CreateModel(
            name='Ressonancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Tipo de Ressonancia',
            },
        ),
        migrations.CreateModel(
            name='TipoVoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Tipo de Voz',
            },
        ),
    ]
