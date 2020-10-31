def cari_nilai_tengah(nomor):
    # `nomor` berada di antara 100 dan 999
    angka_puluhan = nomor % 100
    angka_tengah = angka_puluhan // 10
    return angka_tengah


print(cari_nilai_tengah(273))
