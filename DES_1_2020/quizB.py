'''
DESKRIPSI SOAL

Badul diajarkan oleh gurunya suatu algoritma untuk mengurutkan suatu data
didalam suatu Array. Sang guru menajarinya dengan suatu analogi. Berikut
analoginya :

1. Semuanya dimulai dari posisi tangan kosong dan semua kartu masih tersimpan di
   atas meja. Anggap saja Anda hendak menyusun kartu ke tangan kiri Anda.

2. Anda lalu mengambil kartu pertama dari meja dan menyimpannya di tangan kiri.

3. Kemudian, Anda mengambil kartu kedua dari meja. Lalu, Anda membandingkan
   kartu tersebut dengan kartu yang ada di tangan kiri.

4. Jika kartu yang baru saja diambil dari meja memiliki nilai yang lebih kecil
   daripada kartu di tangan kiri, maka kartu tersebut akan diletakan di depan
   kartu pembanding

5. Kartu yang telah dibandingkan akan bergeser mundur.

6. Proses ini akan terus berlangsung sampai semua kartu terurut dengan benar
   sesuai kriteria pengurutannya.

7. Setelah semua kartu terurut, satu set kartu yang sudah terurut akan disimpan
   kembali ke meja.

Ternyata si Badul belum paham juga dengan analogi yang telah diberikan, Kemudian
sang guru mencontohkan dengan suatu data, yaitu Array berisi angka 5, 4, 3, 2, 1
kemudian sang guru menjabarkan tiap prosesnya. Dengan begitu Badul menjadi
paham.

proses 1

4 5 3 2 1

proses 2

4 3 5 2 1

3 4 5 2 1

proses 3

3 4 2 5 1

3 2 4 5 1

2 3 4 5 1

proses 4

2 3 4 1 5

2 3 1 4 5

2 1 3 4 5

1 2 3 4 5

Terapkan Algoritma ini sehingga dapat dihasilkan Array yang sudah terurut dan
dapat diketahui berapa kali pertukaran dilakukan.

PETUNJUK MASUKAN

Baris pertama berisi bilangan bulat N (0<=N<=100) yang menyatakan banyaknya
aksi.

Baris kedua merupakan deret angka isi dari Array

PETUNJUK KELUARAN

terdapat 2 baris. Baris pertama berisi list N data input yang sudah terurut
ascending. Baris kedua berisi banyak pertukaran data yang dilakukan selama
proses pengurutan data.



CONTOH MASUKAN

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

list_length = int(input())
list_to_be_sorted = list(map(int, input().split()))

convert_count = 0
# Insertion sort

for i in range(1, list_length):
   to_be_sorted = list_to_be_sorted[i]

   target_position = i - 1

   while target_position >= 0 and list_to_be_sorted[target_position] > to_be_sorted:
      list_to_be_sorted[target_position + 1] = list_to_be_sorted[target_position]
      target_position -= 1
      convert_count += 1
   list_to_be_sorted[target_position + 1] = to_be_sorted


print(' '.join(list(map(str, list_to_be_sorted))))
print(convert_count)
