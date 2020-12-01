'''

DESKRIPSI SOAL

Buatlah program yang menerima 4 buah input nilai, outputkan nilai paling besar kedua diantara keempat input tersebut.
PETUNJUK MASUKAN

Input terdiri atas 4 angka dalam 1 baris
PETUNJUK KELUARAN

Outputkan angka terbesar kedua dari 4 angka yang dimasukkan
CONTOH MASUKAN

1 2 3 4

CONTOH KELUARAN

3

CONTOH MASUKAN

10 9 11 11

CONTOH KELUARAN

11

'''
def merge_sort(list_awal):
    list_awal_length = len(list_awal)

    if list_awal_length == 1:
        return

    # Split
    tengah = list_awal_length // 2
    list_kiri = list_awal[:tengah]
    list_kanan = list_awal[tengah:]

    merge_sort(list_kiri)
    merge_sort(list_kanan)

    # Merge
    i = 0  # Iterator untuk list kiri
    j = 0  # Iterator untuk list kanan
    k = 0  # Iterator untuk list awal

    while i < len(list_kiri) and j < len(list_kanan):
        if list_kiri[i] < list_kanan[j]:
            list_awal[k] = list_kiri[i]
            i += 1
        else:
            list_awal[k] = list_kanan[j]
            j += 1
        k += 1

    while i < len(list_kiri):
        list_awal[k] = list_kiri[i]
        i += 1
        k += 1

    while j < len(list_kanan):
        list_awal[k] = list_kanan[j]
        j += 1
        k += 1

if __name__ == "__main__":
    num_list = list(map(int, input().split()))
    merge_sort(num_list)
    print(num_list[-2])
