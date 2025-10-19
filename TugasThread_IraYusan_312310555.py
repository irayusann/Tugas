import threading
import time

# Saldo awal rekening
saldo = 100
# Objek lock untuk mencegah akses bersamaan
lock = threading.Lock()

def tarik_uang_aman(nama, jumlah):
    """
    Fungsi penarikan dengan menggunakan lock
    agar tidak terjadi race condition antar thread.
    """
    global saldo
    with lock:
        print(f"\n{nama} sedang memproses penarikan...")
        time.sleep(0.1)

        print(f"Saldo sebelum {nama} menarik: {saldo}")

        if saldo >= jumlah:
            saldo -= jumlah
            print(f"{nama} berhasil menarik {jumlah}")
        else:
            print(f"{nama} gagal menarik, saldo tidak mencukupi")

        print(f"Saldo setelah {nama} menarik: {saldo}")

def main():
    print("=" * 50)
    print("SIMULASI PENARIKAN UANG DENGAN LOCK")
    print("=" * 50)
    print(f"Saldo awal: {saldo}")
    print("Jumlah penarikan masing-masing: 80")
    print("=" * 50)

    andi = threading.Thread(target=tarik_uang_aman, args=("Andi", 80))
    budi = threading.Thread(target=tarik_uang_aman, args=("Budi", 80))

    andi.start()
    budi.start()

    andi.join()
    budi.join()

    print("\n" + "=" * 50)
    print(f"SALDO AKHIR: {saldo}")
    print("=" * 50)

if __name__ == "__main__":
    main()
