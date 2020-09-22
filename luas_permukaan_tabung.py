from math import pi


def luas_permukaan_tabung(r, t):
    luas_tutup = (pi * (r**2)) * 2
    luas_selimut = (pi * r * 2 * t)
    return luas_tutup + luas_selimut


print(luas_permukaan_tabung(10, 40))
