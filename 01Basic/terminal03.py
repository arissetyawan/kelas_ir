# -*- coding: utf-8 -*-
"""
@author: hends
"""

import os
from time import sleep

# Tampilkan bar judul

print ("\t********************************")
print ("\t**        Salam - Halo!       **")
print ("\t********************************")

# data nama yang akan diprint
nama = ['hendro','romi','slamet','ipul']

for teman in nama:
    # bersihkan layar dulu
    os.system('cls')
    
    # tampilkan judul
    print ("\t********************************")
    print ("\t**        Salam - Halo!       **")
    print ("\t********************************")

    print ("\n\n")
    for x in range(0,5):
        print (teman.title())
    
    # pause 1 detik sebelum menampilkan nama berikutnya
    sleep(1)
    
    
