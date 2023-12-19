from django.urls import path
from surat.views import Login,Pegawai_create, Pegawai_delete, Pegawai_list, Pegawai_update, Logout
from surat.views import Jabatan_create,Jabatan_delete, Jabatan_list, Jabatan_update
from surat.views import Struktur_create,Struktur_delete,Struktur_list,Struktur_update
from surat.views import User_list, User_create, User_delete, User_update, Konfigurasi_list, Konfigurasi_create
from surat.views import SuratTugas_create, DasarTugas_create, SuratTugas_list, DasarTugas_list

urlpatterns = [
    path('', Login,name="Login"),
    path('logout/',Logout,name="Logout"),
    path('pegawai/create/',Pegawai_create,name='pegawai_create'),
    path('pegawai/list/',Pegawai_list,name='pegawai_list'),
    path('pegawai/update/',Pegawai_update,name='pegawai_update'),
    path('pegawai/delete/',Pegawai_delete,name='pegawai_delete'),
    path('jabatan/create/',Jabatan_create,name='jabatan_create'),
    path('jabatan/list/',Jabatan_list,name='jabatan_list'),
    path('jabatan/update/',Jabatan_update,name='jabatan_update'),
    path('jabatan/delete/',Jabatan_delete,name='jabatan_delete'),
    path('struktur/create/',Struktur_create,name='struktur_create'),
    path('struktur/list/',Struktur_list,name='struktur_list'),
    path('struktur/update/',Struktur_update,name='struktur_update'),
    path('struktur/delete/',Struktur_delete,name='struktur_delete'),
    path('user/create/',User_create,name='user_create'),
    path('user/list/',User_list,name='user_list'),
    path('user/update/',User_update,name='suser_update'),
    path('user/delete/',User_delete,name='user_delete'),
    path('konfigurasi/list/',Konfigurasi_list,name='konfigurasi_list'),
    path('konfigurasi/create/',Konfigurasi_create,name='konfigurasi_create'),
    path('surattugas/create/',SuratTugas_create,name='SuratTugas_create'),
    path('dasartugas/create/',DasarTugas_create,name='DasarTugas_create'),
    path('surattugas/list/',SuratTugas_list,name='SuratTugas_list'),
    path('dasartugas/list/',DasarTugas_list,name='DasarTugas_list'),
]
