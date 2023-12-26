# Generated by Django 4.2.7 on 2023-12-26 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0014_alter_surattugas_id_nomorsurat'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaporanEval',
            fields=[
                ('Nomor_Surat_Eval', models.CharField(default='', max_length=30, primary_key=True, serialize=False)),
                ('Tanggal_Surat_Eval', models.DateField()),
                ('Tahun_Anggaran', models.CharField(default='2024', max_length=4)),
                ('Periode_Awal', models.DateField()),
                ('Periode_Akhir', models.DateField()),
                ('Periode_Pegawai', models.DateField()),
                ('UPPD', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='surattugas',
            name='Nomor_Surat',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='LaporanEval_stat_peg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipe_Pegawai', models.CharField(max_length=20)),
                ('Jumlah_Pegawai', models.IntegerField(default=0)),
                ('Nomor_Surat_Eval', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.laporaneval')),
            ],
        ),
        migrations.CreateModel(
            name='LaporanEval_normatif_peg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Pegawai', models.CharField(max_length=20)),
                ('NIP_Pegawai', models.CharField(default='', max_length=50)),
                ('Jabatan_Pegawai', models.CharField(default='', max_length=200)),
                ('Nomor_Surat_Eval', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.laporaneval')),
            ],
        ),
        migrations.CreateModel(
            name='LaporanEval_keuangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Detail', models.TextField(default='')),
                ('Nomor_Surat_Eval', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.laporaneval')),
            ],
        ),
        migrations.CreateModel(
            name='LaporanEval_Hasil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hasil', models.CharField(max_length=200)),
                ('Nomor_Surat_Eval', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.laporaneval')),
            ],
        ),
        migrations.CreateModel(
            name='LaporanEval_DataUmum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.CharField(max_length=200)),
                ('Nomor_Surat_Eval', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.laporaneval')),
            ],
        ),
        migrations.AddField(
            model_name='laporaneval',
            name='Nomor_Surat_Tugas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='surat.surattugas'),
        ),
    ]