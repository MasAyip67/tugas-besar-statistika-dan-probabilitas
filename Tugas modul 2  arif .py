import json
import os
from datetime import datetime

class SupermarketQueueSystem:
    def __init__(self):
        # Struktur Data
        self.queue = []      # Queue (Antrian Utama)
        self.history = []    # Stack (Riwayat Pelayanan)
        self.vip_count_today = 0
        self.max_vip = 3
        self.file_name = "data_supermarket.json"

    # ==========================================
    # A. SISTEM ANTRIAN UTAMA (QUEUE - FIFO)
    # ==========================================
    
    def tambah_pelanggan(self, nama, item, waktu, is_vip=False):
        pelanggan = {
            "nama": nama,
            "item": item,
            "waktu": waktu,
            "is_vip": is_vip
        }
        
        if is_vip:
            if self.vip_count_today < self.max_vip:
                self.queue.insert(0, pelanggan) # Masuk ke depan antrian
                self.vip_count_today += 1
                print(f"[+] Pelanggan VIP '{nama}' berhasil ditambahkan ke depan antrian! (Sisa kuota VIP: {self.max_vip - self.vip_count_today})")
            else:
                print("[-] Gagal: Kuota pelanggan VIP hari ini sudah habis (Maksimal 3/hari).")
                return
        else:
            self.queue.append(pelanggan) # Masuk ke belakang antrian
            print(f"[+] Pelanggan '{nama}' berhasil ditambahkan ke antrian.")

    def panggil_pelanggan(self):
        if not self.queue:
            print("[-] Antrian kosong. Tidak ada pelanggan yang bisa dipanggil.")
            return
        
        # Dequeue dari depan (indeks 0)
        pelanggan = self.queue.pop(0)
        
        # Tambahkan stempel waktu selesai
        waktu_selesai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pelanggan["waktu_selesai"] = waktu_selesai
        
        # Push ke Stack Riwayat
        self.history.append(pelanggan)
        print(f"[!] Memanggil pelanggan '{pelanggan['nama']}' untuk menuju kasir.")

    def lihat_antrian(self):
        if not self.queue:
            print("[-] Antrian saat ini kosong.")
            return
            
        print("\n--- DAFTAR ANTRIAN SAAT INI ---")
        print(f"{'Posisi':<8} | {'Nama Pelanggan':<15} | {'Item':<6} | {'Est. Waktu':<12} | {'Status':<6}")
        print("-" * 60)
        
        akumulasi_waktu = 0
        for i, p in enumerate(self.queue):
            status = "VIP" if p['is_vip'] else "Reguler"
            print(f"{i+1:<8} | {p['nama']:<15} | {p['item']:<6} | {p['waktu']:<5} menit | {status:<6}")
            akumulasi_waktu += p['waktu']
            
        print("-" * 60)
        print(f"Total Pelanggan: {len(self.queue)}")
        print(f"Total Estimasi Waktu Tunggu Antrian: {akumulasi_waktu} menit")

    def peek_antrian(self):
        if self.queue:
            p = self.queue[0]
            print(f"[*] Pelanggan di baris terdepan: {p['nama']} ({p['item']} item, {p['waktu']} menit)")
        else:
            print("[-] Antrian kosong.")

    def hitung_estimasi_waktu(self, nama_target):
        waktu_tunggu = 0
        ditemukan = False
        
        for p in self.queue:
            if p['nama'].lower() == nama_target.lower():
                ditemukan = True
                break
            waktu_tunggu += p['waktu']
            
        if ditemukan:
            print(f"[*] Estimasi waktu tunggu untuk '{nama_target}' adalah {waktu_tunggu} menit.")
        else:
            print(f"[-] Pelanggan dengan nama '{nama_target}' tidak ditemukan di antrian.")

    def reset_antrian(self):
        self.queue.clear()
        print("[!] Seluruh antrian berhasil dikosongkan.")

    # B. SISTEM RIWAYAT PELAYANAN (STACK - LIFO)
    
    def lihat_riwayat(self):
        if not self.history:
            print("[-] Riwayat pelayanan masih kosong.")
            return
            
        print("\n--- RIWAYAT PELAYANAN (Terbaru ke Terlama) ---")
        print(f"{'No':<4} | {'Nama Pelanggan':<15} | {'Item':<6} | {'Waktu Selesai':<20}")
        print("-" * 55)
        
        # Iterasi dari atas stack (terbaru/terakhir dimasukkan)
        for i, p in enumerate(reversed(self.history)):
            print(f"{i+1:<4} | {p['nama']:<15} | {p['item']:<6} | {p['waktu_selesai']:<20}")
        print("-" * 55)
        print(f"Total Pelanggan Dilayani: {len(self.history)}")

    def peek_riwayat(self):
        if self.history:
            p = self.history[-1] # Puncak stack
            print(f"[*] Pelanggan terakhir dilayani: {p['nama']} pada {p['waktu_selesai']}")
        else:
            print("[-] Riwayat kosong.")

    def undo_pelayanan(self):
        if not self.history:
            print("[-] Riwayat kosong. Tidak ada yang bisa di-undo.")
            return
            
        # Pop dari Stack
        pelanggan = self.history.pop()
        
        # Hapus stempel waktu
        if "waktu_selesai" in pelanggan:
            del pelanggan["waktu_selesai"]
            
        # Kembalikan ke depan Queue
        self.queue.insert(0, pelanggan)
        print(f"[!] UNDO BERHASIL: Pelanggan '{pelanggan['nama']}' dikembalikan ke antrian terdepan.")

    def cari_riwayat(self, nama_target):
        hasil_cari = [p for p in self.history if p['nama'].lower() == nama_target.lower()]
        
        if hasil_cari:
            print(f"\n[*] Ditemukan {len(hasil_cari)} riwayat untuk '{nama_target}':")
            for p in hasil_cari:
                print(f"    - Dilayani pada: {p['waktu_selesai']} ({p['item']} item)")
        else:
            print(f"[-] Pelanggan '{nama_target}' belum pernah dilayani hari ini.")

    def reset_riwayat(self):
        self.history.clear()
        print("[!] Seluruh riwayat pelayanan berhasil dihapus.")

    # C. FITUR TAMBAHAN (Integrasi)

    def statistik_harian(self):
        print("\n=== STATISTIK HARIAN ===")
        total_dilayani = len(self.history)
        sisa_antrian = len(self.queue)
        
        total_waktu_pelayanan = sum(p['waktu'] for p in self.history)
        rata_waktu = (total_waktu_pelayanan / total_dilayani) if total_dilayani > 0 else 0
        
        print(f"Total pelanggan selesai dilayani : {total_dilayani} orang")
        print(f"Sisa pelanggan dalam antrian   : {sisa_antrian} orang")
        print(f"Rata-rata waktu pelayanan      : {rata_waktu:.2f} menit/orang")
        print(f"Kuota VIP terpakai hari ini    : {self.vip_count_today}/{self.max_vip}")
        print("========================\n")

    def simpan_data(self):
        data = {
            "queue": self.queue,
            "history": self.history,
            "vip_count": self.vip_count_today
        }
        try:
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"[+] Data berhasil diekspor ke '{self.file_name}'.")
        except Exception as e:
            print(f"[-] Gagal menyimpan data: {e}")

    def muat_data(self):
        if not os.path.exists(self.file_name):
            print(f"[-] File '{self.file_name}' tidak ditemukan.")
            return
            
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.queue = data.get("queue", [])
                self.history = data.get("history", [])
                self.vip_count_today = data.get("vip_count", 0)
            print("[+] Data berhasil diimpor dari file.")
        except Exception as e:
            print(f"[-] Gagal memuat data: {e}")

