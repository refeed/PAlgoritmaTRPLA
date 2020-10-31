harga = int(input())
diskon = int(input())

harus_bayar = harga - (harga * diskon / 100)

if harus_bayar % 1000 != 0:  # kalau harus bayar tidak habis dibagi 1000
    pembulatan = ((harus_bayar // 1000) + 1) * 1000
else:
    pembulatan = harus_bayar

print(int(pembulatan))

