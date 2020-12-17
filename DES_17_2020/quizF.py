'''

DESKRIPSI SOAL

Buat program untuk merapikan tulisan nama variable (pakai camelcase). Program
menerima input sebuah string yang terdiri dari huruf kapital atau pun
non-kapital dan juga spasi. Outputkan sebuah string sesuai aturan penuliasan
variable (camelcase) dengan karakter pertamanya merupakan huruf bukan
kapital,spasi dihilangkan dan sisanya bukan kapital kecuali huruf setelah spasi
menjadi Kapital.

PETUNJUK MASUKAN

Input terdiri atas 1 buah string

PETUNJUK KELUARAN

Output terdiri dari 1 buah string camelcase

CONTOH MASUKAN

luAs lINKaRan

CONTOH KELUARAN

luasLingkaran

CONTOH MASUKAN

jaRi jaRI lingKaRAn

CONTOH KELUARAN

jariJariLingkaran

'''
# This program assumes that there's no strange characters but
# normal alphabets

word_list = input().split()

ASCII_SMALL_CHAR_OFFSET = ord('a')
ASCII_CAPITALIZED_CHAR_OFFSET = ord('A')
ASCII_CAPITALIZE_CHAR = ASCII_CAPITALIZED_CHAR_OFFSET - ASCII_SMALL_CHAR_OFFSET

def is_capitalized(char):
    return ASCII_CAPITALIZED_CHAR_OFFSET <= ord(char) <= (ASCII_CAPITALIZED_CHAR_OFFSET + 26)

def capitalize_char(char):
    if is_capitalized(char):
        return char
    return chr(ord(char) + ASCII_CAPITALIZE_CHAR)

def small_ize_char(char):
    if not is_capitalized(char):
        return char
    return chr(ord(char) - ASCII_CAPITALIZE_CHAR)

# Camel case
new_char_list = []
for word_i, word in enumerate(word_list):
    for char_i, char in enumerate(word):
        if word_i >= 1 and char_i == 0:
            new_char_list.append(capitalize_char(char))
            continue
        new_char_list.append(small_ize_char(char))

print(''.join(new_char_list))
