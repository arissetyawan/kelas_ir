# -*- coding: utf-8 -*-
"""
@author: hends
"""

import os
import pickle

### FUNCTIONS ###

# bar judul dibuatkan function agar tidak berulang
def display_bar_title():
    os.system('cls')
    print ("\t********************************")
    print ("\t**   Simple Search Engine     **")
    print ("\t********************************")
    
def get_user_input():
    print ("\n")
    print ("[1] Tambahkan konten/dokumen")
    print ("[2] Lihat daftar dokumen")
    print ("[3] Lihat konten dokumen")
    print ("[4] Edit konten dokumen")
    print ("[5] Delete dokumen dengan nomor index")
    print ("[6] Delete dokumen yang mengandung kata")
    print ("[b] Save/Backup daftar dokumen ke file.")
    print ("[q] Keluar.")

    return raw_input("\nMasukkan pilihanmu: ")
    
def print_uc():
    print ("\nMaaf belum dibuat. Tugas kalian membuatnya")

def print_separator():
    print ("-----------------------------------------------")
        
def se_add_doc():
    print ("\nMasukkan konten dokumen, akhiri dengan ENTER.")
    print_separator()
    konten = raw_input()
    if len(konten) == 0:
        print_separator()
        raw_input("\nKonten kosong, ENTER kembali ke menu.")
    else:
        docs.append(konten)
        print_separator()
        raw_input("\nKonten telah berhasil ditambahkan. ENTER kembali ke menu.")

def se_list_docs():
    print ("\nDaftar dokumen")
    print_separator()
    print ("index\tkonten")
    print_separator()
    for i, d in enumerate(docs):
        print ("%d\t%s" % (i, d) )
    print_separator()
    
def se_show_doc():
    i_max = len(docs) - 1
    i = raw_input("Masukkan nomor index dokumen [0-%d]: " % i_max)
    print_separator()
    print (docs[ int(i) ])
    print_separator()
    
def se_loaddb(datafile):
    try:
        file_object = open(datafile, 'rb')
        data = pickle.load(file_object)
        file_object.close()
    except:
        data = []
        
    return data
        
def se_savedb(data):
    try:
        file_object = open(datafile, 'wb')
        pickle.dump(data, file_object)
        file_object.close()
    except Exception as e:
        print(e)
        print("\nMaaf gagal simpan data dokumen. Sorry.")   

### MAIN PROGRAM ###

datafile = 'searchengine.pydata'
docs = se_loaddb(datafile)

pilihan = ""
display_bar_title()

while pilihan != "q":
    
    # Beri pengguna kesempatan memilih perintah
    pilihan = get_user_input()
    
    # Respon 
    display_bar_title()
    if str(pilihan) == "1":
        se_add_doc()
    elif str(pilihan) == "2":
        se_list_docs()
    elif str(pilihan) == "3":
        se_show_doc()
    elif str(pilihan) == "4":
        print_uc()
    elif str(pilihan) == "5":
        print_uc()
    elif str(pilihan) == "6":
        print_uc()
    elif pilihan == "b":
        se_savedb(docs)
    elif pilihan == "q":
        simpan = raw_input("\nSimpan data sebelum kelular [Y/n]: ")
        if (simpan == "n"):
            print (".")
        else:
            se_savedb(docs)
            
        print ("\nOkeh terima kasih. Sampai jumpa.")
    else:
        print ("\nAku gak ngerti kamu")        
        