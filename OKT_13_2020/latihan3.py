input_nums = list(map(int, input().split()))

is_prima = True
check_num = input_nums[0] + input_nums[1]

for num in range(2, check_num):
    if check_num % num == 0:
        is_prima = False
        break

if is_prima:
    print('prima')
else:
    print('bukan prima')
