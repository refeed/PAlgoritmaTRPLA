'''

DESKRIPSI SOAL

Dalam matematika, bilangan Fibonacci adalah barisan yang didefinisikan secara
rekursif sebagai berikut: Penjelasan: barisan ini berawal dari 1 dan 1, kemudian
angka berikutnya didapat dengan cara menambahkan kedua bilangan yang berurutan
sebelumnya.

Contoh baris Fibonacci adalah 1,1,2,3,5,8,13, ... dst

Buatlah program yang menghasilkan angka yang merupakan suku ke-N, dengan N
merupakan input dari pengguna

PETUNJUK MASUKAN

Input terdiri atas 1 buah angka yaitu N

PETUNJUK KELUARAN

Output terdiri dari 1 angka yang merupakan angka yang merupakan suku ke-N

CONTOH
MASUKAN

10

CONTOH KELUARAN

55

CONTOH MASUKAN

7

CONTOH KELUARAN

13

'''

num_input = int(input())


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(num_input))
