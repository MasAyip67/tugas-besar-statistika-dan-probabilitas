# ==============================================================================
# SISTEM PEMETAAN WILAYAH & DOMISILI MAHASISWA
# ==============================================================================

import networkx as nx
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. MODUL TREE: Hierarki Kategori / Wilayah
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    # Fitur 1: Menampilkan seluruh entitas (Print Tree)
    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    # Fungsi Bantuan: Mencari entitas spesifik di dalam Tree
    def find_node(self, target_data):
        if self.data.lower() == target_data.lower():
            return self
        for child in self.children:
            found = child.find_node(target_data)
            if found:
                return found
        return None

    # Fitur 3: Menampilkan relasi Parent-Child
    def show_relations(self):
        print(f"\n[Relasi Entitas: {self.data}]")
        
        if self.parent:
            print(f"Parent   : {self.parent.data}")
        else:
            print(f"Parent   : (Ini adalah Root Utama)")
            
        if self.children:
            nama_anak = [child.data for child in self.children]
            print(f"Children : {', '.join(nama_anak)}")
        else:
            print(f"Children : (Tidak memiliki child / merupakan Leaf)")

# ---------------------------------------------------------
# 2. MODUL SEARCHING & SORTING
# ---------------------------------------------------------
def quick_sort_mhs(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]['nim']
    left = [x for x in arr if x['nim'] < pivot]
    middle = [x for x in arr if x['nim'] == pivot]
    right = [x for x in arr if x['nim'] > pivot]
    return quick_sort_mhs(left) + middle + quick_sort_mhs(right)

def binary_search_mhs(arr, target_nim):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]['nim'] == target_nim:
            return arr[mid]
        elif arr[mid]['nim'] < target_nim:
            low = mid + 1
        else:
            high = mid - 1
    return None

# ---------------------------------------------------------
# Inisialisasi Data Sistem
# ---------------------------------------------------------
def init_data():
    # 1. Setup Data Tree Wilayah
    root_wilayah = TreeNode("Provinsi Sulawesi Tengah")
    
    kota_palu = TreeNode("Kota Palu")
    kab_sigi = TreeNode("Kabupaten Sigi")
    kab_parigi = TreeNode("Kabupaten Parigi Moutong")
    kab_donggala = TreeNode("Kabupaten Donggala")
    kab_poso = TreeNode("Kabupaten Poso")
    kab_morowali = TreeNode("Kabupaten Morowali")

    palu_timur = TreeNode("Palu Timur")
    sigi_biromaru = TreeNode("Sigi Biromaru")
    parigi_selatan = TreeNode("Parigi Selatan")
    donggala_banawa = TreeNode("Banawa")
    poso_kota = TreeNode("Poso Kota")
    morowali_bungku = TreeNode("Bungku Tengah")

    root_wilayah.add_child(kota_palu)
    root_wilayah.add_child(kab_sigi)
    root_wilayah.add_child(kab_parigi)
    root_wilayah.add_child(kab_donggala)
    root_wilayah.add_child(kab_poso)
    root_wilayah.add_child(kab_morowali)

    kota_palu.add_child(palu_timur)
    kota_palu.add_child(TreeNode("Palu Barat"))
    kab_sigi.add_child(sigi_biromaru)
    kab_parigi.add_child(parigi_selatan)
    kab_donggala.add_child(donggala_banawa)
    kab_poso.add_child(poso_kota)
    kab_morowali.add_child(morowali_bungku)

    palu_timur.add_child(TreeNode("Kelurahan Besusu"))
    sigi_biromaru.add_child(TreeNode("Desa Mpanau"))
    parigi_selatan.add_child(TreeNode("Kelurahan Masigi"))

    # 2. Setup Data Graph Rute menggunakan NetworkX (Undirected Graph)
    rute_graph = nx.Graph()  
    rute_graph.add_nodes_from([
        "Kota Palu", "Kabupaten Donggala", "Kabupaten Sigi", 
        "Kabupaten Parigi Moutong", "Kabupaten Poso", "Kabupaten Morowali"
    ])

    edges = [
        ("Kota Palu", "Kabupaten Donggala", 35),
        ("Kota Palu", "Kabupaten Sigi", 15),
        ("Kabupaten Sigi", "Kabupaten Parigi Moutong", 70),
        ("Kota Palu", "Kabupaten Parigi Moutong", 65),
        ("Kabupaten Parigi Moutong", "Kabupaten Poso", 135),  
        ("Kabupaten Poso", "Kabupaten Morowali", 240)         
    ]
    rute_graph.add_weighted_edges_from(edges)

    # 3. Setup Database Mahasiswa
    db_mahasiswa = [
        {"nim": "F5212520063", "nama": "Moh. Arif Sigit", "jurusan": "Teknologi Informasi", "prodi": "S1 Sistem Informasi", "wilayah": "Kelurahan Besusu, Palu Timur"},
        {"nim": "F5212520071", "nama": "Fatih Ariqoh", "jurusan": "Teknologi Informasi", "prodi": "S1 Sistem Informasi", "wilayah": "Kelurahan Masigi, Parigi Selatan"},
        {"nim": "F5212520070", "nama": "Bimo Prakoso Batmomolin", "jurusan": "Teknologi Informasi", "prodi": "S1 Sistem Informasi", "wilayah": "Desa Mpanau, Sigi Biromaru"},
        {"nim": "F5212520045", "nama": "Athamisyal Firaz Malahika", "jurusan": "Teknologi Informasi", "prodi": "S1 Sistem Informasi", "wilayah": "Sigi Biromaru"},
        {"nim": "F5212520075", "nama": "Bayu Wasista", "jurusan": "Teknologi Informasi", "prodi": "S1 Sistem Informasi", "wilayah": "Banawa, Kabupaten Donggala"},
        {"nim": "F5212520064", "nama": "Regan Musholli", "jurusan": "Teknologi Informasi", "prodi": "S1 Sistem Informasi", "wilayah": "Poso Kota, Kabupaten Poso"}
    ]

    return root_wilayah, rute_graph, db_mahasiswa

