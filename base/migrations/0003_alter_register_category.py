# Generated by Django 4.2.11 on 2024-04-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_register_options_register_subtitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='category',
            field=models.CharField(choices=[('Filmes e séries', 'Filmes e séries'), ('Tecnologia', 'Tecnologia'), ('Ciências', 'Ciências'), ('Entretenimento', 'Entretenimento'), ('Saúde', 'Saúde'), ('Educação', 'Educação')], max_length=50),
        ),
    ]
