'''
Soal Bab 5 Quiz modul nomor 3
Constraints:
- Tidak boleh loop
- Tidak boleh menggunakan `in`
- Tidak boleh menggunakan `return`
- Hanya boleh melakukan percabangan dan semua materi yang dipelajari di kelas
'''

NOTVALID_STR = 'tidak valid'
VALID_STR = 'valid'

angka_input = list(map(int, input().split()))

# Bisa ditulis a, b, c = angka_input
tanggal = angka_input[0]
bulan = angka_input[1]
tahun = angka_input[2]

hasil = VALID_STR


if (tanggal > 31 or
        tanggal < 1 or
        tahun < 0 or
        bulan > 12 or
        bulan < 1):
    hasil = NOTVALID_STR
elif bulan <= 7:
    if bulan % 2 == 0:
        if bulan == 2:
            if tanggal > 29:
                hasil = NOTVALID_STR
            elif (tahun % 4 != 0 or
                  (tahun % 100 == 0 and tahun % 400 != 0)):
                if tanggal > 28:
                    hasil = NOTVALID_STR
        elif tanggal > 30:
            hasil = NOTVALID_STR
elif bulan % 2 != 0 and tanggal > 30:
    # Jika bulan lebih besar daripada 7 dan ganjil dan tanggalnya lebih besar
    # daripada 30
    hasil = NOTVALID_STR

print(hasil)
