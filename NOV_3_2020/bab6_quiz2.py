input_n = int(input())

# for i in range(input_n):
#     print('#' * input_n)

# Bisa pakai yang bawah atau yang atas
for _ in range(input_n):
    for _ in range(input_n):
        print('#', end='')
    print()
