def tampilkan_menu():
    print("\n=== APLIKASI PENGELOLA DAFTAR BELANJA VILO ===")
    print("1. Tampilkan Semua Daftar Belanja")
    print("2. Tambah Item Baru")
    print("3. Hapus Item Berdasarkan Nama")
    print("4. Ubah Jumlah Item")
    print("5. Cari Barang")
    print("6. Urutkan Berdasarkan Harga (Termurah)")
    print("7. Tampilkan 3 Item Termahal")
    print("0. Keluar")

def tampilkan_belanjaan(daftar):
    if not daftar:
        print("\nDaftar belanjaan masih kosong.")
        return
    
    print(f"\n{'Nama Barang':<20} | {'Harga':<10} | {'Jumlah':<8} | {'Total':<10}")
    print("-" * 55)
    total_seluruh = 0
    for item in daftar:
        total_item = item['harga'] * item['jumlah']
        total_seluruh += total_item
        print(f"{item['nama']:<20} | {item['harga']:<10} | {item['jumlah']:<8} | {total_item:<10}")
    print("-" * 55)
    print(f"TOTAL BELANJA KESELURUHAN: {total_seluruh}")

def main(): 
    # Array utama untuk menyimpan data belanja
    daftar_belanja = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-7): ")

        if pilihan == '1':
            tampilkan_belanjaan(daftar_belanja)

        elif pilihan == '2':
            nama = input("Masukkan nama barang: ")
            harga = int(input("Masukkan harga satuan: "))
            jumlah = int(input("Masukkan jumlah beli: "))
            daftar_belanja.append({'nama': nama, 'harga': harga, 'jumlah': jumlah})
            print("Barang berhasil ditambahkan!")

        elif pilihan == '3':
            nama = input("Masukkan nama barang yang ingin dihapus: ")
            # Menghapus item dengan filter list comprehension
            daftar_belanja = [item for item in daftar_belanja if item['nama'].lower() != nama.lower()]
            print(f"Item {nama} telah dihapus (jika ada).")

        elif pilihan == '4':
            nama = input("Masukkan nama barang yang akan diubah jumlahnya: ")
            ketemu = False
            for item in daftar_belanja:
                if item['nama'].lower() == nama.lower():
                    item['jumlah'] = int(input("Masukkan jumlah baru: "))
                    print("Jumlah berhasil diperbarui!")
                    ketemu = True
                    break
            if not ketemu: print("Barang tidak ditemukan.")

        elif pilihan == '5':
            nama = input("Cari barang: ")
            hasil = [item for item in daftar_belanja if nama.lower() in item['nama'].lower()]
            tampilkan_belanjaan(hasil)

        elif pilihan == '6':
            # Mengurutkan menggunakan fungsi lambda berdasarkan kunci 'harga'
            daftar_belanja.sort(key=lambda x: x['harga'])
            print("Daftar berhasil diurutkan dari yang termurah.")
            tampilkan_belanjaan(daftar_belanja)

        elif pilihan == '7':
            # Mengurutkan terbalik (mahal ke murah) lalu ambil 3 teratas
            termahal = sorted(daftar_belanja, key=lambda x: x['harga'], reverse=True)[:3]
            print("\n--- 3 ITEM TERMAHAL ---")
            tampilkan_belanjaan(termahal)

        elif pilihan == '0':
            print("Terima kasih! Selamat belanja, Vilo.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()