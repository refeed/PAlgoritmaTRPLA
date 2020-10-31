"""
DESKRIPSI SOAL

Keindahan puisi dinilai dari seberapa "mirip" akhiran suatu baris dengan baris
yang lain yang berdekatan. Diinputkan dua buah string yang merupakan dua baris
puisi. Beri nilai keindahan dengan cara menghitung berapa banyak huruf yang
mirip diakhir kedua string tersebut. PETUNJUK MASUKAN

Dua buah string dengan panjang huruf yang sama, tidak mengandung spasi dan
hanya terdiri dari huruf tidak kapital

PETUNJUK KELUARAN

Outputkan sebuah bilangan bulat sesuai penjelasan di atas
"""

str_1 = input()
str_2 = input()

same_chars_count = 0

for i in range(1, len(str_1) + 1):
    if str_1[-i] == str_2[-i]:
        same_chars_count += 1
    else:
        break

print(same_chars_count)
