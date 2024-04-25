# Generated by Django 5.0.4 on 2024-04-25 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myformsapp', '0003_rename_field1_mymodel_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='field2',
            new_name='Profesion',
        ),
        migrations.AddField(
            model_name='mymodel',
            name='Mensaje',
            field=models.TextField(default='Esta casilla es para tu mensaje'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='Telefono',
            field=models.CharField(default=11111111, max_length=100),
            preserve_default=False,
        ),
    ]