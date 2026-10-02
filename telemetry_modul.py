#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : telemetry_modul.py
Tujuan    : Menganalisis data telemetry CPU dan
            mengklasifikasikan penggunaan CPU.
Pembuat   : Aulia Natasya
NIM       : 2409106084
"""


# ==========================================
# DATA SAMPLE TELEMETRY
# ==========================================

data_telemetry = {
    "sample_1": {
        "cpuUsage": 40
    },

    "sample_2": {
        "cpuUsage": 64
    },

    "sample_3": {
        "cpuUsage": 84
    }
}


# ==========================================
# FUNCTION KLASIFIKASI TELEMETRY
# ==========================================

def klasifikasi_telemetry():
    """
    Mengklasifikasikan penggunaan CPU berdasarkan
    nilai cpuUsage.
    """

    hasil = {}

    # Melakukan iterasi pada setiap data telemetry
    for nama_sample, data in data_telemetry.items():

        cpu = data["cpuUsage"]

        # ==========================================
        # KLASIFIKASI DATA
        # ==========================================

        if cpu > 80:
            kategori = "KRITIS"

        elif cpu >= 50:
            kategori = "WASPADA"

        else:
            kategori = "NORMAL"

        hasil[nama_sample] = {
            "cpuUsage": cpu,
            "kategori": kategori
        }

        print(
            nama_sample,
            "-> CPU:",
            cpu,
            "%",
            "| Status:",
            kategori
        )

    return hasil


# ==========================================
# PROGRAM UTAMA
# ==========================================

if __name__ == "__main__":

    print("==========================================")
    print("       ANALISIS DATA TELEMETRY")
    print("==========================================")

    klasifikasi_telemetry()