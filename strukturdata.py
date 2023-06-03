from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Sunflorist!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


class TokoBunga:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_bunga = {
            "Mawar": 5000,
            "Melati": 4000,
            "Anggrek": 6000,
            "Lily": 5500,
            "Tulip": 4500
        }

    def tampilkan_daftar_bunga(self):
        print("Daftar Bunga:")
        for nama, harga in self.daftar_bunga.items():
            print(f"- {nama}: Rp {harga}")

    def beli_bunga(self):
        self.tampilkan_daftar_bunga()
        print("Masukkan nama bunga yang ingin Anda beli:")
        nama_bunga = input()

        if nama_bunga in self.daftar_bunga:
            print("Masukkan jumlah bunga yang ingin Anda beli:")
            jumlah = int(input())

            harga_per_bunga = self.daftar_bunga[nama_bunga]
            total_harga = harga_per_bunga * jumlah
            print(f"Total harga: Rp {total_harga}")
        else:
            print("Bunga tidak tersedia.")

toko_bunga = TokoBunga("Toko Bunga XYZ")

print("Selamat datang di", toko_bunga.nama)
print("Apa yang ingin Anda lakukan?")
print("1. Tampilkan daftar bunga")
print("2. Beli bunga")

pilihan = int(input("Masukkan pilihan (1 atau 2): "))

if pilihan == 1:
    toko_bunga.tampilkan_daftar_bunga()
elif pilihan == 2:
    toko_bunga.beli_bunga()
else:
    print("Pilihan tidak valid.")
