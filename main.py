#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : main.py
Tujuan    : Mengintegrasikan seluruh modul UTS Jaringan Komputer Lanjut
Pembuat   : Aulia Natasya
NIM       : 2409106084
"""

import identitas
import ssh_modul
import snmp_modul
import netconf_modul
import telemetry_modul


class LaporanCabang:

    def tampilkan_laporan(
        self,
        hasil_ssh,
        hasil_snmp,
        pesan_netconf,
        hasil_telemetry
    ):
        print()
        print("==========================================")
        print("          LAPORAN AKHIR CABANG")
        print("==========================================")
        print()

        # ==========================================
        # IDENTITAS CABANG
        # ==========================================
        print("IDENTITAS CABANG")
        print("Nama         :", identitas.nama)
        print("NIM          :", identitas.nim)
        print("Kode Cabang  :", identitas.kode_cabang)
        print(
            "ID Perangkat :",
            identitas.buat_id_perangkat("router", 1)
        )
        print()

        # ==========================================
        # HASIL SSH
        # ==========================================
        print("HASIL SSH")
        print("Status       :", hasil_ssh["status"])
        print("Hostname     :", hasil_ssh["hostname"])
        print("Uptime       :", hasil_ssh["uptime"])
        print()

        # ==========================================
        # HASIL SNMP
        # ==========================================
        print("HASIL SNMP")
        print("Status       :", hasil_snmp["status"])
        print("OID          : 1.3.6.1.2.1.1.5.0")
        print("sysName      :", hasil_snmp["sysName"])
        print()

        # ==========================================
        # HASIL NETCONF
        # ==========================================
        print("HASIL NETCONF")
        print(pesan_netconf)
        print()

        # ==========================================
        # HASIL TELEMETRY
        # ==========================================
        print("HASIL TELEMETRY")

        for nama_sample, data in hasil_telemetry.items():
            print(
                nama_sample,
                "-> CPU:",
                data["cpuUsage"],
                "%",
                "| Status:",
                data["kategori"]
            )

        print()
        print("==========================================")
        print("        INTEGRASI SELESAI")
        print("==========================================")


def main():

    print("==========================================")
    print("     INTEGRASI SISTEM JARINGAN")
    print("==========================================")
    print()

    # ==========================================
    # 1. MENJALANKAN MODUL SSH
    # ==========================================
    hasil_ssh = ssh_modul.cek_ssh()

    # ==========================================
    # 2. MENJALANKAN MODUL SNMP
    # ==========================================
    hasil_snmp = snmp_modul.cek_snmp()

    # ==========================================
    # 3. MEMBUAT PESAN NETCONF
    # ==========================================
    pesan_netconf = netconf_modul.buat_pesan_netconf()

    # ==========================================
    # 4. MENJALANKAN ANALISIS TELEMETRY
    # ==========================================
    hasil_telemetry = telemetry_modul.klasifikasi_telemetry()

    # ==========================================
    # 5. MENAMPILKAN LAPORAN AKHIR
    # ==========================================
    laporan = LaporanCabang()

    laporan.tampilkan_laporan(
        hasil_ssh,
        hasil_snmp,
        pesan_netconf,
        hasil_telemetry
    )


if __name__ == "__main__":
    main()