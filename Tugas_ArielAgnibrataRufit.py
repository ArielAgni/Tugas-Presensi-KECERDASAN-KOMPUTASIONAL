import os
import sys

CYAN    = "\033[1;36m"
GREEN   = "\033[1;32m"
RED     = "\033[1;31m"
YELLOW  = "\033[1;33m"
GRAY    = "\033[38;5;245m"
WHITE   = "\033[97m"
BOLD    = "\033[1m"
RESET   = "\033[0m"
BORDER  = "\033[38;5;240m"


mahasiswa = [
    {"nama": "Anton",   "kehadiran": "Tinggi", "tugas": "Lengkap"},
    {"nama": "Kalamari",   "kehadiran": "Rendah", "tugas": "Tidak Lengkap"},
    {"nama": "Cinta",  "kehadiran": "Tinggi", "tugas": "Tidak Lengkap"},
    {"nama": "Dendi",   "kehadiran": "Rendah", "tugas": "Lengkap"},
    {"nama": "Topson",   "kehadiran": "Tinggi", "tugas": "Lengkap"},   # data baru
]


def klasifikasi(mhs):
    if mhs["kehadiran"] == "Tinggi":
        status = "Aktif"
        keterangan = "Mahasiswa Disiplin " if mhs["tugas"] == "Lengkap" else "Perlu Tingkatkan Tugas"
    else:
        status = "Tidak Aktif"
        keterangan = "Hadir Kurang, Tugas OK" if mhs["tugas"] == "Lengkap" else "Butuh Perhatian Serius "
    return status, keterangan


def clear():
    os.system("cls" if os.name == "nt" else "clear")



def cetak_header():
    print()
    print(BORDER + "╔" + "═" * 60 + "╗" + RESET)
    print(BORDER + "║" + RESET + CYAN + "   SISTEM PRESENSI MAHASISWA".center(60) + RESET + BORDER + "║" + RESET)
    print(BORDER + "║" + RESET + GRAY + "   Kecerdasan Komputasional — Decision Tree".center(60) + RESET + BORDER + "║" + RESET)
    print(BORDER + "╚" + "═" * 60 + "╝" + RESET)
    print()


def cetak_kartu(nomor, mhs):
    status, keterangan = klasifikasi(mhs)
    warna_status = GREEN if status == "Aktif" else RED
    warna_ket    = YELLOW if "Disiplin" in keterangan else WHITE

    print(BORDER + f"  ┌── Mahasiswa #{nomor:02d} " + "─" * 42 + "┐" + RESET)
    print(BORDER + "  │" + RESET + f"  {GRAY}Nama       : {RESET}{WHITE}{mhs['nama']:<20}{RESET}" + BORDER + "                       │" + RESET)
    print(BORDER + "  │" + RESET + f"  {GRAY}Kehadiran  : {RESET}{WHITE}{mhs['kehadiran']:<20}{RESET}" + BORDER + "                       │" + RESET)
    print(BORDER + "  │" + RESET + f"  {GRAY}Tugas      : {RESET}{WHITE}{mhs['tugas']:<20}{RESET}" + BORDER + "                       │" + RESET)
    print(BORDER + "  │" + RESET + f"  {GRAY}Status     : {RESET}{warna_status}{status:<20}{RESET}" + BORDER + "                       │" + RESET)
    print(BORDER + "  │" + RESET + f"  {GRAY}Keterangan : {RESET}{warna_ket}{keterangan:<20}{RESET}" + BORDER + "                       │" + RESET)
    print(BORDER + "  └" + "─" * 57 + "┘" + RESET)
    print()


def cetak_rekap():
    total    = len(mahasiswa)
    aktif    = sum(1 for m in mahasiswa if klasifikasi(m)[0] == "Aktif")
    disiplin = sum(1 for m in mahasiswa if "Disiplin" in klasifikasi(m)[1])
    tidak    = total - aktif

    print()
    print(BORDER + "  ┌─   REKAP STATISTIK " + "─" * 37 + "┐" + RESET)
    print(BORDER + "  │" + RESET + f"  {GRAY}Total Mahasiswa   : {RESET}{WHITE}{total}{RESET}" + BORDER + "                                │" + RESET)
    print(BORDER + "  │" + RESET + f"  {GRAY}Status Aktif      : {RESET}{GREEN}{aktif}{RESET}" + BORDER + "                                │" + RESET)
    print(BORDER + "  │" + RESET + f"  {GRAY}Tidak Aktif       : {RESET}{RED}{tidak}{RESET}" + BORDER + "                                │" + RESET)
    print(BORDER + "  │" + RESET + f"  {GRAY}Mahasiswa Disiplin: {RESET}{YELLOW}{disiplin}{RESET}" + BORDER + "                                │" + RESET)
    print(BORDER + "  └" + "─" * 57 + "┘" + RESET)
    print()


def cetak_menu():
    print(BORDER + "  ┌─ MENU " + "─" * 51 + "┐" + RESET)
    print(BORDER + "  │" + RESET + f"  {CYAN}[1]{RESET} Tampilkan Semua Data"        + BORDER + "                               │" + RESET)
    print(BORDER + "  │" + RESET + f"  {CYAN}[2]{RESET} Cari Mahasiswa"              + BORDER + "                                    │" + RESET)
    print(BORDER + "  │" + RESET + f"  {CYAN}[3]{RESET} Tambah Mahasiswa Baru"       + BORDER + "                             │" + RESET)
    print(BORDER + "  │" + RESET + f"  {CYAN}[4]{RESET} Rekap Statistik"             + BORDER + "                                  │" + RESET)
    print(BORDER + "  │" + RESET + f"  {CYAN}[0]{RESET} Keluar"                      + BORDER + "                                        │" + RESET)
    print(BORDER + "  └" + "─" * 57 + "┘" + RESET)
    print()


