# Generated by Django 3.2.9 on 2021-11-20 18:49

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ilgi_Alanlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alan_Adi', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='K_Turu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('K_Turu', models.CharField(default='nonEmail', max_length=35, verbose_name='Tur')),
                ('Aciklama', models.CharField(max_length=35, verbose_name='Aciklama')),
            ],
        ),
        migrations.CreateModel(
            name='Kullanci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('k_email', models.EmailField(default='nonEmail', max_length=254, verbose_name='E-mail')),
                ('k_adi', models.CharField(default='nonEmail', max_length=35, verbose_name='k_adi')),
                ('k_soyadi', models.CharField(default='nonEmail', max_length=35, verbose_name='soyadi')),
                ('k_sifre', models.CharField(default='nonEmail', max_length=35)),
                ('kayitTarihi', models.DateField()),
                ('avatar', models.FileField(upload_to=builtins.id)),
                ('K_Turu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.k_turu')),
            ],
        ),
        migrations.CreateModel(
            name='Ogrenci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.FloatField()),
                ('k_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.kullanci')),
            ],
        ),
        migrations.CreateModel(
            name='Ogretmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ogr_tanitim', models.FileField(upload_to='')),
                ('stars', models.FloatField()),
                ('k_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.kullanci')),
            ],
        ),
        migrations.CreateModel(
            name='Randevular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ders_tarihi', models.DateField()),
                ('ogrenci_randevu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.ogrenci')),
                ('ogretmen_randevu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.ogretmen')),
            ],
        ),
        migrations.CreateModel(
            name='K_Ilgi_Alani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilgi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.ilgi_alanlari')),
                ('k_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.kullanci')),
            ],
        ),
    ]
