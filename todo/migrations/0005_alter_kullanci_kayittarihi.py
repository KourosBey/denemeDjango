# Generated by Django 3.2.9 on 2021-11-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_remove_kullanci_k_turu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kullanci',
            name='kayitTarihi',
            field=models.DateField(),
        ),
    ]