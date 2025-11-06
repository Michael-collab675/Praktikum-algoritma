#michael harvian
#065002500011
#latihan pertama

def konversi(huruf='A'):
    if huruf == 'A':
        return 4
    elif huruf == 'B':
        return 3
    elif huruf == 'C':
        return 2
    elif huruf == 'D':
        return 1
    else:
        return 0

def rata_rata(n1, n2):
    return (n1 + n2) / 2

h1 = input("Masukkan huruf: ").upper()
n1 = konversi(h1)
print("Nilai =", n1)

h2 = input("Masukkan huruf: ").upper()
n2 = konversi(h2)
print("Nilai =", n2)

print("Rata-ratanya adalah:", rata_rata(n1,n2))
