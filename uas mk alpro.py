import os

# =====================================================================
# 1. STRUKTUR DATA TREE (Hierarki Wilayah Administratif)
# =====================================================================
class NodeWilayah:
    def __init__(self, nama):
        self.nama = nama
        self.anak = []

    def tambah_anak(self, node_anak):
        self.anak.append(node_anak)

    def tampilkan_wilayah(self, spasi=0):
        print("  " * spasi + "|-- " + self.nama)
        for item in self.anak:
            item.tampilkan_wilayah(spasi + 2)

# Inisialisasi Data Tree (Hierarki Wilayah)
sulteng = NodeWilayah("Provinsi Sulawesi Tengah")

# Kabupaten Sigi
sigi = NodeWilayah("Kabupaten Sigi")
biromaru = NodeWilayah("Kec. Sigi Biromaru")
biromaru.tambah_anak(NodeWilayah("Desa Mpanau"))
biromaru.tambah_anak(NodeWilayah("Desa Kabobona"))
sigi.tambah_anak(biromaru)
sulteng.tambah_anak(sigi)

# Kabupaten Parigi Moutong
parigi_kab = NodeWilayah("Kabupaten Parigi Moutong")
parigi_kec = NodeWilayah("Kec. Parigi")
parigi_kec.tambah_anak(NodeWilayah("Kelurahan Masigi"))
parigi_kab.tambah_anak(parigi_kec)
sulteng.tambah_anak(parigi_kab)

# Kota Palu
palu_kota = NodeWilayah("Kota Palu")
palu_timur = NodeWilayah("Kec. Palu Timur")
palu_timur.tambah_anak(NodeWilayah("Kelurahan Besusu"))
palu_kota.tambah_anak(palu_timur)
sulteng.tambah_anak(palu_kota)


# =====================================================================
# 2. STRUKTUR DATA GRAPH (Jaringan Rute Jalan Antar Wilayah)
# =====================================================================
rute_wilayah = {
    "Palu": [("Sigi", 15), ("Donggala", 35), ("Parigi", 75)],
    "Sigi": [("Palu", 15), ("Parigi", 85)],
    "Donggala": [("Palu", 35)],
    "Parigi": [("Palu", 75), ("Sigi", 85)]
}

# --- Algoritma Traversal 1: Breadth-First Search (BFS) ---
def traversal_bfs(graph, start):
    if start not in graph:
        return []
    
    dikunjungi = []
    antrean = [start] # Menggunakan Queue (FIFO)
    
    while antrean:
        titik = antrean.pop(0)
        if titik not in dikunjungi:
            dikunjungi.append(titik)
            for tetangga, jarak in graph.get(titik, []):
                if tetangga not in dikunjungi:
                    antrean.append(tetangga)
    return dikunjungi

# --- Algoritma Traversal 2: Depth-First Search (DFS) ---
def traversal_dfs(graph, start):
    if start not in graph:
        return []
    
    dikunjungi = []
    tumpukan = [start] # Menggunakan Stack (LIFO)
    
    while tumpukan:
        titik = tumpukan.pop() # Mengambil dari elemen paling akhir
        if titik not in dikunjungi:
            dikunjungi.append(titik)
            # Dibalik agar urutan penelusuran sesuai urutan input list
            for tetangga, jarak in reversed(graph.get(titik, [])):
                if tetangga not in dikunjungi:
                    tumpukan.append(tetangga)
    return dikunjungi


# =====================================================================
# 3. ALGORITMA SEARCH (Pencarian Data Mahasiswa)
# =====================================================================
db_mahasiswa = [
    {"nim": "F55123001", "nama": "Ahmad", "domisili": "Desa Mpanau (Sigi)"},
    {"nim": "F55123002", "nama": "Siti", "domisili": "Kelurahan Masigi (Parigi)"},
    {"nim": "F55123003", "nama": "Budi", "domisili": "Desa Kabobona (Sigi)"},
    {"nim": "F55123004", "nama": "Dewi", "domisili": "Kelurahan Besusu (Palu)"}
]

# Binary Search untuk NIM
def binary_search_nim(database, target_nim):
    low = 0
    high = len(database) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if database[mid]["nim"] == target_nim:
            return database[mid]
        elif database[mid]["nim"] < target_nim:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Linear Search untuk Wilayah
