'''
Tulis program untuk fungsi (polinom) Chebysev.
Berapa nilai T(4,3)

T(4, 3) == 577
'''

def T(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return 2*x*T(n-1, x) - T(n-2, x)

print(T(4, 3))
