#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : netconf_modul.py
Tujuan    : Membuat pesan XML NETCONF untuk konfigurasi VLAN.
Pembuat   : Aulia Natasya
NIM       : 2409106084
"""

import xml.etree.ElementTree as ET


# ==========================================
# KONFIGURASI
# ==========================================

KODE_CABANG = "084"


# ==========================================
# FUNCTION BUAT PESAN NETCONF
# ==========================================

def buat_pesan_netconf():
    """
    Membuat pesan XML NETCONF untuk membuat VLAN.
    """

    # ==========================================
    # MESSAGES LAYER
    # ==========================================
    # Membuat elemen <rpc> sebagai pembungkus
    # pesan NETCONF.

    rpc = ET.Element(
        "rpc",
        {
            "message-id": "101",
            "xmlns": "urn:ietf:params:xml:ns:netconf:base:1.0"
        }
    )

    # ==========================================
    # OPERATIONS LAYER
    # ==========================================
    # Membuat operasi <edit-config>.

    edit_config = ET.SubElement(
        rpc,
        "edit-config"
    )

    # ==========================================
    # OPERATIONS LAYER
    # ==========================================
    # Menentukan target konfigurasi.
    
    target = ET.SubElement(
        edit_config,
        "target"
    )

    running = ET.SubElement(
        target,
        "running"
    )

    # ==========================================
    # CONTENT LAYER
    # ==========================================
    # Membuat bagian <config> yang berisi
    # konfigurasi VLAN.

    config = ET.SubElement(
        edit_config,
        "config"
    )

    vlan = ET.SubElement(
        config,
        "vlan"
    )

    vlan_id = ET.SubElement(
        vlan,
        "id"
    )

    vlan_id.text = KODE_CABANG

    vlan_name = ET.SubElement(
        vlan,
        "name"
    )

    vlan_name.text = "VLAN_" + KODE_CABANG

    # ==========================================
    # MENGUBAH MENJADI STRING XML
    # ==========================================

    ET.indent(rpc, space="    ")

    pesan_xml = ET.tostring(
        rpc,
        encoding="unicode"
    )

    return pesan_xml


# ==========================================
# PROGRAM UTAMA
# ==========================================

if __name__ == "__main__":

    pesan = buat_pesan_netconf()

    print("==========================================")
    print("       PEMBUATAN PESAN NETCONF")
    print("==========================================")
    print()

    print(pesan)