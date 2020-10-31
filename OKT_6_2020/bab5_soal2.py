angka_input = list(map(int, input().split()))

# Bisa ditulis a, b, c = angka_input
nilai1 = angka_input[0]
nilai2 = angka_input[1]
nilai3 = angka_input[2]

rata_rata = (nilai1 + nilai2 + nilai3) / 3

if rata_rata > 50 and nilai1 > 40 and nilai2 > 40 and nilai3 > 40:
    print('lulus')
else:
    print('tidak lulus')
