#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : snmp_modul.py
Tujuan    : Melakukan pengecekan perangkat menggunakan SNMPv2c
            dan mengambil nilai sysName.
Pembuat   : Aulia Natasya
NIM       : 2409106084
"""

import asyncio

from pysnmp.hlapi.v3arch.asyncio import (
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    get_cmd
)


# ==========================================
# KONFIGURASI SNMP
# ==========================================

HOST = "192.168.3.76"
PORT = 161
COMMUNITY = "comm_084"


# ==========================================
# FUNCTION CEK SNMP
# ==========================================

def cek_snmp():
    """
    Mengambil nilai sysName perangkat menggunakan SNMPv2c.
    """

    print("==========================================")
    print("         PEMERIKSAAN KONEKSI SNMP")
    print("==========================================")
    print("Host      :", HOST)
    print("Port      :", PORT)
    print("Community :", COMMUNITY)
    print()

    try:

        # ==========================================
        # OID SYSNAME
        # ==========================================

        oid_sysname = "1.3.6.1.2.1.1.5.0"

        # Menjalankan permintaan SNMP GET
        hasil = asyncio.run(
            permintaan_snmp(oid_sysname)
        )

        return hasil

    except Exception as error:

        print("Status   : Gagal")
        print("Kesalahan:", error)

        return {
            "status": "gagal",
            "pesan": str(error)
        }


# ==========================================
# FUNCTION PERMINTAAN SNMP
# ==========================================

async def permintaan_snmp(oid_sysname):
    """
    Mengirim permintaan SNMP GET ke perangkat.
    """

    # Membuat target perangkat SNMP
    transport = await UdpTransportTarget.create(
        (HOST, PORT),
        timeout=5,
        retries=1
    )

    # Mengirim permintaan SNMP GET
    error_indication, error_status, error_index, var_binds = await get_cmd(
        SnmpEngine(),
        CommunityData(COMMUNITY, mpModel=1),
        transport,
        ContextData(),
        ObjectType(
            ObjectIdentity(oid_sysname)
        )
    )

    # ==========================================
    # PEMERIKSAAN ERROR
    # ==========================================

    if error_indication:

        print("Status   : Gagal")
        print("Kesalahan:", error_indication)

        return {
            "status": "gagal",
            "pesan": str(error_indication)
        }

    elif error_status:

        print("Status   : Gagal")
        print("Kesalahan:", error_status.prettyPrint())

        return {
            "status": "gagal",
            "pesan": error_status.prettyPrint()
        }

    else:

        for var_bind in var_binds:

            hasil_sysname = var_bind[1].prettyPrint()

            print("Status   : Koneksi SNMP berhasil")
            print("OID      :", oid_sysname)
            print("sysName  :", hasil_sysname)

            return {
                "status": "berhasil",
                "sysName": hasil_sysname
            }


# ==========================================
# PROGRAM UTAMA
# ==========================================

if __name__ == "__main__":
    cek_snmp()