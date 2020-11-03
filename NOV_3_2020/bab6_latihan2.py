c_num = int(input())

a_num = 1
b_num = 1

# O(n**2)
while a_num < c_num:
    while b_num < c_num:
        if (a_num**2 + b_num**2) == c_num**2:
            print(a_num, b_num)
        b_num += 1
    b_num = 1
    a_num += 1

# Bisa pakai yang atas atau yang bawah
# O(n**2)
# for a in range(1, c_num):
#     for b in range(1, c_num):
#         if (a**2 + b**2) == c_num**2:
#             print(a, b)
