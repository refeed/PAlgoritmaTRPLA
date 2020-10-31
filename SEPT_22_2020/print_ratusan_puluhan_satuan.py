nomor = int(input('Masukkan angka: '))
ratusan = nomor // 100
puluhan = nomor // 10 % 10
satuan = nomor % 10

print(ratusan, 'ratusan')
print(puluhan, 'puluhan')
print(satuan, 'satuan')
