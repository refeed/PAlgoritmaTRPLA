'''

DESKRIPSI

Buatlah program yang mengurutkan suatu subkumpulan bilangan dalam sebuah
kumpulan bilangan.

PETUNJUK MASUKAN

Baris pertama terdiri dari sebuah bilangan bulat N yang menyatakan banyak
bilangan (2 ≤ N ≤ 1000).

Baris kedua terdiri atas N buah bilangan yang dipisahkan dengan spasi (rentang
bilangan tidak akan melebihi integer).

Baris ketiga terdiri dari dua buah bilangan X dan Y dimana X adalah batas bawah
dan Y adalah batas atas subkumpulan bilangan yang akan disorting (1 ≤ X,Y ≤ N).
kemudian diikuti dengan sebuah huruf 'A' atau 'D' dimana A artinya Ascending dan
D berarti Descending.
PETUNJUK KELUARAN

Urutan bilangan ke-X hingga ke-Y secara ascending (menaik) atau descending (menurun).
CONTOH MASUKAN 1

5
1 4 3 2 6
1 3 D

CONTOH KELUARAN 1

4 3 1

CONTOH MASUKAN 2

5
1 4 3 2 6
1 5 A

CONTOH KELUARAN 2

1 2 3 4 6
'''

# Ignore the first input as we use dynamic array size (list)
input()

list_to_be_sorted = list(map(int, input().split()))

low_index, hi_index, ascending_or_descending = input().split()

low_index = int(low_index) - 1
hi_index = int(hi_index)

list_to_be_sorted = list_to_be_sorted[low_index:hi_index]


# Bubble sort

for _ in range(len(list_to_be_sorted) - 1):
    for i in range(len(list_to_be_sorted) - 1):
        comparison = (list_to_be_sorted[i] > list_to_be_sorted[i+1])
        if ascending_or_descending == 'D':
            comparison = not comparison
        if comparison:
            # Convert
            tmp = list_to_be_sorted[i]
            list_to_be_sorted[i] = list_to_be_sorted[i+1]
            list_to_be_sorted[i+1] = tmp

print(' '.join(list(map(str, list_to_be_sorted))))
