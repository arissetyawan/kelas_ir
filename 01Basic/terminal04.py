# -*- coding: utf-8 -*-
"""
@author: hends
"""

import os
from time import sleep

# bar judul dibuatkan function agar tidak berulang

def display_bar_title():
    os.system('cls')
    print ("\t********************************")
    print ("\t**        Salam - Halo!       **")
    print ("\t********************************")

# data nama yang akan diprint
nama = ['hendro','romi','slamet','ipul']


for teman in nama:
    display_bar_title()

    print ("\n\n")
    for x in range(0,5):
        print (teman.title())
    
    # pause 1 detik sebelum menampilkan nama berikutnya
    sleep(1)
    
    
