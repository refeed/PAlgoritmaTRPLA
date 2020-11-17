def terbesar(a, b, c):
    nilai_max = a

    for nilai in [b, c]:
        if nilai > nilai_max:
            nilai_max = nilai

    return nilai_max
