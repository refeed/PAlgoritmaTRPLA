'''

DESKRIPSI SOAL

Susi dan Santi merupakan kakak beradik yang sangat kompak. Tebaklah, siapa yang
menjadi kakak dengan melihat tanggal lahir mereka. PETUNJUK MASUKAN

Input terdiri atas 2 baris dengan masing-masing baris 3 input (tanggal, bulan,
tahun)

Baris pertama untuk Susi, baris kedua untuk Santi

PETUNJUK KELUARAN

Nama orang yang lebih tua (Susi atau Santi atau Kembar) dengan huruf depan
menggunakan huruf kapital

CONTOH MASUKAN

21 11 1999 22 10 1999

CONTOH KELUARAN

Santi

CONTOH MASUKAN

10 10 2010 10 10 2010

CONTOH KELUARAN

Kembar

'''

susi_year_input = list(map(int, input().split()))
santi_year_input = list(map(int, input().split()))

SUSI_STR = 'Susi'
SANTI_STR = 'Santi'
KEMBAR_STR = 'Kembar'

result = KEMBAR_STR

for i in range(2, -1, -1):
    if susi_year_input[i] < santi_year_input[i]:
        result = SUSI_STR
        break
    elif susi_year_input[i] > santi_year_input[i]:
        result = SANTI_STR
        break

print(result)
