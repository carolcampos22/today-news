# Generated by Django 4.2.11 on 2024-04-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='register',
            options={'ordering': ['-created_at'], 'verbose_name': 'Formulário de publicação de notícias', 'verbose_name_plural': 'Formulários de publicações de notícias'},
        ),
        migrations.AddField(
            model_name='register',
            name='subtitle',
            field=models.CharField(default='Detalhes abaixo!', max_length=500),
        ),
        migrations.AlterField(
            model_name='register',
            name='category',
            field=models.CharField(choices=[(1, 'Filmes e séries'), (2, 'Tecnologia'), (3, 'Ciências'), (4, 'Entretenimento'), (5, 'Saúde'), (6, 'Educação')], max_length=50),
        ),
    ]
