
class Stack:
    def __init__(self, max_size):
        self.data = []
        self.max_size = max_size

    def isFull(self):
        return len(self.data) == self.max_size

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, item):
        if not self.isFull():
            self.data.append(item)
        else:
            print("Stack penuh!")

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            print("Stack kosong!")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return None

    def display(self):
        print("Riwayat Pelayanan:")
        for item in reversed(self.data):
            print(item)

class Queue:
    def __init__(self, max_size):
        self.data = []
        self.max_size = max_size

    def isFull(self):
        return len(self.data) == self.max_size

    def isEmpty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        if not self.isFull():
            self.data.append(item)
        else:
            print("Antrian penuh!")

    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)
        else:
            print("Antrian kosong!")
            return None

    def view(self):
        if not self.isEmpty():
            return self.data[0]
        else:
            return None

    def display(self):
        print("\nDaftar Antrian:")
        if self.isEmpty():
            print("Antrian kosong")
        else:
            for i, item in enumerate(self.data, start=1):
                print(f"{i}. {item}")

    def count(self):
        return len(self.data)


antrian = Queue(100)
riwayat = Stack(100)

while True:
    print("\n=== SISTEM ANTRIAN KASIR ===")
    print("1. Tambah Pelanggan")
    print("2. Panggil Pelanggan")
    print("3. Lihat Antrian")
    print("4. Peek (Lihat Depan)")
    print("5. Total Antrian")
    print("6. Lihat Riwayat")
    print("7. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama: ")
        item = input("Jumlah item: ")
        waktu = input("Estimasi waktu (menit): ")

        data = f"{nama} | Item: {item} | Waktu: {waktu} menit"
        antrian.enqueue(data)

    elif pilih == "2":
        pelanggan = antrian.dequeue()
        if pelanggan:
            print("Memanggil:", pelanggan)
            riwayat.push(pelanggan)

    elif pilih == "3":
        antrian.display()

    elif pilih == "4":
        depan = antrian.view()
        if depan:
            print("Pelanggan berikutnya:", depan)
        else:
            print("Antrian kosong")

    elif pilih == "5":
        print("Total antrian:", antrian.count())

    elif pilih == "6":
        riwayat.display()

    elif pilih == "7":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid!")