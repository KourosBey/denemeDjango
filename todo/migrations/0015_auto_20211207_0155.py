# Generated by Django 3.2.9 on 2021-12-06 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_alter_ogretmen_k_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanci',
            name='k_ilgi',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='todo.ilgi_alanlari'),
        ),
        migrations.DeleteModel(
            name='K_Ilgi_Alani',
        ),
    ]
