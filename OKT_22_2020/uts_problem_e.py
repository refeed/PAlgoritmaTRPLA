"""
DESKRIPSI SOAL

Pak Blangkon sedang membuat usaha penyewaan arena futsal. Toni dan kawan
kawannya sering sekali bermain di sana, pada suatu hari Toni menyewa lapangan
selama T detik. Dengan tarif H rupiah perjam (perlu diketahui biaya sewa
dibulatkan ke bawah ke jam terdekat, jadi jika seseorang meminjam kurang dari 1
jam, Pak Blangkon yang baik ini akan menyewakan secara gratis!) tentukan biaya
yang harus Toni bayar ke Pak Blangkon. PETUNJUK MASUKAN

Dua buah bilangan bulat T dan H. T adalah lama menyewa Toni dalam detik. H
adalah harga tiap jamnya.(1 ≤ X,Y ≤ 100000) PETUNJUK KELUARAN

Harga yang harus dibayar.
"""

t, h = list(map(int, input().split()))

hours_rounded_down = t // 3600

print(hours_rounded_down * h)
