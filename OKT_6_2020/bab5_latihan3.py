angka_input = list(map(int, input().split()))

# Bisa ditulis a, b, c = angka_input
a = angka_input[0]
b = angka_input[1]
c = angka_input[2]

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)
