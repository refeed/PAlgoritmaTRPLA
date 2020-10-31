# Nomor pertama batas atasnya, nomor kedua bilangan b
input_nums = list(map(int, input().split()))

for i in range(1, input_nums[0] + 1):
    if i % input_nums[1] == 0:
        print(i)
