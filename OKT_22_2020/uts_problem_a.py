"""
Dua buah bilangan bulat X dan Y. X merupakan panjang sisi kubus kecil dalam
centimeter. Dan Y adalah banyak kubus kecil yang menyusun panjang sisi kubus
besar.(1 ≤ X,Y ≤ 100)
"""

x, y = list(map(int, input().split()))

volume = (x*y)**3

print(volume)
