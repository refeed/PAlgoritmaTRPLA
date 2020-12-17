'''

DESKRIPSI SOAL

Diberikan sebuah fungsi f(n) dengan beberapa syarat berikut :

1. Jika n=0, maka f(n)=10.

2. Jika n lebih dari 0 dan n genap, maka f(n) = 4xf(n/2).

3. Jika n lebih dari 0 dan n ganjil, maka f(n) = f(n-1)+1.
PETUNJUK MASUKAN

Input terdiri atas 1 buah bilangan bulat n (0≤n≤200)
PETUNJUK KELUARAN

Outputkan sebuah bilangan bulat yang merupakan nilai dari f(n).
CONTOH MASUKAN 1

10

CONTOH KELUARAN 1

708

CONTOH MASUKAN 2

100

CONTOH KELUARAN 2

46096

'''

input_num = int(input())

def f(n):
    if n == 0:
        return 10
    if n % 2 == 0:
        return 4 * f(n/2)
    return f(n - 1) + 1

print(f(input_num))
