'''
Maximum Scalar Product
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Diberikan 2 buah array X dan Y yang masing-masing berisi N buah bilangan bulat. Perkalian scalar dari X dan Y adalah X1*Y1 + X2*Y2 + X3*Y3 + .... + XN*YN. Jika kita diperbolehkan untuk melakukan permutasi terhadap elemen-elemen pada array X dan Y, berapakah perkalian scalar maksimum yang dapat dihasilkan?

Sebagai contoh, misalkan N = 4, array X berisi {1,3,5,7} dan Y berisi {2,4,6,8}. Beberapa konfigurasi yang mungkin adalah:
Xi 	5 	1 	7 	3
Yi 	8 	2 	4 	6
Xi*Yi 	40 	2 	28 	18
Total 	88

Xi 	3 	5 	7 	1
Yi 	2 	8 	6 	4
Xi*Yi 	6 	40 	42 	4
Total 	92

Dan masih banyak lagi konfigurasi yang mungkin. Anda diminta untuk mencari konfigurasi yang bisa menghasilkan scalar product maksimal
PETUNJUK MASUKAN

Baris pertama terdiri dari sebuah bilangan bulat N (1 ≤ N ≤ 1000).

Baris kedua terdiri atas N buah bilangan yang menyatakan bilangan-bilangan pada array X (0 ≤ Xi ≤ 1000)

Baris ketiga terdiri atas N buah bilangan yang menyatakan bilangan-bilangan pada array Y (0 ≤ Yi ≤ 1000)
PETUNJUK KELUARAN

Outputkan perkalian scalar maksimal yang dapat dihasilkan.
CONTOH MASUKAN

4
1 3 5 7
2 4 6 8

CONTOH KELUARAN

100
'''


def merge_sort(list_awal):
    list_awal_length = len(list_awal)

    if list_awal_length == 1:
        return

    # Split
    tengah = list_awal_length // 2
    list_kiri = list_awal[:tengah]
    list_kanan = list_awal[tengah:]

    merge_sort(list_kiri)
    merge_sort(list_kanan)

    # Merge
    i = 0  # Iterator untuk list kiri
    j = 0  # Iterator untuk list kanan
    k = 0  # Iterator untuk list awal

    while i < len(list_kiri) and j < len(list_kanan):
        if list_kiri[i] < list_kanan[j]:
            list_awal[k] = list_kiri[i]
            i += 1
        else:
            list_awal[k] = list_kanan[j]
            j += 1
        k += 1

    while i < len(list_kiri):
        list_awal[k] = list_kiri[i]
        i += 1
        k += 1

    while j < len(list_kanan):
        list_awal[k] = list_kanan[j]
        j += 1
        k += 1


if __name__ == "__main__":
    list_length = int(input())
    array_X_list = list(map(int, input().split()))
    array_Y_list = list(map(int, input().split()))

    merge_sort(array_X_list)
    merge_sort(array_Y_list)

    array_sum = 0
    for i in range(list_length):
        array_sum += array_X_list[i] * array_Y_list[i]

    print(array_sum)
