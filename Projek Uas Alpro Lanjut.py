import math
import os
import networkx as nx
import matplotlib.pyplot as plt


# =========================================================
# MODUL 6 : LINKED LIST
# =========================================================
class NodePesanan:
    def __init__(self, menu, harga):
        self.menu = menu
        self.harga = harga
        self.next = None


class DaftarPesanan:
    def __init__(self):
        self.head = None

    def tambah_item(self, menu, harga):
        baru = NodePesanan(menu, harga)

        if self.head is None:
            self.head = baru
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = baru

    def tampilkan(self):
        if self.head is None:
            print("Belum ada pesanan")
            return

        temp = self.head
        nomor = 1

        while temp:
            print(f"{nomor}. {temp.menu} - Rp{temp.harga}")
            temp = temp.next
            nomor += 1

    def hitung_total(self):
        total = 0
        temp = self.head

        while temp:
            total += temp.harga
            temp = temp.next

        return total


# =========================================================
# MODUL 4 : TREE
# =========================================================
class NodeMenu:
    def __init__(self, nama):
        self.nama = nama
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def tampilkan_tree(self, level=0):
        print("   " * level + "|-- " + self.nama)

        for child in self.children:
            child.tampilkan_tree(level + 1)


# =========================================================
# SISTEM UTAMA
# =========================================================
class ManajemenRestoran:

    def __init__(self):

        # =====================================================
        # MODUL 1 : ARRAY
        # =====================================================
        self.nama_menu = [
            "Nasi Goreng",
            "Ayam Bakar",
            "Es Teh",
            "Kopi Hitam",
            "Mie Goreng"
        ]

        self.harga_items = [
            15000,
            25000,
            12000,
            18000,
            17000
        ]

        # =====================================================
        # MODUL 2 : STACK & QUEUE
        # =====================================================
        self.queue_pesanan = []
        self.stack_piring = []

        # =====================================================
        # MODUL 6 : LINKED LIST
        # =====================================================
        self.pesanan_aktif = DaftarPesanan()

    # =========================================================
    # MEMBERSIHKAN LAYAR
    # =========================================================
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # =========================================================
    # MODUL 3 : QUICK SORT
    # =========================================================
    def quick_sort(self, data):

        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2]

        kiri = [x for x in data if x < pivot]
        tengah = [x for x in data if x == pivot]
        kanan = [x for x in data if x > pivot]

        return self.quick_sort(kiri) + tengah + self.quick_sort(kanan)

    # =========================================================
    # MODUL 3 : JUMP SEARCH
    # =========================================================
    def jump_search(self, arr, x):

        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0

        while prev < n and arr[min(step, n) - 1] < x:

            prev = step
            step += int(math.sqrt(n))

            if prev >= n:
                return -1

        for i in range(prev, min(step, n)):

            if arr[i] == x:
                return i

        return -1

    # =========================================================
    # MENU ARRAY
    # =========================================================
    def menu_array(self):

        print("\n========== ARRAY ==========")

        for i in range(len(self.nama_menu)):
            print(f"{i+1}. {self.nama_menu[i]} - Rp{self.harga_items[i]}")

        print("\nStatistik Harga")
        print(f"Harga Termurah : Rp{min(self.harga_items)}")
        print(f"Harga Termahal : Rp{max(self.harga_items)}")
        print(f"Rata-rata Harga: Rp{sum(self.harga_items)/len(self.harga_items):.0f}")

    # =========================================================
    # MENU STACK & QUEUE
    # =========================================================
    def menu_stack_queue(self):

        while True:

            print("\n====== STACK & QUEUE ======")
            print("1. Tambah Antrean Pesanan")
            print("2. Proses Antrean Pesanan")
            print("3. Tambah Piring Kotor")
            print("4. Cuci Piring")
            print("5. Lihat Data")
            print("0. Kembali")

            pilih = input("Pilih menu : ")

            if pilih == '1':

                pesanan = input("Masukkan pesanan : ")
                self.queue_pesanan.append(pesanan)

                print("Pesanan masuk antrean")

            elif pilih == '2':

                if len(self.queue_pesanan) == 0:
                    print("Antrean kosong")

                else:
                    proses = self.queue_pesanan.pop(0)
                    print(f"Pesanan diproses : {proses}")

            elif pilih == '3':

                piring = input("Masukkan kode piring : ")
                self.stack_piring.append(piring)

                print("Piring ditambahkan")

            elif pilih == '4':

                if len(self.stack_piring) == 0:
                    print("Tidak ada piring")

                else:
                    cuci = self.stack_piring.pop()
                    print(f"Piring dicuci : {cuci}")

            elif pilih == '5':

                print("\nQUEUE / FIFO")
                print(self.queue_pesanan)

                print("\nSTACK / LIFO")
                print(self.stack_piring)

            elif pilih == '0':
                break

            else:
                print("Pilihan tidak valid")

    # =========================================================
    # MENU SORTING & SEARCHING
    # =========================================================
    def menu_sorting_searching(self):

        print("\n===== SORTING & SEARCHING =====")

        hasil_sort = self.quick_sort(self.harga_items)

        print(f"Data Awal   : {self.harga_items}")
        print(f"Quick Sort  : {hasil_sort}")

        cari = int(input("\nMasukkan harga yang dicari : Rp"))

        hasil = self.jump_search(hasil_sort, cari)

        if hasil != -1:
            print(f"Harga ditemukan pada index ke-{hasil}")

        else:
            print("Harga tidak ditemukan")

    # =========================================================
    # MENU TREE
    # =========================================================
    def menu_tree(self):

        root = NodeMenu("MENU CAFE")

        makanan = NodeMenu("Makanan")
        minuman = NodeMenu("Minuman")

        makanan.add_child(NodeMenu("Nasi Goreng"))
        makanan.add_child(NodeMenu("Ayam Bakar"))
        makanan.add_child(NodeMenu("Mie Goreng"))

        minuman.add_child(NodeMenu("Es Teh"))
        minuman.add_child(NodeMenu("Kopi Hitam"))

        root.add_child(makanan)
        root.add_child(minuman)

        print("\n========== TREE ==========")
        root.tampilkan_tree()

    # =========================================================
    # MENU GRAPH
    # =========================================================
    def menu_graph(self):

        print("\n========== GRAPH ==========")

        G = nx.Graph()

        # NODE
        G.add_node("Kasir")
        G.add_node("Meja 1")
        G.add_node("Meja 2")
        G.add_node("Meja 3")
        G.add_node("Dapur")

        # EDGE
        G.add_edge("Kasir", "Meja 1")
        G.add_edge("Kasir", "Dapur")
        G.add_edge("Meja 1", "Meja 2")
        G.add_edge("Meja 2", "Meja 3")
        G.add_edge("Meja 3", "Dapur")

        # POSISI
        pos = {
            "Kasir": (0, 1),
            "Meja 1": (1, 2),
            "Meja 2": (2, 1),
            "Meja 3": (3, 0),
            "Dapur": (0, 0)
        }

        plt.figure(figsize=(8, 5))

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="gold",
            node_size=4000,
            font_size=12,
            font_weight="bold",
            edge_color="green"
        )

        plt.title("Graph Relasi Layout Cafe")
        plt.show()

    # =========================================================
    # MENU LINKED LIST
    # =========================================================
    def menu_linked_list(self):

        while True:

            print("\n====== LINKED LIST ======")
            print("1. Tambah Pesanan")
            print("2. Lihat Pesanan")
            print("0. Kembali")

            pilih = input("Pilih menu : ")

            if pilih == '1':

                menu = input("Nama menu : ")
                harga = int(input("Harga : Rp"))

                self.pesanan_aktif.tambah_item(menu, harga)

                print("Pesanan berhasil ditambahkan")

            elif pilih == '2':

                print("\nDaftar Pesanan")
                self.pesanan_aktif.tampilkan()

                print(f"\nTotal Tagihan : Rp{self.pesanan_aktif.hitung_total()}")

            elif pilih == '0':
                break

            else:
                print("Pilihan tidak valid")