# ---------------------------------------------------------
# Antarmuka Command Line
# ---------------------------------------------------------
def main():
    tree_wilayah, graph_rute, data_mhs = init_data()
    data_mhs_sorted = quick_sort_mhs(data_mhs)

    while True:
        print("\n" + "="*40)
        print("===== SISTEM DOMISILI MAHASISWA =====")
        print("1. Kelola Tree Hierarki Wilayah")
        print("2. Kelola Graph Rute Wilayah")
        print("3. Binary Search (Cari Mhs by NIM)")
        print("4. BFS Traversal Graph (Cetak & Visualisasi)")
        print("5. Keluar")
        print("="*40)

        pilihan = input("Pilihan : ")

        if pilihan == '1':
            while True:
                print("\n--- KELOLA TREE HIERARKI ---")
                print("a. Menampilkan seluruh entitas Tree")
                print("b. Menambahkan kategori/entitas baru dinamis")
                print("c. Menampilkan relasi Parent-Child dari suatu entitas")
                print("d. Kembali ke Menu Utama")
                sub_pilih = input("Pilih menu Tree (a/b/c/d): ").lower()

                if sub_pilih == 'a':
                    print("\n--- Struktur Keseluruhan Tree ---")
                    tree_wilayah.print_tree()

                elif sub_pilih == 'b':
                    print("\n--- Tambah Entitas Baru ---")
                    nama_parent = input("Masukkan nama entitas Parent tempat data baru akan ditambahkan: ")
                    parent_node = tree_wilayah.find_node(nama_parent)
                    
                    if parent_node:
                        nama_baru = input(f"Masukkan nama entitas/kategori baru di bawah '{parent_node.data}': ")
                        parent_node.add_child(TreeNode(nama_baru))
                        print(f"Berhasil! '{nama_baru}' telah ditambahkan sebagai anak dari '{parent_node.data}'.")
                        
                        # 📌 TITIK HUBUNG 1: Jika user menambah Kabupaten baru langsung di bawah Root Provinsi
                        if parent_node == tree_wilayah:
                            if nama_baru not in graph_rute:
                                graph_rute.add_node(nama_baru)
                                print(f"[SINKRONISASI] '{nama_baru}' otomatis ditambahkan sebagai Node baru di Graph Rute.")
                    else:
                        print(f"Gagal: Entitas Parent '{nama_parent}' tidak ditemukan di dalam Tree.")

                elif sub_pilih == 'c':
                    print("\n--- Cek Relasi Parent-Child ---")
                    nama_entitas = input("Masukkan nama entitas yang ingin dicek relasinya: ")
                    target_node = tree_wilayah.find_node(nama_entitas)
                    
                    if target_node:
                        target_node.show_relations()
                    else:
                        print(f"Gagal: Entitas '{nama_entitas}' tidak ditemukan.")

                elif sub_pilih == 'd':
                    break
                else:
                    print("Pilihan sub-menu tidak valid.")

        elif pilihan == '2':
            while True:
                print("\n--- KELOLA GRAPH RUTE WILAYAH ---")
                print("a. Tambah Lokasi (Node) Baru")
                print("b. Tambah Rute/Relasi (Edge) Baru")
                print("c. Tampilkan Tetangga (Adjacent Nodes)")
                print("d. Tampilkan Graph (Visualisasi GUI)")
                print("e. Kembali ke Menu Utama")
                sub_pilih = input("Pilih menu Graph (a/b/c/d/e): ").lower()

                if sub_pilih == 'a':
                    print("\n--- Tambah Lokasi Baru ---")
                    lokasi_baru = input("Masukkan nama wilayah/lokasi baru: ")
                    
                    if lokasi_baru in graph_rute:
                        print(f"Lokasi '{lokasi_baru}' sudah ada di dalam peta.")
                    else:
                        graph_rute.add_node(lokasi_baru)
                        print(f"Berhasil! Lokasi '{lokasi_baru}' telah ditambahkan.")
                        
                        # 📌 TITIK HUBUNG 2: Otomatis daftarkan lokasi baru ke dalam Tree di bawah Root Provinsi
                        if not tree_wilayah.find_node(lokasi_baru):
                            tree_wilayah.add_child(TreeNode(lokasi_baru))
                            print(f"[SINKRONISASI] '{lokasi_baru}' otomatis terdaftar sebagai entitas di bawah '{tree_wilayah.data}' pada Tree.")

                elif sub_pilih == 'b':
                    print("\n--- Tambah Relasi Rute Baru ---")
                    lokasi_asal = input("Masukkan lokasi asal: ")
                    lokasi_tujuan = input("Masukkan lokasi tujuan: ")
                    
                    if lokasi_asal not in graph_rute or lokasi_tujuan not in graph_rute:
                        print("Gagal: Pastikan kedua lokasi sudah terdaftar di peta. Gunakan opsi 'a' jika belum.")
                    else:
                        try:
                            jarak = int(input("Masukkan jarak tempuh (dalam KM): "))
                            graph_rute.add_edge(lokasi_asal, lokasi_tujuan, weight=jarak)
                            print(f"Berhasil! Rute dari '{lokasi_asal}' ke '{lokasi_tujuan}' ({jarak} KM) telah ditambahkan.")
                        except ValueError:
                            print("Gagal: Input jarak harus berupa angka.")

                elif sub_pilih == 'c':
                    print("\n--- Cek Lokasi Tetangga (Adjacent Nodes) ---")
                    lokasi_cek = input("Masukkan nama lokasi yang ingin dicek tetangganya: ")
                    
                    if lokasi_cek in graph_rute:
                        tetangga = list(graph_rute.neighbors(lokasi_cek))
                        if tetangga:
                            print(f"\n[Lokasi yang terhubung langsung dengan '{lokasi_cek}']")
                            for ttg in tetangga:
                                jarak_ttg = graph_rute[lokasi_cek][ttg]['weight']
                                print(f"- {ttg} (Jarak: {jarak_ttg} KM)")
                        else:
                            print(f"Lokasi '{lokasi_cek}' saat ini terisolasi.")
                    else:
                        print(f"Gagal: Lokasi '{lokasi_cek}' tidak ditemukan.")

                elif sub_pilih == 'd':
                    print("\n--- Membuka Peta Jaringan Rute... ---")
                    pos = nx.spring_layout(graph_rute, seed=50)
                    nx.draw(graph_rute, pos, with_labels=True, node_color='lightgreen', 
                            font_weight='bold', node_size=2500, font_size=8)
                    edge_labels = nx.get_edge_attributes(graph_rute, 'weight')
                    nx.draw_networkx_edge_labels(graph_rute, pos, edge_labels=edge_labels, font_size=8)
                    plt.title('Peta Rute Tak Berarah & Jarak Antar Wilayah (KM)')
                    plt.show()
                    print("Jendela visualisasi telah ditutup.")

                elif sub_pilih == 'e':
                    break
                else:
                    print("Pilihan sub-menu tidak valid.")

        elif pilihan == '3':
            print("\n--- Cari Data Mahasiswa ---")
            nim_cari = input("Masukkan NIM yang dicari: ")
            hasil = binary_search_mhs(data_mhs_sorted, nim_cari)
            if hasil:
                print("\n[Data Ditemukan]")
                print(f"NIM      : {hasil['nim']}")
                print(f"Nama     : {hasil['nama']}")
                print(f"Akademik : Jurusan {hasil['jurusan']} (Membawahi {hasil['prodi']})")
                print(f"Domisili : {hasil['wilayah']}")
            else:
                print(f"\nData dengan NIM {nim_cari} tidak ditemukan.")

        elif pilihan == '4':
            print("\n--- Pencarian Rute (BFS Shortest Path) ---")
            start_node = input("Masukkan wilayah asal (Source): ")
            target_node = input("Masukkan wilayah tujuan (Target): ")
            
            if start_node in graph_rute and target_node in graph_rute:
                try:
                    # 1. Kalkulasi rute terpendek menggunakan BFS
                    jalur = nx.shortest_path(graph_rute, source=start_node, target=target_node)
                    
                    # Cetak urutan jalur di terminal
                    print(f"\nRute Terpendek Ditemukan: {' -> '.join(jalur)}")
                    
                    # 2. Visualisasi Peta
                    print("Membuka jendela visualisasi peta rute...")
                    plt.figure(figsize=(8, 5))
                    pos = nx.spring_layout(graph_rute, seed=50)
                    
                    # Gambar graf dasar terlebih dahulu (warna hijau, garis abu-abu)
                    nx.draw(graph_rute, pos, with_labels=True, node_color='lightgreen', 
                            font_weight='bold', node_size=2500, edge_color='gray', font_size=8)
                    
                    # 3. Persiapkan data jalur yang akan diwarnai MERAH
                    path_edges = list(zip(jalur, jalur[1:]))
                    
                    # Timpa node yang dilewati dengan warna merah muda (lightcoral)
                    nx.draw_networkx_nodes(graph_rute, pos, nodelist=jalur, node_color='lightcoral', node_size=2500)
                    # Timpa garis/rute yang dilewati dengan warna MERAH TEBAL
                    nx.draw_networkx_edges(graph_rute, pos, edgelist=path_edges, edge_color='red', width=3.0)
                    
                    # Gambar label jarak (weight)
                    edge_labels = nx.get_edge_attributes(graph_rute, 'weight')
                    nx.draw_networkx_edge_labels(graph_rute, pos, edge_labels=edge_labels, font_size=8)
                    
                    plt.title(f'Navigasi BFS (Garis Merah): {start_node} -> {target_node}')
                    plt.show()
                    print("Jendela visualisasi rute telah ditutup.")
                except nx.NetworkXNoPath:
                    print(f"Gagal: Tidak ada jalan yang menghubungkan '{start_node}' dan '{target_node}'.")
            else:
                print("Wilayah asal atau tujuan tidak ditemukan di dalam Peta Graph.")

        elif pilihan == '5':
            print("\nKeluar dari program.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()