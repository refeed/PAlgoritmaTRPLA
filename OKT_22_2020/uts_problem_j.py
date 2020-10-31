"""
DESKRIPSI SOAL

Buatlah program untuk menghitung selisih waktu dalam jam, menit, detik. Masukan
adalah jam, menit, detik mulaidan jam, menit, detik selesai. Keluaran adalah
selisih waktunya.

PETUNJUK MASUKAN

Input terdiri atas 2 baris dengan masing-masing baris terdiri dari 3 angka yang
dipisahkan spasi

PETUNJUK KELUARAN

Outputkan Terdiri dari 3 angka dalam satu baris (pisahkan dengan spasi) yang
merupakan selisih dari input pada baris pertama dan kedua
"""

hour1, min1, sec1 = list(map(int, input().split()))
hour2, min2, sec2 = list(map(int, input().split()))

secs1 = hour1*3600 + min1*60 + sec1
secs2 = hour2*3600 + min2*60 + sec2

difference_secs = abs(secs1 - secs2)

# Result
hour3 = difference_secs // 3600
difference_secs -= hour3 * 3600
min3 = difference_secs // 60
difference_secs -= min3 * 60
sec3 = difference_secs

print(hour3, min3, sec3)