# =========================================================
# MENU UTAMA
# =========================================================
def main():

    sistem = ManajemenRestoran()

    while True:

        print("\n" + "=" * 55)
        print("      CAFE & RESTO MANAGEMENT SYSTEM")
        print("=" * 55)

        print("1. Array - Statistik Harga Menu")
        print("2. Stack & Queue - Dapur dan Piring")
        print("4. Sorting & Searching - Analisis Harga")
        print("6. Tree - Struktur Kategori Menu")
        print("7. Graph - Relasi Layout Cafe")
        print("8. Linked List - Pesanan Meja")
        print("0. Keluar")

        print("=" * 55)

        pilihan = input("Pilih menu : ")

        if pilihan == '1':
            sistem.menu_array()

        elif pilihan == '2':
            sistem.menu_stack_queue()

        elif pilihan == '4':
            sistem.menu_sorting_searching()

        elif pilihan == '6':
            sistem.menu_tree()

        elif pilihan == '7':
            sistem.menu_graph()

        elif pilihan == '8':
            sistem.menu_linked_list()

        elif pilihan == '0':
            print("\nProgram selesai.")
            break

        else:
            print("Pilihan tidak valid")


# =========================================================
# MENJALANKAN PROGRAM
# =========================================================
if __name__ == "__main__":
    main()