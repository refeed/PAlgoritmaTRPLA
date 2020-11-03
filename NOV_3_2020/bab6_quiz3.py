input_n = int(input())

for i in range(input_n):
    if i == 0 or i == input_n-1:
        print('#' * input_n)
        continue

    print('#', end='')
    print(' ' * (input_n-2), end='')
    print('#')
