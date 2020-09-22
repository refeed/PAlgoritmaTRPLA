detik_input = int(input())

jam = detik_input // 3600
detik_input -= jam * 3600

menit = detik_input // 60
detik_input -= menit * 60

detik = detik_input

print(jam)
print(menit)
print(detik)
