#Michael Harvian
#065002500011

print ("hitunglah luas ruangan!")

PR = float(input("masukkan panjang ruangan :"))
LR = float(input("masukkan lebar ruangan :"))
Satuan = input("pilihlah satuan (meter/inci) :")

if Satuan == "meter":
    Luas = PR * LR
    print(f"luas ruangan = {Luas}meter")

elif Satuan == "inci":
    Panjang_inci= PR * 39.3701
    Lebar_inci= LR * 39.3701
    Luas = Panjang_inci * Lebar_inci
    print(f"panjang dalam inci: {Panjang_inci:2f} inci")
    print(f"lebar dalam inci: {Lebar_inci:2f} inci")
    print(f"luas ruangan: {Luas:2f} inci")


