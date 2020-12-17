'''

DESKRIPSI SOAL

Koko membuat N buah tumpukan kayu yang bertempat di sebuah wadah. Kemudian, dia
memiringkan wadah tersebut ke kanan. Karena dimiringkan tersebut, bisa jadi
banyak kayu yang bergeser ke kanan.

Misalkan awalnya Koko mempunyai 4 buah tumpukan, dengan tinggi 3, 2, 1, 2.
Setelah dimiringkan ke kanan, posisi akhirnya yaitu 1, 2, 2, 3 (dimulai dari
kiri), seperti terlihat pada gambar berikut.

(Gambar ada di direktori yang sama dengan nama quizJ.jpg)

Jika N sangat banyak, Koko penasaran bagaimana posisi akhirnya.

PETUNJUK MASUKAN

Input terdiri atas 1 baris yang terdiri atas beberapa angka yang menyatakan
tinggi dari masing-masing tumpukan. (tinggi masing-masing tumpukan tidak akan
lebih dari 100). Setiap angka dipisahkan dengan spasi

PETUNJUK KELUARAN

Outputkan posisi akhirnya.

CONTOH MASUKAN

3 2 1 2

CONTOH KELUARAN

1 2 2 3

CONTOH MASUKAN

2 3 8

CONTOH KELUARAN

2 3 8
'''
# This is an ascending sorting problem

num_list = list(map(int, input().split()))

def merge_sort(original_list):
    original_list_len = len(original_list)
    if original_list_len == 1:
        return original_list

    # Split
    mid_index = original_list_len // 2
    left_list = original_list[:mid_index]
    right_list = original_list[mid_index:]

    merge_sort(left_list)
    merge_sort(right_list)

    # Merge
    i = 0  # iterator for left_list
    j = 0  # iterator for right_list
    k = 0  # iterator for original_list

    left_list_len = len(left_list)
    right_list_len = len(right_list)

    while i < left_list_len and j < right_list_len:
        if left_list[i] < right_list[j]:
            original_list[k] = left_list[i]
            i += 1
        else:
            original_list[k] = right_list[j]
            j += 1
        k += 1

    # Leftover
    while i < left_list_len:
        original_list[k] = left_list[i]
        i += 1
        k += 1

    while j < right_list_len:
        original_list[k] = right_list[j]
        j += 1
        k += 1

merge_sort(num_list)

num_list_str_list = list(map(str, num_list))

print(' '.join(num_list_str_list))
