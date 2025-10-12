'''
Michael Harvian
065002500011
latihan kedua modul 3
'''

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
total_belanja = int(input("Masukkan total belanja: Rp "))

kupon = input("Masukkan kode kupon (jika ada): ")

if kupon == "IKL6309":
    print("Selamat, anda mendapatkan diskon 100%.")
    diskon = 1.0
    potongan = total_belanja
    bayar = 0
else:
    if 40000 <= total_belanja <= 89999:
        diskon = 0.2
    elif 90000 <= total_belanja <= 189999:
        diskon = 0.4
    elif 190000 <= total_belanja <= 389999:
        diskon = 0.6
    elif total_belanja >= 390000:
        diskon = 0.8
    else:
        diskon = 0.0

    potongan = total_belanja * diskon
    bayar = total_belanja - potongan

print(f"Total Belanja : Rp {total_belanja}")
print(f"Diskon        : {int(diskon*100)}%")
print(f"Potongan      : Rp {int(potongan)}")
print(f"Total Bayar   : Rp {int(bayar)}")

print("terima kasih sudah berbelanja")

