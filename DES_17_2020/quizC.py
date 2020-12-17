'''

DESKRIPSI SOAL

Buatlah program Penjumlahan angka pecahan (dan menyederhanakan) dengan format
penjumlahannya a / b + c / d = e / f

PETUNJUK MASUKAN

Input terdiri atas 4 buah angka yaitu a b c d

PETUNJUK KELUARAN

Output terdiri dari 2 buah angka yaitu e f

CONTOH MASUKAN

1 3 2 5

CONTOH KELUARAN

11 15

CONTOH MASUKAN

1 4 1 4

CONTOH KELUARAN

1 2

'''

a, b, c, d = list(map(int, input().split()))

e = a*d + c*b
f = b*d

def gcd(a, b):
    '''
    Find the greatest common divisor of two numbers.
    '''
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

# Simplify the fraction
greatest_common_divisor_ef = gcd(e, f)

# Because the result will always be an integer
# (a number can always be divided by its gcd)
# we use // instead of /, so that the return type is int, not float
# so we don't have to do any typecasting anymore
e = e // greatest_common_divisor_ef
f = f // greatest_common_divisor_ef

print(e, f)
