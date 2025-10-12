# Michael Harvian
# 065002500011
# INSTRUKSI

import math

print("Silahkan isi latitude dan longitudenya untuk menentukan jarak antara 2 titik yang di cari:")

R = 6371  

negara1 = input("Masukkan Nama titik pertama permukaannya: ")
negara2 = input("Masukkan Nama titik kedua permukaannya: ")


lat1 = float(input("Masukan Latitude 1 = "))
lon1 = float(input("Masukan Longitude 1 = "))
lat2 = float(input("Masukan Latitude 2 = "))
lon2 = float(input("Masukan Longitude 2 = "))

lat1_rad = math.radians(lat1)
lon1_rad = math.radians(lon1)
lat2_rad = math.radians(lat2)
lon2_rad = math.radians(lon2)

dlon = lon2_rad - lon1_rad
dlat = lat2_rad - lat1_rad

a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
jarak = R * c

print(f"Jarak antara {negara1} dan {negara2} adalah {jarak} kilometer")
