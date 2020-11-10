input_n = int(input())

list_l = list(range(input_n))

print('List L (awal) = ', list_l)

average = sum(list_l)/len(list_l)

list_k = []
list_m = []

while len(list_l) != 0:
    value = list_l.pop()

    if value <= average:
        list_k.append(value)
    else:
        list_m.append(value)

print('List L (akhir) = ', list_l)
print('List K = ', list_k)
print('List M = ', list_m)
