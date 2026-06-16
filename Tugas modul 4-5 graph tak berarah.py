import networkx as nx
import matplotlib.pyplot as plt

# BAGIAN 1: TREE (Struktur Organisasi)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = [] # List untuk menampung banyak anak
        self.parent = None

    def add_child(self, child):
        child.parent = self # Set simpul saat ini sebagai induk
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p: # Menelusuri induk hingga ke root
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        # Indentasi berdasarkan level kedalaman simpul
        spaces = self.get_level() * 4
        prefix = spaces * " " + "|-- " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

# Implementasi Tree SSB
root = TreeNode("Pemilik Klub SSB")

# Tingkat 1: Tiga Cabang Utama
pelatih_kepala = TreeNode("Pelatih Kepala")
admin_klub = TreeNode("Manajer Administrasi")
medis = TreeNode("Tim Medis & Fisioterapi")

root.add_child(pelatih_kepala)
root.add_child(admin_klub)
root.add_child(medis)

# Tingkat 2: Detail dari tiap Cabang
pelatih_kepala.add_child(TreeNode("Pelatih Kelompok U-12"))
pelatih_kepala.add_child(TreeNode("Pelatih Kelompok U-15"))
pelatih_kepala.add_child(TreeNode("Pelatih Khusus Kiper"))

admin_klub.add_child(TreeNode("Staf Pendaftaran"))
admin_klub.add_child(TreeNode("Staf Logistik & Bola"))

# BAGIAN 2: GRAPH (Jaringan Operan Pemain)
# Inisialisasi graf tidak berarah
G = nx.Graph()

# Menambahkan 5 simpul posisi pemain
posisi = ["Kiper", "Bek", "Gelandang", "Sayap", "Penyerang"]
G.add_nodes_from(posisi)

# Menambahkan relasi operan
jalur_bola = [
    ("Kiper", "Bek"),
    ("Bek", "Gelandang"),
    ("Gelandang", "Sayap"),
    ("Gelandang", "Penyerang"),
    ("Sayap", "Penyerang"),
    ("Bek", "Sayap")
]
G.add_edges_from(jalur_bola)

# BAGIAN 3: OUTPUT AKHIR

print("--- 1. Visualisasi Tree: Struktur Organisasi SSB ---")
root.print_tree()
print("\n")

# Menggambar graf 
nx.draw(G, with_labels=True, node_color='gold', 
        font_weight='bold', node_size=2000, edge_color='green')
plt.title('Undirected Graph: Relasi Operan Bola Antar Posisi')
plt.show()