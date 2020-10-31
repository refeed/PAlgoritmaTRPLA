angka_ratusan = int(input())

ratusan = angka_ratusan // 100
puluhan = angka_ratusan // 10 % 10
satuan = angka_ratusan % 10

print(ratusan + puluhan + satuan)
