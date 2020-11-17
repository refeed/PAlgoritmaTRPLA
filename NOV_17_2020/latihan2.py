def nama_terpanjang(list_nama):
    nama_terpanjang = ''

    for nama in list_nama:
        if len(nama) > len(nama_terpanjang):
            nama_terpanjang = nama

    return nama_terpanjang
