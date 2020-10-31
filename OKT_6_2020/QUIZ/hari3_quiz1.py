'''
Soal Bab 5 Quiz modul nomor 2

- Hanya boleh melakukan percabangan dan semua materi yang dipelajari di kelas
'''

angka_input = list(map(int, input().split()))

# Bisa ditulis a, b, c = angka_input
a = angka_input[0]
b = angka_input[1]
c = angka_input[2]

if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > c:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if a > b:
        print(a)
    else:
        print(b)
