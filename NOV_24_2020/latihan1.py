"""
Buatlah program untuk mengurutkan daftar nama orang. Diinputkan 5 buah nama
orang. Outputkan nama-nama tersebut terurut secara leksikografis (terurut seperti di
kamus).
"""

def merge_sort_str(list_awal):
    if len(list_awal) == 1:
        return

    tengah = len(list_awal) // 2
    list_kiri = list_awal[:tengah]
    list_kanan = list_awal[tengah:]

    # Split and merge sort
    merge_sort_str(list_kiri)
    merge_sort_str(list_kanan)

    # Merge
    i = 0  # iterator untuk list_kiri
    j = 0  # iterator untuk list_kanan
    k = 0  # iterator untuk list_awal
    l = 0  # iterator untuk char dalam list/string

    while i < len(list_kiri) and j < len(list_kanan):
        # Jika ada string dengan huruf yang sama
        # cari indeks sampai hurufnya berbeda
        while (l < (len(list_kiri[i]) - 1) and
               l < (len(list_kanan[j]) - 1) and
               list_kiri[i][l] == list_kanan[j][l]):
            l += 1
        # Jika ternyata masih sama juga, string yang memiliki
        # panjang lebih pendek akan memiliki kedudukan yang lebih tinggi
        # if list_kiri[i][l] == list_kanan[j][l]:
        #     if len(list_kiri[i]) < len(list_kanan[j]):
        #         list_awal[k] = list_kiri[i]
        #         i += 1
        #     else:
        #         list_awal[k] = list_kanan[j]
        #         j += 1
        #     k += 1
        #     l = 0
        #     continue

        if ((list_kiri[i][l] == list_kanan[j][l] and
                len(list_kiri[i]) < len(list_kanan[j])) or
             list_kiri[i][l] < list_kanan[j][l]):
            list_awal[k] = list_kiri[i]
            i += 1
        else:
            list_awal[k] = list_kanan[j]
            j += 1
        k += 1
        l = 0  # Set balik l ke 0

    # Sisanya
    while i < len(list_kiri):
        list_awal[k] = list_kiri[i]
        i += 1
        k += 1

    while j < len(list_kanan):
        list_awal[k] = list_kanan[j]
        j += 1
        k += 1


nama_str_list = []

for i in range(5):
    nama_str_list.append(input())

merge_sort_str(nama_str_list)

for nama in nama_str_list:
    print(nama)
