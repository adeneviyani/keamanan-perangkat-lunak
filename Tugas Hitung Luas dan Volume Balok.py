# Tugas Hitung Luas dan Volume Balok
# Nama : Ade Neviyani
# Nim : 19051397018

from typing import ValuesView


print ("Menghitung Luas dan Volume Balok")

p = int(input("Masukkan Panjangnya  = "))
l = int(input("Masukkan Lebarnya  = "))
t = int(input("Masukkan Tingginya  = "))
if p <0 or 1 <0 or t <0 or t <0 :
    raise ValuesView

luas = (2*p*l)+(2*p*t)+(2*l*t)
volume = p*l*t

print("Luas Baloknya Adalah  = ", luas)
print("Volume Baloknya Adalah  = ", volume)