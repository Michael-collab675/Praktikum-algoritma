#michael harvian
#065002500011
#modul ke 6 lat 2

def kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)


def jumlah_hari(bulan, tahun=2024):
    if bulan == 2:
        if kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return 0


print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
print("Masukkan 0 untuk menghentikan program")

while True:
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan == 0:
        print("Terima kasih.")
        break

  
    if bulan == 2:
        tahun = int(input("Masukkan tahun (e.g., 2021): "))
        print(jumlah_hari(bulan, tahun), "hari dalam sebulan\n")
    else:
        print(jumlah_hari(bulan), "hari dalam sebulan\n")
