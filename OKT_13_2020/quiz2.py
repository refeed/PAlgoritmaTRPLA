'''
2. Buatlah program menampilkan segitiga bintang :
A=3
*
**
*
'''

num_input = int(input())

for i in range(num_input, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# Bisa juga dengan
# for i in range(num_input, 0, -1):
#     print('*' * i)
