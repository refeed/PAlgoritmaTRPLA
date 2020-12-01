'''
DESKRIPSI SOAL

Pengkodean A1Z26 adalah metode enkripsi subtitusi sederhana yang mengubah huruf
“A” menjadi angka 1, “B” menjadi angka 2, dan seterusnya hingga “Z” menjadi 26,
atau sebaliknya. Buatlah program yang menerima masukan angka-angka, lalu kodekan
menjadi huruf yang bersesuaian. PETUNJUK MASUKAN

Input adalah sekumpulan angka yang diinputkan dengan format berikut:

n t
a1 a2 a3 ... an

Nilai n (0 < n ≤ 30) adalah banyak angka yang akan diinputkan dan a1 sampai an
adalah angka yang harus dikodekan. Nilai t antara 1 atau 0, jika t bernilai 1
artinya outputkan dalam huruf tidak kapital, dan jika nilai t adalah 0 outputkan
dalam huruf kapital. PETUNJUK KELUARAN

Sebuah string hasil pengkodean, ditulis sambung tanpa spasi

CONTOH MASUKAN

6 0
22 15 11 1 19 9

CONTOH KELUARAN

VOKASI
'''

_, capitalize_output = list(map(int, input().split()))
number_list = list(map(int, input().split()))

CAPITALIZE_CHAR_OFFSET = ord('A') - 1
SMALL_CHAR_OFFSET = ord('a') - 1

string_list = []

for num in number_list:
    if capitalize_output == 0:
        string_list.append(chr(num + CAPITALIZE_CHAR_OFFSET))
    else:
        string_list.append(chr(num + SMALL_CHAR_OFFSET))

print(''.join(string_list))
