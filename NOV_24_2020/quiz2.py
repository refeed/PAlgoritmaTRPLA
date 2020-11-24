'''
Dimiliki N data bilangan bulat. Akan ditampilkan data terbesar ke-K sampai ke-M
dengan (1<=K<=M) dan (M <= N) data terbesar.
Misal terdapat 5 data: 7, 2, 10, 9, 1
Input: 2 4
Output: 9, 7, 2
'''
data_list = [7, 2, 10, 9, 1]

input_int = list(map(int, input().split()))


def merge_sort(list_awal):
    if len(list_awal) == 1:
        return

    # Split
    indeks_tengah = len(list_awal) // 2
    list_kiri = list_awal[:indeks_tengah]
    list_kanan = list_awal[indeks_tengah:]

    merge_sort(list_kiri)
    merge_sort(list_kanan)

    # Merge
    i = 0  # Iterator untuk list_kiri
    j = 0  # Iterator untuk list_kanan
    k = 0  # Iterator untuk list_awal

    while i < len(list_kiri) and j < len(list_kanan):
        if list_kiri[i] < list_kanan[j]:
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


merge_sort(data_list)

data_list = data_list[::-1]  # Balik urutan

hasil_list = data_list[input_int[0]-1:input_int[1]]

# Output formatting

hasil_str = str(hasil_list)[1:len(str(hasil_list))-1]

print(hasil_str)
