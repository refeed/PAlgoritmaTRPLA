'''

DESKRIPSI SOAL

Buatlah program untuk menghitung volume Bola

PETUNJUK MASUKAN

Input terdiri atas 1 buah angka yaitu jari-jari

PETUNJUK KELUARAN

Output terdiri dari 1 angka yang merupakan volume bola dengan pembulatan 2 angka
dibelakang koma

CONTOH MASUKAN

21

CONTOH KELUARAN

38808.0

CONTOH MASUKAN

10

CONTOH KELUARAN

4190.48

'''
PI = 22/7

ball_radius = int(input())

def calc_ball_volume(radius):
    return 4/3 * PI * (radius**3)

# If there are two trailing zeros, make it to one
result_str = '%.2f' % calc_ball_volume(ball_radius)

if result_str.endswith('.00'):
    result_str = result_str[0:-1]

print(result_str)
