def print_angka_terbalik(nomor):
    # `nomor` berada di jarak 100 sampai 999
    ratusan = nomor // 100
    puluhan = (nomor - ratusan*100) // 10
    satuan = (nomor - ratusan*100 - puluhan*10)

    print(satuan, puluhan, ratusan)


print_angka_terbalik(100)
