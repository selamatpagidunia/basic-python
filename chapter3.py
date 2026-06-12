#TITLE : Aplikasi Rating Driver Ojek Online
print(f"Aplikasi Rating DRIVER OJEK ONLINE".upper())
print(f"=========================================".upper())

#input phase
while True:
    jumlahrating_input = input("Masukan Rating Driver : ".upper())
    if jumlahrating_input.isdigit():
        jumlahrating = float(jumlahrating_input)
        break
    else:
        print("Rating Driver harus berupa angka .".upper())

while True:
    orderandriver = input("Masukan jumlah orderan driver : ".upper())
    if orderandriver.isdigit() and int(orderandriver) >= 1:
        orderandriver = int(orderandriver)
        break
    else:
        print("Jumlah orderan driver harus berupa angka yang lebih besar dari 0 .".upper())

rata_rata_rating = jumlahrating / orderandriver

#validation phase
if rata_rata_rating <0.0 or rata_rata_rating >5.0:
    print("rating tidak valid".upper())
    exit()
elif rata_rata_rating >= 4.8:
    status_rating = "dapat bonus super (70% pendapatan)".upper()
elif rata_rata_rating >= 4.5:
    status_rating = "dapat bonus standar (30% pendapatan)".upper()
elif rata_rata_rating >= 4.0:
    status_rating = "tidak dapat bonus ".upper()
elif rata_rata_rating <4.0:
    status_rating = "peringatan akun driver!".upper()
else:
    status_rating = "rating tidak valid".upper()
    exit()

#output phase
print(f"Rata-rata Rating Driver : {rata_rata_rating:.2f} - {status_rating}".upper())