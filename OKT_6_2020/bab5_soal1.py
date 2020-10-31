angka_input = list(map(int, input().split()))

# Bisa ditulis a, b, c = angka_input
a = angka_input[0]
b = angka_input[1]
c = angka_input[2]

if a % c == 0:
    if b % c == 0:
        print('a habis dibagi c dan b habis dibagi c')
    else:
        print('a habis dibagi c, tetapi b tidak habis dibagi c')
else:
    if b % c == 0:
        print('a tidak habis dibagi c, tetapi b habis dibagi c')
    else:
        print('a tidak habis dibagi c dan b tidak habis dibagi c')
