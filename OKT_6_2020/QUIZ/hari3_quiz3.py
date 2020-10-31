'''
Soal Bab 5 Quiz nomor 2

Dibaca 3 Nilai : Nilai1, Nilai2, Nilai3. Syarat lulus adalah nilai rata2 > 50
dan boleh ada 1 nilai <= 40. Program menampilkan lulus atau tidak lulus.

Constraints:
- Tidak boleh loop
- Tidak boleh menggunakan `in`
- Tidak boleh menggunakan `return`
- Hanya boleh melakukan percabangan dan semua materi yang dipelajari di kelas
'''

angka_input = list(map(int, input().split()))

# Bisa ditulis a, b, c = angka_input
nilai1 = angka_input[0]
nilai2 = angka_input[1]
nilai3 = angka_input[2]

rata_rata = (nilai1 + nilai2 + nilai3) / 3


if rata_rata > 50:
    jumlah_kurang_dari_40 = 0
    if nilai1 <= 40:
        jumlah_kurang_dari_40 += 1
    if nilai2 <= 40:
        jumlah_kurang_dari_40 += 1
    if nilai3 <= 40:
        jumlah_kurang_dari_40 += 1

    if jumlah_kurang_dari_40 > 1:
        print('tidak lulus')
    else:
        print('lulus')
else:
    print('tidak lulus')
