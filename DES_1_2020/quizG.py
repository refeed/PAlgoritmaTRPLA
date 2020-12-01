'''
DESKRIPSI SOAL

Kali ini Adi belajar baris-berbaris. Ada N peserta baris-berbaris yang ikut. Seperti biasa, peserta harus berbaris sesuai urutan tinggi badan (yang paling tinggi di belakang). Setelah berbaris dengan urut, peserta akan diberi no urut. No 1 untuk peserta yang paling pendek dan no N untuk peserta paling tinggi. Tinggi badan Adi adalah 165 cm. Tentukan no peserta yang dikenakan oleh Adi (asumsi tidak ada peserta yang tingginya sama).
PETUNJUK MASUKAN

Baris pertama adalah bilangan bulat N yang menunjukkan banyaknya peserta.

N baris berikutnya adalah tinggi dari setiap peserta. Tinggi Adi adalah 165 cm.
PETUNJUK KELUARAN

Bilangan antara 1-N yang menunjukkan no peserta dari Adi.
CONTOH MASUKAN

4
170
158
165
168

CONTOH KELUARAN

2

Adi akan diberi no urut 2 karena tinggi badannya nomor 2 dihitung dari yang paling pendek.
'''
import sys


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


def binary_search(list_awal, wanted_value, lo, hi):
    mid_index = (lo + hi) // 2
    mid_value = list_awal[mid_index]

    if mid_value == wanted_value:
        return mid_index
    elif (hi - lo) <= 1:
        return -1  # Not found
    elif wanted_value > mid_value:
        return binary_search(list_awal, wanted_value, mid_index+1, hi)
    elif wanted_value < mid_value:
        return binary_search(list_awal, wanted_value, lo, mid_index)


if __name__ == "__main__":
    input_list = []
    list_length = int(input())

    for _ in range(list_length):
        input_list.append(int(input()))

    merge_sort(input_list)
    sys.stdout.write(str(binary_search(input_list, 165, 0, list_length-1) + 1))
