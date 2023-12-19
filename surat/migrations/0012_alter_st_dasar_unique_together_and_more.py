# Generated by Django 4.2.7 on 2023-12-19 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0011_surattugas_isdone'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='st_dasar',
            unique_together={('Nomor_Surat', 'Dasar')},
        ),
        migrations.AlterUniqueTogether(
            name='st_peserta',
            unique_together={('Nomor_Surat', 'Peserta')},
        ),
    ]
