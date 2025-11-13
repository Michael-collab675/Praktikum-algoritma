#Michael Harvian
#065002500011

def cek_prima(angka):
    if angka <= 1:
        return False
    if angka == 2:
        return True

    for i in range(2, angka):
        if angka % i == 0:
            return False
    return True


def tampil_hasil_prima(angka, status_prima):
    if status_prima:
        print(f"{angka} adalah bilangan Prima")
    else:
        print(f"{angka} bukanlah bilangan Prima")

angka_input = int(input("Masukkan angka: "))
status = cek_prima(angka_input)
tampil_hasil_prima(angka_input,status)

