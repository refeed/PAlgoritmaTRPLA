'''

DESKRIPSI SOAL

Rumus pitagoras untuk menghitung sisi miring segitiga siku-siku adalah a2 + b2 =
c2.

Diberikan 3 buah angka, cari tahu, apakah kombinasi dari 3 angka tersebut
membentuk Segitiga Siku-siku atau tidak

PETUNJUK MASUKAN

Input terdiri atas 3 buah angka yaitu a b c

PETUNJUK KELUARAN

Output terdiri dari 1 buah string yang menandakan pitagoras atau bukan

CONTOH MASUKAN

3 5 4

CONTOH KELUARAN

pitagoras

CONTOH MASUKAN

10 10 10

CONTOH KELUARAN

bukan

'''

input_num_list = list(map(int, input().split()))

def pytaghoras_check(a, b, c):
    # c has to be the maximum number
    if (a**2 + b**2) == c**2:
        return True
    return False

max_index = 0
max_value = input_num_list[max_index]

for i in range(1, len(input_num_list)):
    if input_num_list[i] > max_value:
        max_value = input_num_list[i]
        max_index = i

input_num_list.pop(max_index)

if pytaghoras_check(input_num_list[0], input_num_list[1], max_value):
    print('pitagoras')
else:
    print('bukan')
