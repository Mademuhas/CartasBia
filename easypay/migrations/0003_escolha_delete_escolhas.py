# Generated by Django 4.1.7 on 2025-02-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypay', '0002_escolhas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Escolhas',
        ),
    ]
