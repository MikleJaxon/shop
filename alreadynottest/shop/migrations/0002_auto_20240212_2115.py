# Generated by Django 3.2.23 on 2024-02-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
    ]
