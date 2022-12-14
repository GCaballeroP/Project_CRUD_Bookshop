# Generated by Django 4.1.1 on 2022-10-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('image', models.ImageField(null=True, upload_to='img/', verbose_name='Imagen')),
                ('description', models.TextField(null=True, verbose_name='Descripción')),
            ],
        ),
    ]
