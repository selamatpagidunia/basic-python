print(f"Kantor Pengatur Payout/Bonus Driver Ojek Online".upper())
print(f"===============================================".upper())

databasedriver = [
    {"nama" : "Pak Marchel", "rating" : 4.8},
    {"nama" : "Pak Joko", "rating" : 4.4},
    {"nama" : "Pak Michael", "rating" : 3.5}
]

for datadriver in databasedriver:
    nama_driver = datadriver["nama"]
    rating_driver = datadriver["rating"]
    if rating_driver >= 4.8:
        status_rating = "dapat bonus super (70% pendapatan)".upper()
    elif rating_driver >= 4.5:
        status_rating = "dapat bonus standar (30% pendapatan)".upper()
    elif rating_driver >= 4.0:
        status_rating = "tidak dapat bonus".upper()
    else:
        status_rating = "rating sangat buruk!".upper()
    print(f"Nama Driver : {nama_driver} - Rata-rata Rating Driver : {rating_driver:.2f} - {status_rating}")