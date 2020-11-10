input_str = input()

sum_capital = 0

for char in input_str:
    if ord('A') <= ord(char) <= ord('Z'):
        sum_capital += 1

print(sum_capital)
