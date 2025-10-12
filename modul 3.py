'''
Michael Harvian
065002500011
latihan pertama
'''


a = float(input("Masukkan sisi pertama: "))
b = float(input("Masukkan sisi kedua: "))
c = float(input("Masukkan sisi ketiga: "))

   
if a + b <= c or a + c <= b or b + c <= a:
    print("Bukan segitiga")
elif a == b == c:
    print("Segitiga sama sisi")
elif a == b or b == c or a == c:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")


