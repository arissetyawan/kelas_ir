# -*- coding: utf-8 -*-
"""
@author: hends
"""

import os
from time import sleep

### FUNCTIONS ###

# bar judul dibuatkan function agar tidak berulang
def display_bar_title():
    os.system('cls')
    print ("\t********************************")
    print ("\t**   Warung Sebelah - Halo!   **")
    print ("\t********************************")

### MAIN PROGRAM ###

pilihan = ""
display_bar_title()

while pilihan != "q":
    
    # Beri pengguna kesempatan memilih perintah
    print ("\n")
    print ("[1] Lihat menu")
    print ("[2] Sesuatu ...")
    print ("[q] Keluar.")

    pilihan = raw_input("\nMasukkan pilihanmu: ")
    
    # Respon 
    display_bar_title()
    if str(pilihan) == "1":
        print ("\nBakso\nSoto\nMie Ayam")
    elif str(pilihan) == "2":
        print ("\nTiada ada pilihan lain...")
    elif pilihan == "q":
        print ("\nOkeh terima kasih. Sampai jumpa.")
    else:
        print ("\nAku gak ngerti kamu")        
        