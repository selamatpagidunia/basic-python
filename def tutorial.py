def rapihkannama(namamentah):
    namabersih = namamentah.strip()

    if namabersih == "":
        return "NAMA TIDAK BOLEH KOSONG"

    else:
        return namabersih.upper()


nama_user = input(f'masukan nama anda : '.upper())

test = rapihkannama(nama_user)

nama_resu = input(f'masukan nama anda : '.upper())

test1 = rapihkannama(nama_resu)

print(f'Nama User Pertama : {nama_user} > {test}')
print(f'Nama User Kedua : {nama_resu}  > {test1}')