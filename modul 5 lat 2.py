#michael harvian
#065002500011

total = 0.0
usia = "0"

while True:
    usia = input("masukkan umur: ")
    if usia == "":
        break  

    umur = int(usia)

    if umur <= 2:
        harga = 0
        print("Gratis")
    elif umur >= 3 and umur <= 12:
        harga = 14
        print("Harga $14.00")
    elif umur >= 65:
        harga = 18
        print("Harga $18.00")
    else:
        harga = 23
        print("Harga $23.00")

    total += harga
    print(f"Running total: {total:.2f}")

uang = float(input("masukkan jumlah uang: "))
kembalian = uang - total
print(f"Running kembalian: {kembalian:.2f}")
