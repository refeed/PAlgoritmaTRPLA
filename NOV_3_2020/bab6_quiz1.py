input_num = int(input())

is_prime = True

for i in range(2, input_num):
    if input_num % i == 0:
        is_prime = False
        break

if is_prime:
    print('PRIMA')
else:
    print('BUKAN PRIMA')