# ---------- FITUR SEARCH ----------
def cari_mahasiswa():
    clear()
    cetak_header()

    # Tampilkan sub-menu filter
    print(BORDER + "  ┌─   CARI MAHASISWA " + "─" * 38 + "┐" + RESET)
    print(BORDER + "  │" + RESET + f"  {CYAN}[1]{RESET} Cari berdasarkan Nama"       + BORDER + "                             │" + RESET)
    print(BORDER + "  │" + RESET + f"  {CYAN}[2]{RESET} Filter berdasarkan Status (Aktif / Tidak Aktif)" + BORDER + "  │" + RESET)
    print(BORDER + "  │" + RESET + f"  {CYAN}[3]{RESET} Filter berdasarkan Kehadiran (Tinggi / Rendah)" + BORDER + "   │" + RESET)
    print(BORDER + "  │" + RESET + f"  {CYAN}[4]{RESET} Filter berdasarkan Tugas (Lengkap / Tidak)"     + BORDER + "    │" + RESET)
    print(BORDER + "  └" + "─" * 57 + "┘" + RESET)
    print()

    mode = input(f"  {GRAY}Pilih mode pencarian [1-4]: {RESET}").strip()

    hasil = []

    if mode == "1":
        kata = input(f"  {GRAY}Masukkan nama (boleh sebagian): {RESET}").strip().lower()
        hasil = [m for m in mahasiswa if kata in m["nama"].lower()]
        label = f"nama mengandung '{kata}'"

    elif mode == "2":
        print(f"  {GRAY}Pilihan: {WHITE}aktif {GRAY}/ {WHITE}tidak aktif{RESET}")
        kata = input(f"  {GRAY}Masukkan status: {RESET}").strip().lower()
        hasil = [m for m in mahasiswa if kata in klasifikasi(m)[0].lower()]
        label = f"status '{kata}'"

    elif mode == "3":
        print(f"  {GRAY}Pilihan: {WHITE}tinggi {GRAY}/ {WHITE}rendah{RESET}")
        kata = input(f"  {GRAY}Masukkan kehadiran: {RESET}").strip().lower()
        hasil = [m for m in mahasiswa if kata in m["kehadiran"].lower()]
        label = f"kehadiran '{kata}'"

    elif mode == "4":
        print(f"  {GRAY}Pilihan: {WHITE}lengkap {GRAY}/ {WHITE}tidak{RESET}")
        kata = input(f"  {GRAY}Masukkan status tugas: {RESET}").strip().lower()
        hasil = [m for m in mahasiswa if kata in m["tugas"].lower()]
        label = f"tugas '{kata}'"

    else:
        print(f"\n  {RED}Pilihan tidak valid.{RESET}\n")
        input(f"  {GRAY}Tekan Enter untuk kembali...{RESET}")
        return

    print()
    if hasil:
        print(f"  {GREEN}✔  Ditemukan {len(hasil)} mahasiswa dengan {label}:{RESET}\n")
        for i, m in enumerate(hasil, 1):
            cetak_kartu(i, m)
    else:
        print(f"  {RED}⚠  Tidak ada mahasiswa dengan {label}.{RESET}\n")

    input(f"  {GRAY}Tekan Enter untuk kembali...{RESET}")

def tambah_mahasiswa():
    clear()
    cetak_header()
    print(f"  {CYAN}── Tambah Mahasiswa Baru{RESET}\n")

    nama = input(f"  {GRAY}Nama          : {RESET}").strip()

    while True:
        k = input(f"  {GRAY}Kehadiran (t=Tinggi / r=Rendah): {RESET}").strip().lower()
        if k in ("t", "r"):
            kehadiran = "Tinggi" if k == "t" else "Rendah"
            break
        print(f"  {RED}Masukkan 't' atau 'r'{RESET}")

    while True:
        tg = input(f"  {GRAY}Tugas (l=Lengkap / t=Tidak Lengkap): {RESET}").strip().lower()
        if tg in ("l", "t"):
            tugas = "Lengkap" if tg == "l" else "Tidak Lengkap"
            break
        print(f"  {RED}Masukkan 'l' atau 't'{RESET}")

    mahasiswa.append({"nama": nama, "kehadiran": kehadiran, "tugas": tugas})
    print(f"\n  {GREEN}✔  Mahasiswa '{nama}' berhasil ditambahkan!{RESET}\n")
    input(f"  {GRAY}Tekan Enter untuk kembali...{RESET}")


def main():
    while True:
        clear()
        cetak_header()
        cetak_menu()

        pilihan = input(f"  {GRAY}Pilih menu [0-4]: {RESET}").strip()

        if pilihan == "1":
            clear()
            cetak_header()
            print(f"  {CYAN}── Daftar Seluruh Mahasiswa{RESET}\n")
            for i, m in enumerate(mahasiswa, 1):
                cetak_kartu(i, m)
            input(f"  {GRAY}Tekan Enter untuk kembali...{RESET}")

        elif pilihan == "2":
            cari_mahasiswa()

        elif pilihan == "3":
            tambah_mahasiswa()

        elif pilihan == "4":
            clear()
            cetak_header()
            cetak_rekap()
            input(f"  {GRAY}Tekan Enter untuk kembali...{RESET}")

        elif pilihan == "0":
            clear()
            print(f"\n  {CYAN}Terima kasih! Program selesai.{RESET}\n")
            sys.exit(0)

        else:
            print(f"\n  {RED}Pilihan tidak valid.{RESET}")


if __name__ == "__main__":
    main()