def linear_search_wilayah(database, keyword):
    hasil = []
    for mhs in database:
        if keyword.lower() in mhs["domisili"].lower():
            hasil.append(mhs)
    return hasil


# =====================================================================
# 4. ANTARMUKA UTAMA (MENU CLI SESUAI LAYOUT PPT)
# =====================================================================
def menu_utama():
    while True:
        print("\n=== SISTEM AKADEMIK V1.0 ===")
        print("1. Lihat Hierarki Peminatan (Tree)")
        print("2. Cari Detail Mata Kuliah (Search)")
        print("3. Lihat Alur Prasyarat (Graph)")
        print("4. Cek Rekomendasi Semester (BFS / DFS)")
        print("5. Keluar")
        print("----------------------------")
        
        pilihan = input("Pilihan Anda: ")
        
        if pilihan == "1":
            print("\n[INFO] Menampilkan Hierarki Wilayah Asal Mahasiswa:")
            sulteng.tampilkan_wilayah()
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == "2":
            print("\n=== FITUR PENCARIAN DATA MAHASISWA ===")
            print("a. Cari Spesifik via NIM (Binary Search)")
            print("b. Cari Berdasarkan Nama Wilayah (Linear Search)")
            sub_pilihan = input("Pilih metode pencarian (a/b): ").lower()
            
            if sub_pilihan == "a":
                target = input("Masukkan NIM Mahasiswa: ").upper()
                hasil = binary_search_nim(db_mahasiswa, target)
                if hasil:
                    print(f"\n-> DATA DITEMUKAN: {hasil['nama']} | Domisili: {hasil['domisili']}")
                else:
                    print("\n-> Data mahasiswa tidak ditemukan.")
            elif sub_pilihan == "b":
                keyword = input("Masukkan Nama Wilayah/Desa: ")
                hasil_list = linear_search_wilayah(db_mahasiswa, keyword)
                if hasil_list:
                    print(f"\nDaftar Mahasiswa di '{keyword}':")
                    for mhs in hasil_list:
                        print(f" - {mhs['nim']} | {mhs['nama']} ({mhs['domisili']})")
                else:
                    print("\n-> Tidak ada mahasiswa di wilayah tersebut.")
            else:
                print("\nPilihan metode tidak valid.")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == "3":
            print("\n[INFO] Menampilkan Jaringan Peta Jalan & Jarak Antar Wilayah:")
            for asal, tujuan_list in rute_wilayah.items():
                print(f" Wilayah {asal} terhubung langsung ke:")
                for tujuan, jarak in tujuan_list:
                    print(f"  -> {tujuan} ({jarak} KM)")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == "4":
            print("\n=== TRACE URUTAN JANGKAUAN WILAYAH ===")
            asal = input("Masukkan Titik Awal (Palu/Sigi/Parigi/Donggala): ").capitalize()
            
            if asal in rute_wilayah:
                print("\nSilakan Pilih Metode Traversal:")
                print("a. BFS (Breadth-First Search) - Melebar/Tetangga Terdekat")
                print("b. DFS (Depth-First Search) - Mendalam ke Satu Jalur")
                metode = input("Pilihan Metode (a/b): ").lower()
                
                if metode == "a":
                    hasil_bfs = traversal_bfs(rute_wilayah, asal)
                    print(f"\nUrutan wilayah terjangkau (BFS) dari {asal}:")
                    print(" -> ".join(hasil_bfs))
                elif metode == "b":
                    hasil_dfs = traversal_dfs(rute_wilayah, asal)
                    print(f"\nUrutan wilayah terjangkau (DFS) dari {asal}:")
                    print(" -> ".join(hasil_dfs))
                else:
                    print("\nMetode yang dipilih tidak tersedia.")
            else:
                print("\nWilayah tidak terdaftar dalam peta jaringan.")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == "5":
            print("\nProgram selesai. Terima kasih!")
            break
        else:
            print("\nPilihan tidak ada. Silakan pilih menu 1-5.")
            input("\nTekan Enter untuk mencoba lagi...")

if __name__ == "__main__":
    menu_utama()