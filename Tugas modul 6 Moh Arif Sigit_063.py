class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Khusus Doubly

# =========================================================================
# 1. SINGLY LINKED LIST (Manajer Unduhan Global)
# =========================================================================
class DownloadManager:
    def __init__(self): self.head = None
    
    def unduh(self, file): # Append (Menambah data di akhir)
        new = Node(file)
        if not self.head: self.head = new
        else:
            curr = self.head
            while curr.next: curr = curr.next
            curr.next = new
        print(f">> [SUKSES] Unduh file: '{file}'")

    def tampil(self): # Display
        curr = self.head
        if not curr: print("Folder Unduhan Kosong."); return
        while curr: print(f"[{curr.data}]", end=" -> "); curr = curr.next
        print("None")

# =========================================================================
# 2. DOUBLY LINKED LIST (Navigasi Internal Per Tab)
# =========================================================================
class BrowserNavigation:
    def __init__(self):
        self.head = None
        self.current = None

    def buka_url(self, url): # Append (Menambah jejak riwayat baru di akhir)
        new = Node(url)
        if not self.head: self.head = new; self.current = new
        else: self.current.next = new; new.prev = self.current; self.current = new
        print(f">> Menjelajahi: {url}")

    def back(self): # Fitur khusus penunjuk mundur (.prev)
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f">> [BACK] Kembali ke: {self.current.data}")
        else: print(">> [ALERT] Tidak bisa BACK! Ini halaman pertama.")

    def forward(self): # Fitur khusus penunjuk maju (.next)
        if self.current and self.current.next:
            self.current = self.current.next
            print(f">> [FORWARD] Maju ke: {self.current.data}")
        else: print(">> [ALERT] Tidak bisa FORWARD! Ini halaman terbaru.")

    def tampil(self): # Display dengan penunjuk letak halaman aktif
        curr = self.head
        while curr:
            print(f"| {curr.data} |" if curr == self.current else f"[{curr.data}]", end=" <-> ")
            curr = curr.next
        print("None")

# =========================================================================
# 3. CIRCULAR LINKED LIST (Pengelola Tab - Menampung Objek Doubly)
# =========================================================================
class TabSwitcher:
    def __init__(self):
        self.head = None
        self.active_tab = None

    def buka_tab(self, nama): # Append & Prepend terintegrasi
        new = Node(nama)
        new.nav = BrowserNavigation() # Hubungan antar Linked List terjadi di sini!
        new.nav.buka_url(f"homepage_{nama}.com") # Otomatis set awal halaman
        
        if not self.head: self.head = new; new.next = self.head; self.active_tab = new
        else:
            curr = self.head
            while curr.next != self.head: curr = curr.next
            curr.next = new; new.next = self.head
        print(f">> [TAB] Berhasil membuka tab: '{nama}'")

    def ganti_tab(self): # Perputaran melingkar tanpa ujung khas Circular
        if self.active_tab:
            self.active_tab = self.active_tab.next
            print(f">> [SWITCH] Geser layar ke: Tab '{self.active_tab.data}'")

    def tampil(self): # Display seluruh tab browser
        if not self.head: print("Tidak ada tab terbuka."); return
        curr = self.head
        while True:
            print(f"| {curr.data} (AKTIF) |" if curr == self.active_tab else f"[{curr.data}]", end=" -> ")
            curr = curr.next
            if curr == self.head: break
        print("(Melingkar)")

# =========================================================================
# ENGINE UTAMA: SATU MENU UNTUK SEMUA OPERASI TERHUBUNG
# =========================================================================
def main():
    tabs = TabSwitcher(); unduhan = DownloadManager()
    tabs.buka_tab("Utama") # Membuat satu tab awal otomatis saat browser dibuka
    
    while True:
        tab_aktif = tabs.active_tab.data if tabs.active_tab else "Kosong"
        print("\n" + "="*45 + f"\n WINDOWS BROWSER | Tab Aktif: '{tab_aktif}'\n" + "="*45)
        print("1. Buka Tab Baru (Circular Append)\n2. Geser/Switch Tab (Circular Next)\n3. Kunjungi Website Baru (Doubly Append)\n4. Tombol Kembali (Doubly Prev)\n5. Tombol Maju (Doubly Next)\n6. Unduh File dari Web Ini (Singly Append)\n7. Lihat Status Folder Unduhan (Singly Display)\n8. Tampilkan Peta Seluruh Memori Browser (All Display)\n0. Keluar")
        p = input("Pilih Menu (0-8): ")
        
        if p == '1': tabs.buka_tab(input("Nama tab baru: "))
        elif p == '2': tabs.ganti_tab()
        elif p == '3': 
            if tabs.active_tab: tabs.active_tab.nav.buka_url(input("Masukkan URL: "))
        elif p == '4': 
            if tabs.active_tab: tabs.active_tab.nav.back()
        elif p == '5': 
            if tabs.active_tab: tabs.active_tab.nav.forward()
        elif p == '6': 
            if tabs.active_tab: unduhan.unduh(input("Nama file: "))
        elif p == '7': print("\n--- FOLDER DOWNLOAD SAYA ---"); unduhan.tampil()
        elif p == '8':
            print("\n--- STRUKTUR PETA MEMORI BROWSER ---")
            print("1. Struktur Tab (Circular Linked List):"); tabs.tampil()
            if tabs.active_tab: 
                print(f"2. Histori Web di Tab '{tabs.active_tab.data}' (Doubly Linked List):"); tabs.active_tab.nav.tampil()
        elif p == '0': print("Menutup core browser... Selesai."); break

if __name__ == "__main__": main()
