# Generated by Django 4.2.3 on 2024-05-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_usuarios_id_alter_usuarios_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
