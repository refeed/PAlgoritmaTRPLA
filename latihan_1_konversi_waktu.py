def jam_menit_detik_to_detik(jam, menit, detik):
    detik_jam = jam * 3600
    detik_menit = menit * 60
    return detik_jam + detik_menit + detik


print(jam_menit_detik_to_detik(1, 10, 15))
