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

for x in range(0,10):
    print ("\nKita telah bersenang2 bersama %d kali" % x)
    
# berhenti 3 detik, untuk menunda tampilan berikutnya
sleep(3)

print ("Hai! Aku kembali")