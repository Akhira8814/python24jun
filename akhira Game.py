#!/usr/bin/env python
import random
def main():
    print("Anda Mengenal Nombor Ganjil!")
nomborganjil = random.randint(11, 55)
teka = None 
while teka != nomborganjil:
    teka = int(input("Pilih satu nombor Ganjil:"))
    if teka % 2 == 0:
        print("SALAH,Pastikan anda masukkan nombor Ganjil")
    elif teka < 11 or teka > 55:
        print ("CUBA LAGI. Pastikan nombor yang dimasukkan nombor 11 hingga 55 sahaja")
    elif teka < nomborganjil:
        print ("Nombor Besar. Teka Lagi")
    elif teka > nomborganjil:
        print ("Nombor Kecil. Teka Lagi")
    else:
        print("TAHNIAH, ANDA TELAH BERJAYA MENEKA NOMBOR GANJIL")
main()