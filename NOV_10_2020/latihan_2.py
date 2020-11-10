input_str = input().strip()


BESARKAN_CHAR_INT = ord('A') - ord('a')
KECILKAN_CHAR_INT = -BESARKAN_CHAR_INT

kalimat_rapi_list = []


for i in range(len(input_str)):
    char = input_str[i]
    if not (ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z')):
        # Berarti karakter merupakan simbol
        kalimat_rapi_list.append(char)
        continue

    if i == 0 and not (ord('A') <= ord(char) <= ord('Z')):  # Karakter pertama
        # Berarti huruf bukan huruf kecil maka besarkan
        kalimat_rapi_list.append(chr(ord(char) + BESARKAN_CHAR_INT))
        continue

    # Untuk yang bukan karakter pertama kecilkan semuanya
    if not (ord('a') <= ord(char) <= ord('z')):
        kalimat_rapi_list.append(chr(ord(char) + KECILKAN_CHAR_INT))
        continue

    # Untuk karakter yang sudah benar langsung ditambahkan saja
    kalimat_rapi_list.append(char)

kalimat_rapi_str = ''.join(kalimat_rapi_list)

print(kalimat_rapi_str)
