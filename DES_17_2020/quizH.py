'''

DESKRIPSI SOAL

Akan dibuat sebuah pengundian doorprize berdasar nama peserta. Pada awalnya,
akan dilist semua nama peserta, kemudian akan dipilih nama peserta yang memiliki
nama terpendek.

PETUNJUK MASUKAN

Input terdiri atas 1 baris nama yang dipisahkan dengan spasi

PETUNJUK KELUARAN

Output terdiri dari 1 nama yang mendapatkan doorprize.

CONTOH MASUKAN

agus budi romi sri restu

CONTOH KELUARAN

sri

'''

name_list = input().split()

shortest_name = name_list[0]
shortest_name_len = len(shortest_name)

for name in name_list[1:]:
    name_length = len(name)
    if name_length < shortest_name_len:
        shortest_name = name
        shortest_name_len = name_length

print(shortest_name)
