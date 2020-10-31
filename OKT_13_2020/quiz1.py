'''
1. Buatlah program membaca bil A.  Lalu menampilkan bil prima terbesar yg lebih
   kecil dr A.
Kl 2, outputnya : tdk ada bil prima yg lebih kecil dr 2
'''

num_input = int(input())

if num_input <= 2:
    print('Tidak ada bilangan prima yangg lebih kecil dari 2')
else:
    for num in range(num_input-1, 1, -1):
        apakah_prima = True

        for i in range(2, num):
            if num % i == 0:
                apakah_prima = False
                break

        if apakah_prima:
            print(num)
            break
