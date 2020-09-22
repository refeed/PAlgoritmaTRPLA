import math

harga = int(input())
diskon = int(input())

harus_bayar = harga - (harga * diskon / 100)
pembulatan = math.ceil(harus_bayar / 1000) * 1000

print(pembulatan)
