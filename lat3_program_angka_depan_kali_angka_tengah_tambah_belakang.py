nomor = int(input('Masukan angka: '))

ratusan = nomor // 100
puluhan = nomor // 10 % 10
satuan = nomor % 10

hasil = ratusan * puluhan + satuan

print(hasil)
