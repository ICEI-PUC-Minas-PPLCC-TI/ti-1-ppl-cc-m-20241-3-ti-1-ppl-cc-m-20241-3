# Generated by Django 5.0.6 on 2024-06-30 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_alter_perfil_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_like', models.DateTimeField(auto_now_add=True)),
                ('usuario_que_deu_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_dados', to=settings.AUTH_USER_MODEL)),
                ('usuario_que_recebeu_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_recebidos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario_que_deu_like', 'usuario_que_recebeu_like')},
            },
        ),
    ]