# MENU INTERAKTIF (Console)

def main():
    sistem = SupermarketQueueSystem()
    
    while True:
        print("\n" + "="*40)
        print("   SISTEM ANTRIAN KASIR 'BUAH HATI'")
        print("="*40)
        print("1. Tambah Pelanggan ke Antrian")
        print("2. Panggil Pelanggan Berikutnya (Ke Kasir)")
        print("3. Lihat Antrian Saat Ini")
        print("4. Cek Estimasi Waktu Tunggu Pelanggan")
        print("5. Lihat Riwayat Pelayanan (Selesai)")
        print("6. Batal/Undo Panggilan Terakhir")
        print("7. Cari Riwayat Pelanggan")
        print("8. Lihat Statistik Harian")
        print("9. Simpan / Muat Data (Ekspor/Impor)")
        print("0. Keluar Program")
        print("="*40)
        
        pilihan = input("Pilih menu (0-9): ")
        
        try:
            if pilihan == '1':
                nama = input("Nama Pelanggan: ")
                item = int(input("Jumlah Item: "))
                waktu = int(input("Estimasi Waktu (menit): "))
                is_vip_input = input("Apakah VIP? (y/n): ").strip().lower()
                is_vip = True if is_vip_input == 'y' else False
                
                sistem.tambah_pelanggan(nama, item, waktu, is_vip)
                
            elif pilihan == '2':
                sistem.peek_antrian()
                konfirmasi = input("Lanjutkan panggil? (y/n): ")
                if konfirmasi.lower() == 'y':
                    sistem.panggil_pelanggan()
                    
            elif pilihan == '3':
                sistem.lihat_antrian()
                
            elif pilihan == '4':
                nama = input("Masukkan nama pelanggan di antrian: ")
                sistem.hitung_estimasi_waktu(nama)
                
            elif pilihan == '5':
                sistem.lihat_riwayat()
                sistem.peek_riwayat()
                
            elif pilihan == '6':
                konfirmasi = input("Yakin ingin membatalkan pelanggan terakhir dilayani? (y/n): ")
                if konfirmasi.lower() == 'y':
                    sistem.undo_pelayanan()
                    
            elif pilihan == '7':
                nama = input("Masukkan nama pelanggan yang dicari: ")
                sistem.cari_riwayat(nama)
                
            elif pilihan == '8':
                sistem.statistik_harian()
                
            elif pilihan == '9':
                print("1. Simpan Data ke File")
                print("2. Muat Data dari File")
                sub_pilihan = input("Pilih (1/2): ")
                if sub_pilihan == '1':
                    sistem.simpan_data()
                elif sub_pilihan == '2':
                    sistem.muat_data()
                else:
                    print("Pilihan tidak valid.")
                    
            elif pilihan == '0':
                print("Menyimpan data otomatis sebelum keluar...")
                sistem.simpan_data()
                print("Terima kasih telah menggunakan Sistem Antrian Buah Hati.")
                break
                
            elif pilihan == '99': # Secret menu reset
                sistem.reset_antrian()
                sistem.reset_riwayat()
                
            else:
                print("[-] Pilihan tidak valid. Masukkan angka 0-9.")
                
        except ValueError:
            print("[-] Input error! Pastikan jumlah item dan waktu berupa angka.")
        except Exception as e:
            print(f"[-] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()