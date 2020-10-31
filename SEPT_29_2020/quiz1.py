# Konversi bilangan biner 4 bit ke bilangan desimal

s = input()  # Ekspektasi: str bilangan 4 bit

input_int_list = list(map(int, s))

hasil = (input_int_list[0] * 8 +
         input_int_list[1] * 4 +
         input_int_list[2] * 2 +
         input_int_list[3] * 1)

print(hasil)
