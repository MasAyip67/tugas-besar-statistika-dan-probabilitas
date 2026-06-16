import networkx as nx
import matplotlib.pyplot as plt

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

    def print_tree(self):
        spaces = self.get_level() * 4
        prefix = spaces * " " + "|-- " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

# Membangun struktur organisasi (Tree)
root = TreeNode("Pemilik Klub SSB")

pelatih_kepala = TreeNode("Pelatih Kepala")
admin_klub = TreeNode("Manajer Administrasi")
medis = TreeNode("Tim Medis & Fisioterapi")

root.add_child(pelatih_kepala)
root.add_child(admin_klub)
root.add_child(medis)

pelatih_kepala.add_child(TreeNode("Pelatih Kelompok U-12"))
pelatih_kepala.add_child(TreeNode("Pelatih Kelompok U-15"))
pelatih_kepala.add_child(TreeNode("Pelatih Khusus Kiper"))

admin_klub.add_child(TreeNode("Staf Pendaftaran"))
admin_klub.add_child(TreeNode("Staf Logistik & Bola"))

# Membangun skema serangan (Directed Graph)
G = nx.DiGraph()

posisi = ["Kiper", "Bek", "Gelandang", "Sayap", "Penyerang"]
G.add_nodes_from(posisi)

jalur_bola = [
    ("Kiper", "Bek"),
    ("Bek", "Gelandang"),
    ("Gelandang", "Sayap"),
    ("Gelandang", "Penyerang"),
    ("Sayap", "Penyerang"),
    ("Bek", "Sayap")
]
G.add_edges_from(jalur_bola)

# Output
print("--- 1. Visualisasi Tree: Struktur Organisasi SSB ---")
root.print_tree()
print("\n")

print("--- 2. Visualisasi Directed Graph: Skema Serangan Tim ---")
nx.draw(G, with_labels=True, node_color='gold', 
        font_weight='bold', node_size=2000, edge_color='green', 
        arrows=True, arrowsize=20)
plt.title('Directed Graph: Alur Aliran Bola (Skema Serangan)')
plt.show()