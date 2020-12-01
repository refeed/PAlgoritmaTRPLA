'''

DESKRIPSI SOAL

Petruk menuliskan sebuah bilangan n digit dengan tidak ada digit 0. Tiba-tiba,
Bagong menghampiri Petruk dan seketika membaca bilangan itu. Karena Bagong
sangat menyukai bilangan prima yang kurang dari 1000, dia penasaran ada berapa
banyak bilangan prima kurang dari 1000 yang muncul dalam bilangan yang ditulis
oleh Petruk. Perlu diperhatikan bahwa suatu bilangan prima dibentuk atas
digit-digit yang berurutan dari bilangan yang ditulis oleh Petruk.

Sebagai contoh, Petruk menuliskan bilangan 213672. Bilangan prima kurang dari
1000 yang bisa terbentuk adalah : 213672, 213672, 213672, 213672, 213672,
213672, 213672 ; terdapat 7 bilangan.

Karena merasa kesulitan, Bagong meminta bantuan Anda sebagai programmer handal
untuk membantunya.

PETUNJUK MASUKAN

Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan n (1 ≤ n ≤
10000) yang menyatakan banyak digit dari bilangan yang ditulis Petruk. Baris
kedua berisi sebuah bilangan dengan n digit yang merupakan bilangan yang ditulis
Petruk.


Outputkan sebuah bilangan bulat yang menyatakan jawaban dari pertanyaan Bagong.
CONTOH MASUKAN

6 213672

CONTOH KELUARAN

7
'''
import math


def is_prime(num_to_check):
    if num_to_check <= 1:
        return False

    prime = True
    for num in range(2, int(math.sqrt(num_to_check)) + 1):
        if num_to_check % num == 0:
            prime = False

    return prime


if __name__ == "__main__":
    num_length = int(input())
    number = input()

    primes_count = 0

    digit_to_process = 1

    while digit_to_process <= 3:
        for i in range(num_length):
            if (i + digit_to_process) > num_length:
                break
            if is_prime(int(number[i:i+digit_to_process])):
                primes_count += 1
        digit_to_process += 1

    print(primes_count)
