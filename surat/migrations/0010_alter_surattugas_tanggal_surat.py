# Generated by Django 4.2.7 on 2023-12-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0009_surattugas_ketua_tim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surattugas',
            name='Tanggal_Surat',
            field=models.DateField(),
        ),
    ]
