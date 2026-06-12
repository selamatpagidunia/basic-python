print(f"SISTEM FUNGSI OTOMATIS OJEK ONLINE".upper())
print(f"===============================================".upper())

while True:
    rating_driver = input('masukan jumlah rating : '.upper())
    if rating_driver.isdigit() and int(rating_driver) > 0:
        rating_driver = int(rating_driver)
        break
    else:
        print(f'masukan angka dengan benar'.upper())


while True:
    orderan = input('masukan jumlah orderan : '.upper())
    if orderan.isdigit() and int(orderan) > 1:
        orderan = int(orderan)
        break
    else:
        print('masukan jumlah orderan dengan benar! '.upper())

kalkulasi = rating_driver / orderan
r = f'{kalkulasi:.2f}'

def cek_status(kalkulasi):
    if kalkulasi >= 4.8:
        return "dapat bonus 70% pendapatan".upper()
    elif kalkulasi >= 4.5:
        return "dapat bonus 30% pendapatan".upper()
    elif kalkulasi >= 4.0:
        return "driver tidak dapat bonus".upper()
    else:
        return "akun sangat buruk".upper()

print(f'\nrating driver a: {r}'.upper())
print(f"status driver a: {cek_status(kalkulasi)}".upper())