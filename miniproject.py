print(f'\n--- PUSAT DATABASE OJOL ---\n')

#database
databaseojol = []

#input
namaojol = input(f'masukan nama driver : '.upper())
while True:
    ratingtotal = input(f'masukan total rating : '.upper())
    if ratingtotal.isdigit() and int(ratingtotal) > 0:
        ratingtotal = int(ratingtotal)
        break
    else:
        print(f'masukan rating dengan benar'.upper())

while True:
    ordertotal = input(f'masukan total orderan : '.upper())
    if ordertotal.isdigit() and int(ordertotal) > 0:
        ordertotal = int(ordertotal)
        break
    else:
        print(f'masukan total order dengan benar!'.upper())

#calculation
avgrate = ratingtotal / ordertotal                          #variabel avgrate
ratingtotal = f"{avgrate:.2f}".upper()
if avgrate <0.0 or avgrate >5.0:
    bonusrate = "bonus tidak valid".upper()
elif avgrate >= 4.8:
    bonusrate = "bonus 40% pendapatan".upper()
elif avgrate >= 4.5:
    bonusrate = "bonus 20% pendapatan".upper()
elif avgrate >= 4.0:
    bonusrate = "tidak ada bonus".upper()
else:
    bonusrate = "akun anda dalam peringatan".upper()

#database
databaseojol2 = {
    "nama" : namaojol,
    "bonus" : bonusrate,
    "order" : ordertotal,
    "rating" : ratingtotal
}
databaseojol.append(databaseojol2)

#output
for driver in databaseojol:
    nama = driver["nama"]
    rating = driver["rating"]
    order = driver["order"]
    bonus = driver["bonus"]
    print(f'\n--- DATA OJOL HARI INI ---\n')
    print(f'nama : {nama}'.upper())
    print(f'rating : {rating}'.upper())
    print(f'bonus : {bonus}'.upper())
    print(f'\n ==== ==== ====')