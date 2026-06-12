print(f'\nDATABASE OJOL')
print("===============")


databaseojol = []


namaojol = input("Masukan Nama Driver : ").upper()
rating_t = input("Masukan Total Rating : ").upper()

databasebaru = {
    "nama" : namaojol,
    "rating" : rating_t
}

databaseojol.append(databasebaru)

print('\n--- Data Terbaru OJOL (Per Hari Ini) ---'.upper())

for driverstat in databaseojol:
    nama = driverstat["nama"]
    rating = driverstat["rating"]
    print(f"\n NAMA : {nama} | rating : {rating}\n".upper())