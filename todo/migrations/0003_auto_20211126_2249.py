# Generated by Django 3.2.9 on 2021-11-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_k_turu_kullanci_k_turu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kullanci',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='kullanci',
            name='kayitTarihi',
            field=models.DateField(auto_created=True),
        ),
    ]
