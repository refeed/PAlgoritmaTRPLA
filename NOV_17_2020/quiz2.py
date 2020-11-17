'''
No 2. Buatlah fungsi tanpa pengembalian nilai,  yaitu fungsi segitigabintang.
Misal, jika dipanggil dg segitigabintang(4), keluarannya :
*
**
***
****
'''

def segitigabintang(baris):
    for i in range(baris):
        print('*' * (i+1))
