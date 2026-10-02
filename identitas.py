
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : identitas.py
Tujuan    : Mengelola identitas kantor cabang
Pembuat   : Aulia Natasya
NIM       : 2409106084
"""

nim = "2409106084"
nama = "Aulia Natasya"
kode_cabang = nim[-3:]


def buat_id_perangkat(jenis, nomor):
    """Membuat ID perangkat berdasarkan cabang, jenis, dan nomor."""
    return f"CB{kode_cabang}-{jenis.upper()}-{nomor:03d}"


if __name__ == "__main__":
    print("Nama         :", nama)
    print("NIM          :", nim)
    print("Kode Cabang  :", kode_cabang)
    print("ID Perangkat :", buat_id_perangkat("router", 1))