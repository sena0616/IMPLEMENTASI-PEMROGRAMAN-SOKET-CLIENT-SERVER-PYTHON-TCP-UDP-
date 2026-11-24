import socket

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 65432
TIMEOUT_DETIK = 10.0
BUFFER_SIZE = 1024


def main():
    print("=" * 65)
    print("      CLIENT SOCKET JARINGAN KOMPUTER (IF25-21008) - ITERA")
    print("=" * 65)

    target_host = input(f"Masukkan IP Server tujuan [Default: {DEFAULT_HOST}]: ").strip()
    if not target_host:
        target_host = DEFAULT_HOST

    port_input = input(f"Masukkan Port Server [Default: {DEFAULT_PORT}]: ").strip()
    target_port = int(port_input) if port_input else DEFAULT_PORT

    print(f"\n[INFO] Menghubungkan ke Server {target_host}:{target_port} ...")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(TIMEOUT_DETIK)
    print(f"[CONFIG] Timeout aktif: {TIMEOUT_DETIK} detik (settimeout)")

    try:
        client_socket.connect((target_host, target_port))
        print(f"[STATUS] Sukses terhubung dengan Server {target_host}:{target_port}!")
        print("[PETUNJUK] Ketik kalimat bebas, 'calc: <operasi>', 'test_delay', atau 'exit'\n")

        while True:
            pesan_input = input("Client > ")
            if not pesan_input.strip():
                print("[PERINGATAN] Pesan tidak boleh kosong.")
                continue

            client_socket.sendall(pesan_input.encode('utf-8'))

            if pesan_input.strip().lower() in ['exit', 'quit']:
                print("[INFO] Menunggu konfirmasi penutupan dari server...")

            balasan_bytes = client_socket.recv(BUFFER_SIZE)
            if not balasan_bytes:
                print("[SERVER CLOSED] Server menutup koneksi secara sepihak.")
                break

            print(balasan_bytes.decode('utf-8'))

            if pesan_input.strip().lower() in ['exit', 'quit']:
                break

    except socket.timeout:
        print("\n" + "!" * 65)
        print(f"[TIMEOUT ERROR] Server tidak merespon dalam {TIMEOUT_DETIK} detik!")
        print("[ANALISIS] Blocking I/O dibatalkan oleh socket.timeout.")
        print("!" * 65)

    except ConnectionRefusedError:
        print("\n[KONEKSI GAGAL] Connection Refused! Server belum aktif atau port salah.")
        print("[SOLUSI] Pastikan server.py sudah dijalankan terlebih dahulu.")

    except (ConnectionResetError, BrokenPipeError):
        print("\n[KONEKSI TERPUTUS] Koneksi ke server terputus mendadak.")

    except KeyboardInterrupt:
        print("\n[USER ABORT] Program dihentikan dengan Ctrl+C.")

    except Exception as e:
        print(f"\n[ERROR TAK TERDUGA] {e}")

    finally:
        client_socket.close()
        print("[STATUS] Soket klien telah ditutup. Selesai.\n")


if __name__ == "__main__":
    main()