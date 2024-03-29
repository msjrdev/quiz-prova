# Generated by Django 4.2.1 on 2024-03-11 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questao',
            name='imagem3',
            field=models.ImageField(blank=True, null=True, upload_to='quiz_imgs/'),
        ),
        migrations.AddField(
            model_name='questao',
            name='texto3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='TextoAssociado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questao_textoassociado', to='quiz.questao')),
            ],
            options={
                'verbose_name_plural': 'Textos associados',
            },
        ),
    ]
