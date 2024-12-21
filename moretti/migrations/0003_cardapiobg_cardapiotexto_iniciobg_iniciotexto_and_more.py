# Generated by Django 5.1.3 on 2024-12-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moretti', '0002_alter_acesso_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardapioBg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introducao', models.ImageField(upload_to='moretti/cms')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CardapioTexto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introducao_titulo', models.TextField()),
                ('introducao_subtitulo', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InicioBg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introducao', models.ImageField(upload_to='moretti/cms')),
                ('banner1', models.ImageField(upload_to='moretti/cms')),
                ('banner2', models.ImageField(upload_to='moretti/cms')),
                ('banner3', models.ImageField(upload_to='moretti/cms')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InicioTexto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introducao_titulo', models.TextField()),
                ('introducao_subtitulo', models.TextField()),
                ('banner1_titulo', models.TextField()),
                ('banner2_titulo', models.TextField()),
                ('banner3_titulo', models.TextField()),
                ('localizacao_endereco', models.TextField()),
                ('localizacao_link_maps', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SobreBg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introducao', models.ImageField(upload_to='moretti/cms')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SobreImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fundador', models.ImageField(upload_to='moretti/cms')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SobreTexto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introducao_titulo', models.TextField()),
                ('introducao_subtitulo', models.TextField()),
                ('texto1', models.TextField()),
                ('texto2', models.TextField()),
                ('texto3', models.TextField()),
                ('texto4', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='prato',
            name='imagem',
            field=models.ImageField(upload_to='moretti/pratos'),
        ),
    ]
