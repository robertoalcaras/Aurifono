# Generated by Django 3.2.8 on 2021-10-26 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='avaliacaoad_avaliacaoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataAvaliacao', models.DateField()),
                ('QOrelha', models.CharField(choices=[('ES', 'ESQUERDA'), ('DI', 'DIREITA')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='comunicoral_comunicoral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsc_habilidade', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='profissionalenc_profissionalenc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('1', 'Ativo'), ('0', 'Inativo')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='paciente_paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RG', models.CharField(max_length=12)),
                ('CPF', models.CharField(max_length=14)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('DataNascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('DataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do cadastro')),
                ('DataAtualizacao', models.DateTimeField(auto_now=True, verbose_name='Data da ultima atualização')),
                ('sexo', models.CharField(choices=[('feminino', 'Feminino'), ('masculino', 'Masculino')], max_length=9, verbose_name='Sexo')),
                ('Profissional_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinicaAurifono.profissionalenc_profissionalenc')),
            ],
        ),
        migrations.CreateModel(
            name='comunicoralidade_comunicoralidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resp_oralidade', models.CharField(max_length=1)),
                ('ComunicOral_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinicaAurifono.comunicoral_comunicoral')),
                ('avaliacaoAD_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinicaAurifono.avaliacaoad_avaliacaoad')),
            ],
        ),
        migrations.AddField(
            model_name='avaliacaoad_avaliacaoad',
            name='paciente_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinicaAurifono.paciente_paciente'),
        ),
    ]