# Generated by Django 5.1.1 on 2024-09-23 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_app', '0021_alter_livro_emprestado_data_devolucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro_emprestado',
            name='data_devolucao',
            field=models.DateField(default=datetime.date(2024, 10, 23)),
        ),
    ]
