'''
Dimiliki N buah data bilangan bulat. Tentukan berapa banyak data yang nilainya
sama dengan nilai terbesar pada tersebut.
'''

from random import randint

n_data = [randint(0, 10) for _ in range(20)]
print('n_data = ', n_data)

def merge_sort_desc(list_awal):
    # Merge sort yang menurun dari besar ke kecil
    if len(list_awal) == 1:
        return

    # Split
    indeks_tengah = len(list_awal) // 2
    list_kiri = list_awal[:indeks_tengah]
    list_kanan = list_awal[indeks_tengah:]

    merge_sort_desc(list_kiri)
    merge_sort_desc(list_kanan)

    # Merge
    i = 0  # Iterator untuk list_kiri
    j = 0  # Iterator untuk list_kanan
    k = 0  # Iterator untuk list_awal

    while i < len(list_kiri) and j < len(list_kanan):
        if list_kiri[i] > list_kanan[j]:
            list_awal[k] = list_kiri[i]
            i += 1
        else:
            list_awal[k] = list_kanan[j]
            j += 1
        k += 1

    # Sisanya
    while i < len(list_kiri):
        list_awal[k] = list_kiri[i]
        i += 1
        k += 1

    while j < len(list_kanan):
        list_awal[k] = list_kanan[j]
        j += 1
        k += 1

merge_sort_desc(n_data)

i = 1  # iterator untuk list n_data juga menandakan banyaknya bilangan yang sama dengan bilangan terbesar

# Indeks ke-0 merupakan bilangan terbesar
while n_data[0] == n_data[i]:
    i += 1

print(i)
