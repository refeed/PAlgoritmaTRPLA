"""
DESKRIPSI SOAL

Pak Blangkon ingin memberi nilai siswa-siswanya. Aturan penilaiannya adalah
sebagai berikut

    Semua nilai angka yang lebih dari sama dengan 75 maka akan dapat A
    Semua nilai angka yang tidak lebih dari sama dengan 45 maka akan dapat B/C
    Nilai angka yang belum dapat nilai huruf, jika nilai angka tersebut lebih
      besar dari rata-rata maka akan dapat A/B
    Nilai angka yang belum dapat nilai huruf akan otomatis mendapat B

Bantu Pak Blangkon untuk membuat program yang dapat menentukan berapa banyak
yang dapat A, A/B, B, dan B/C.

PETUNJUK MASUKAN

Pada baris pertama adalah sebuah bilangan bulat N yang merupakan banyak siswa
yang akan diinputkan. Pada baris kedua terdapat N buah nilai siswa. Maksimal
akan terdapat 30 siswa dengan nilai siswa antara 0 sampai 100. PETUNJUK
KELUARAN

Outputkan empat buah nilai, yakni banyak siswa yang dapat A, A/B, B, dan B/C
secara berturut-turut.
"""

n = int(input())
grades = list(map(int, input().split()))

got_a = 0
got_a_b = 0
got_b = 0
got_b_c = 0

sum_grades = 0

for i in range(n):
    sum_grades += grades[i]

average_grade = sum_grades/n

for i in range(n):
    if grades[i] >= 75:
        got_a += 1
    elif grades[i] < 45:
        got_b_c += 1
    elif grades[i] > average_grade:
        got_a_b += 1
    else:
        got_b += 1

print(got_a, got_a_b, got_b, got_b_c)
