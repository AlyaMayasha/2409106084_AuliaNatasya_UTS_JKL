#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File : ssh_modul.py
Tujuan    : Melakukan pengecekan koneksi SSH dan menjalankan
            perintah diagnostik pada perangkat jaringan.
Pembuat   : Aulia Natasya
NIM       : 2409106084
"""

import paramiko


# ==========================================
# KONFIGURASI SSH
# ==========================================

HOST = "192.168.3.76"
PORT = 22
USERNAME = "admin_084"
PASSWORD = "ssanjook"


# ==========================================
# FUNCTION CEK SSH
# ==========================================

def cek_ssh():
    """
    Menghubungkan program ke perangkat melalui SSH,
    menjalankan dua perintah diagnostik, dan mencetak hasilnya.
    """

    client = paramiko.SSHClient()

    # Menerima host key secara otomatis untuk kebutuhan pengujian
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print("==========================================")
        print("         PEMERIKSAAN KONEKSI SSH")
        print("==========================================")
        print("Host     :", HOST)
        print("Port     :", PORT)
        print("Username :", USERNAME)
        print()

        # Membuka koneksi SSH
        client.connect(
            hostname=HOST,
            port=PORT,
            username=USERNAME,
            password=PASSWORD,
            timeout=10
        )

        print("Status   : Koneksi SSH berhasil")
        print()

        # ==========================================
        # PERINTAH DIAGNOSTIK 1
        # ==========================================

        stdin, stdout, stderr = client.exec_command("hostname")

        hasil_hostname = stdout.read().decode("utf-8").strip()

        print("Perintah 1 : hostname")
        print("Hasil      :", hasil_hostname)
        print()

        # ==========================================
        # PERINTAH DIAGNOSTIK 2
        # ==========================================

        stdin, stdout, stderr = client.exec_command("uptime")

        hasil_uptime = stdout.read().decode("utf-8").strip()

        print("Perintah 2 : uptime")
        print("Hasil      :", hasil_uptime)
        print()

        return {
            "status": "berhasil",
            "hostname": hasil_hostname,
            "uptime": hasil_uptime
        }

    except paramiko.AuthenticationException:
        print("Status   : Gagal")
        print("Kesalahan: Username atau password SSH salah.")

        return {
            "status": "gagal",
            "pesan": "Autentikasi SSH gagal."
        }

    except paramiko.SSHException as error:
        print("Status   : Gagal")
        print("Kesalahan SSH:", error)

        return {
            "status": "gagal",
            "pesan": str(error)
        }

    except Exception as error:
        print("Status   : Gagal")
        print("Kesalahan:", error)

        return {
            "status": "gagal",
            "pesan": str(error)
        }

    finally:
        client.close()


# ==========================================
# PROGRAM UTAMA
# ==========================================

if __name__ == "__main__":
    cek_ssh()