import math
import networkx as nx
import matplotlib.pyplot as plt

# =================================================================
# MODUL 6: LINKED LIST (Manajemen Skuad Pemain)
# =================================================================
class NodePemain:
    def __init__(self, nama, posisi):
        self.nama = nama
        self.posisi = posisi
        self.next = None

class SkuadTim:
    def __init__(self):
        self.head = None

    def tambah_pemain(self, nama, posisi):
        baru = NodePemain(nama, posisi)
        if not self.head:
            self.head = baru
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = baru

    def tampilkan(self):
        temp = self.head
        if not temp: return "Belum ada pemain."
        res = []
        while temp:
            res.append(f"{temp.nama} ({temp.posisi})")
            temp = temp.next
        return " -> ".join(res)

# =================================================================
# MODUL 4: TREE (Bagan Pertandingan)
# =================================================================
class NodeBagan:
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_bagan(self, level=0):
        print("    " * level + "|-- " + self.label)
        for child in self.children:
            child.print_bagan(level + 1)

# =================================================================
# SISTEM UTAMA (INTEGRASI 6 MODUL)
# =================================================================
class FutsalTournamentSystem:
    def __init__(self):
        # MODUL 1: ARRAY
        self.statistik_gol = [12, 5, 8, 20, 3, 15, 7, 10]
        
        # MODUL 2: STACK & QUEUE
        self.queue_pendaftaran = [] # FIFO
        self.stack_pelanggaran = []  # LIFO
        
        self.manajemen_skuad = SkuadTim()

    # --- MODUL 3: SORTING (Quick Sort) ---
    def quick_sort(self, data):
        if len(data) <= 1: return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    # --- MODUL 3: SEARCHING (Jump Search) ---
    def jump_search(self, arr, target):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while prev < n and arr[min(step, n)-1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n: return -1
        for i in range(prev, min(step, n)):
            if arr[i] == target: return i
        return -1

    # --- MODUL 5: GRAPH (Memunculkan Gambar Sesuai Foto) ---
    def tampilkan_visualisasi_graph(self):
        # Inisialisasi graph [cite: 410]
        G = nx.Graph()
        
        # Menambahkan simpul pemain [cite: 413]
        nodes = ['Kiper', 'Bek', 'Sayap', 'Gelandang', 'Penyerang']
        G.add_nodes_from(nodes)
        
        # Menambahkan sisi (garis hijau) sesuai contoh [cite: 430]
        edges = [
            ('Kiper', 'Bek'),
            ('Bek', 'Sayap'), ('Bek', 'Gelandang'),
            ('Sayap', 'Penyerang'), ('Sayap', 'Gelandang'),
            ('Penyerang', 'Gelandang')
        ]
        G.add_edges_from(edges)
        
        # Menentukan posisi simpul secara manual agar mirip gambar [cite: 416]
        fixed_layout = {
            'Kiper': (0, 0),
            'Bek': (1, 1),
            'Sayap': (0.5, 2),
            'Gelandang': (3, 1.8),
            'Penyerang': (2.5, 2.8)
        }
        
        # Menggambar graf dengan warna dan ukuran sesuai permintaan [cite: 433, 436]
        plt.figure(figsize=(8, 6))
        nx.draw(G, fixed_layout, with_labels=True, node_color='gold', 
                node_size=4000, font_size=12, font_weight='bold', 
                edge_color='green', width=2)
        plt.title('Visualisasi Posisi Pemain (Modul 5)')
        plt.show() # [cite: 437]

# =================================================================
# FUNGSI MAIN
# =================================================================
def main():
    app = FutsalTournamentSystem()
    
    # Inisialisasi Tree (Bagan Luas)
    juara = NodeBagan("JUARA 1 (FINAL)")
    sf1 = NodeBagan("Semi Final 1"); sf2 = NodeBagan("Semi Final 2")
    juara.add_child(sf1); juara.add_child(sf2)
    sf1.add_child(NodeBagan("Pemenang PF 1")); sf1.add_child(NodeBagan("Pemenang PF 2"))
    sf2.add_child(NodeBagan("Pemenang PF 3")); sf2.add_child(NodeBagan("Pemenang PF 4"))

    while True:
        print("\n" + "="*45)
        print("      FUTSAL SYSTEM INTEGRATED v4.1")
        print("="*45)
        print("1. Array - Statistik Gol")
        print("2. Stack & Queue - Registrasi & Log")
        print("3. Sorting & Searching - Analisis")
        print("4. Tree - Bagan Turnamen Lengkap")
        print("5. Graph - Tampilkan Visualisasi Gambar")
        print("6. Linked List - Manajemen Skuad")
        print("7. Keluar")
        
        pilih = input("\nPilih Menu> ")

        # Bagian ini yang diperbarui sesuai permintaanmu
        if pilih == '5':
            print("\n[GRAPH] Sedang memproses gambar...")
            app.tampilkan_visualisasi_graph()
        
        elif pilih == '1': 
            print(f"Data Gol: {app.statistik_gol}")
        
        elif pilih == '4': 
            juara.print_bagan()
            
        elif pilih == '6':
            n = input("Nama: "); p = input("Posisi: ")
            app.manajemen_skuad.tambah_pemain(n, p)
            print(f"Skuad: {app.manajemen_skuad.tampilkan()}")
            
        elif pilih == '7':
            print("\nProgram UAS Berhasil Dijalankan.")
            break

if __name__ == "__main__":
    main()