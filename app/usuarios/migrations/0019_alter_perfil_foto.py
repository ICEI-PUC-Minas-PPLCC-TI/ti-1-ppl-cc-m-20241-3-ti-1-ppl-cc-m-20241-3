# Generated by Django 5.0.6 on 2024-06-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0018_alter_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios/media/'),
        ),
    ]
