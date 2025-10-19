import threading
import time

# Saldo awal rekening bersama
saldo = 100

def tarik_uang(nama, jumlah):
    """
    Fungsi untuk melakukan penarikan tanpa menggunakan lock.
    Dapat menyebabkan kondisi race (data conflict).
    """
    global saldo
    print(f"\n{nama} sedang memproses penarikan...")
    time.sleep(0.1)

    print(f"Saldo sebelum {nama} menarik: {saldo}")

    # Mengurangi saldo tanpa pengamanan
    saldo -= jumlah
    print(f"{nama} berhasil menarik {jumlah}")
    print(f"Saldo setelah {nama} menarik: {saldo}")

def main():
    print("=" * 50)
    print("SIMULASI PENARIKAN UANG TANPA LOCK")
    print("=" * 50)
    print(f"Saldo awal: {saldo}")
    print("Jumlah penarikan masing-masing: 80")
    print("=" * 50)

    # Membuat dua thread untuk simulasi
    andi = threading.Thread(target=tarik_uang, args=("Andi", 80))
    budi = threading.Thread(target=tarik_uang, args=("Budi", 80))

    # Menjalankan kedua thread secara bersamaan
    andi.start()
    budi.start()

    # Menunggu semua thread selesai
    andi.join()
    budi.join()

    # Menampilkan hasil akhir
    print("\n" + "=" * 50)
    print(f"SALDO AKHIR: {saldo}")
    print("=" * 50)

if __name__ == "__main__":
    main()
