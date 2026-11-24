import socket
import time

HOST = '0.0.0.0'
PORT = 65432
BUFFER_SIZE = 1024


def proses_request(pesan_klien: str) -> str:
    pesan_clean = pesan_klien.strip()

    if pesan_clean.lower() == "test_delay":
        print("[SERVER] Menerima instruksi uji timeout: tidur selama 12 detik...")
        time.sleep(12)
        return "RESPON_TERLAMBAT: Selesai tidur 12 detik."

    if pesan_clean.lower().startswith("calc:"):
        ekspresi = pesan_clean[5:].strip()
        try:
            hasil = eval(ekspresi, {"__builtins__": None}, {})
            return f"[HASIL KALKULASI] {ekspresi} = {hasil}"
        except Exception as e:
            return f"[ERROR KALKULASI] Format tidak valid: {str(e)}"

    kata_list = pesan_clean.split()
    total_kata = len(kata_list)
    total_karakter = len(pesan_clean)
    teks_terbalik = pesan_clean[::-1]

    balasan = (
        f"\n--- [BALASAN PEMROSESAN SERVER] ---\n"
        f"Teks Asli        : '{pesan_clean}'\n"
        f"Teks Terbalik    : '{teks_terbalik}'\n"
        f"Statistik Teks   : {total_kata} Kata | {total_karakter} Karakter\n"
        f"Status Server    : Sukses Diproses pada Port {PORT}"
    )
    return balasan


def main():
    print("=" * 65)
    print("      SERVER SOCKET JARINGAN KOMPUTER (IF25-21008) - ITERA")
    print("=" * 65)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            server_socket.bind((HOST, PORT))
            server_socket.listen(5)
            print(f"[STATUS] Server aktif dan mendengarkan pada {HOST}:{PORT}")
            print("[INFO] Menunggu koneksi dari klien... (Ctrl+C untuk berhenti)")

            while True:
                conn, client_addr = server_socket.accept()
                with conn:
                    print(f"\n[KONEKSI BARU] Klien: {client_addr[0]}:{client_addr[1]}")
                    while True:
                        data_bytes = conn.recv(BUFFER_SIZE)
                        if not data_bytes:
                            print(f"[DISCONNECT] Klien {client_addr} menutup koneksi.")
                            break

                        pesan_masuk = data_bytes.decode('utf-8')
                        print(f"[REQUEST DITERIMA] Dari {client_addr}: '{pesan_masuk}'")

                        if pesan_masuk.strip().lower() in ['exit', 'quit']:
                            conn.sendall("KONEKSI_DITUTUP: Sampai jumpa!".encode('utf-8'))
                            print(f"[TERMINASI] Konfirmasi penutupan dikirim ke {client_addr}")
                            break

                        hasil_proses = proses_request(pesan_masuk)
                        conn.sendall(hasil_proses.encode('utf-8'))
                        print(f"[RESPON TERKIRIM] Hasil dikirim ke {client_addr}")

        except KeyboardInterrupt:
            print("\n[SHUTDOWN] Ctrl+C diterima. Menutup server...")
        except Exception as err:
            print(f"[FATAL ERROR] {err}")
        finally:
            print("[STATUS] Server soket telah ditutup.")


if __name__ == "__main__":
    main()