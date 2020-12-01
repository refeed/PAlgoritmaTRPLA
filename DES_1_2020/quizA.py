'''

DESKRIPSI SOAL

Terdapat byk skl cara / algoritma untuk mengurutkan suatu data didalam
suatu Array. Pada kasus ini disiapkan suatu algoritma. Terapkan Algoritma ini
sehingga dapat diketahui, berapa kali pertukaran dilakukan.

Algoritma:

1. Cari data terkecil dalam interval j = 0 sampai dengan j = N-1

2. Jika pada posisi pos ditemukan data yang terkecil, tukarkan data diposisi pos
   dengan data di posisi i jika k.

3. Ulangi langkah 1 dan 2 dengan j = j+i sampai dengan j = N-1, dan seterusnya
   sampai j = N - 1. PETUNJUK MASUKAN

Baris pertama berisi bilangan bulat N (0<=N<=100) yang menyatakan banyaknya
aksi.

Baris kedua merupakan deret angka isi dari Array PETUNJUK KELUARAN

terdapat 2 baris. Baris pertama berisi list N data input yang sudah terurut
ascending. Baris kedua berisi banyak pertukaran data yang dilakukan selama
proses pengurutan data. CONTOH MASUKAN

2
2 2

CONTOH KELUARAN

2 2
0

CONTOH MASUKAN

7
1 6 5 0 9 3 4

CONTOH KELUARAN

0 1 3 4 5 6 9
6

'''
import sys

# Ignore the first input
input()

list_to_be_sorted = list(map(int, input().split()))

# Selection sort

list_length = len(list_to_be_sorted)
converts_count = 0

for i in range(list_length):
    smallest_index = i
    convert_value = False
    for j in range(i+1, list_length):
        if list_to_be_sorted[j] < list_to_be_sorted[smallest_index]:
            smallest_index = j
            convert_value = True

    if not convert_value:
        continue

    list_to_be_sorted[i], list_to_be_sorted[smallest_index] = list_to_be_sorted[smallest_index], list_to_be_sorted[i]
    converts_count += 1

print(' '.join(list(map(str, list_to_be_sorted))))
sys.stdout.write(str(converts_count))
