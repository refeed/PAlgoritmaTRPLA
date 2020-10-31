# Ekspektasi input tiap baris: Nama Umur IPK
masukan = []
masukan.append(input())
masukan.append(input())
masukan.append(input())

umur = []
ipk = []

# Mengabaikan Nama karena tidak digunakan dalam perhitungan
masukan[0] = masukan[0].split()[1:]
masukan[1] = masukan[1].split()[1:]
masukan[2] = masukan[2].split()[1:]

# Konversi nilai elemen ke float
masukan[0] = list(map(float, masukan[0]))
masukan[1] = list(map(float, masukan[1]))
masukan[2] = list(map(float, masukan[2]))

umur.append(masukan[0][0])
umur.append(masukan[1][0])
umur.append(masukan[2][0])

ipk.append(masukan[0][1])
ipk.append(masukan[1][1])
ipk.append(masukan[2][1])

rerata_umur = (umur[0] + umur[1] + umur[2]) / 3
rerata_ipk = (ipk[0] + ipk[1] + ipk[2]) / 3

print(rerata_umur)
print(rerata_ipk)
