"""
Buatlah program untuk menentukan apakah dua buah string terdiri dari huruf yang
sama atau tidak. Dua buah string yang terdiri dari huruf-huruf yang sama disebut
dengan anagram. Misalnya pada kata “harum” dan “rumah” keduanya terdiri dari
huruf yang sama.
"""
def merge_sort(list_awal):
    if len(list_awal) == 1:
        return

    tengah = len(list_awal) // 2
    list_kiri = list_awal[:tengah]
    list_kanan = list_awal[tengah:]

    # Split and merge sort
    merge_sort(list_kiri)
    merge_sort(list_kanan)

    # Merge
    i = 0  # iterator untuk list_kiri
    j = 0  # iterator untuk list_kanan
    k = 0  # iterator untuk list_awal

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


input_str1 = input()
input_str2 = input()

# Tukar semuanya ke angka ascii
# input_str1_list = [ord(chr) for chr in input_str1]
# input_str2_list = [ord(chr) for chr in input_str2]
input_str1_list = []
for chr in input_str1:
    input_str1_list.append(ord(chr))

input_str2_list = []
for chr in input_str2:
    input_str2_list.append(ord(chr))

merge_sort(input_str1_list)
merge_sort(input_str2_list)

apakah_sama = True

for i in range(len(input_str1_list)):
    if input_str1_list[i] != input_str2_list[i]:
        apakah_sama = False

if apakah_sama:
    print('SAMA')
else:
    print('TIDAK SAMA')
