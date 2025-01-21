!pip install streamlit
import streamlit as st
def tampilkan_menu():
    menu = {
        "Nasi Goreng": 25000,
        "Mie Goreng": 20000,
        "Ayam Geprek": 30000,
        "Sate Ayam": 35000,
        "Es Teh Manis": 5000,
        "Jus Jeruk": 10000,
    }
    print("Menu Katering:")
    for item, harga in menu.items():
        print(f"- {item}: Rp{harga:,}")

def pesan_makanan():
    tampilkan_menu()
    pesanan = {}
    while True:
        item = input("Masukkan nama makanan (atau ketik 'selesai' untuk selesai): ")
        if item.lower() == "selesai":
            break
        if item in menu:
            jumlah = int(input(f"Masukkan jumlah {item}: "))
            pesanan[item] = jumlah
        else:
            print("Makanan tidak ditemukan di menu.")
    return pesanan

def hitung_total_harga(pesanan):
    total_harga = 0
    for item, jumlah in pesanan.items():
        total_harga += menu[item] * jumlah
    return total_harga

def tampilkan_pesanan(pesanan):
    print("Pesanan Anda:")
    for item, jumlah in pesanan.items():
        print(f"- {item} x {jumlah}")
    total_harga = hitung_total_harga(pesanan)
    print(f"Total Harga: Rp{total_harga:,}")

def login_admin():
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "admin123":
        print("Login admin berhasil!")
        return True
    else:
        print("Login admin gagal.")
        return False

def menu_admin():
    while True:
        print("\nMenu Admin:")
        print("1. Tambah Menu")
        print("2. Edit Menu")
        print("3. Hapus Menu")
        print("4. Logout")
        pilihan = input("Pilihan Anda: ")

        if pilihan == "1":
            # Tambahkan logika untuk menambah menu
            pass
        elif pilihan == "2":
            # Tambahkan logika untuk mengedit menu
            pass
        elif pilihan == "3":
            # Tambahkan logika untuk menghapus menu
            pass
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

# Program utama
menu = {
    "Nasi Goreng": 25000,
    "Mie Goreng": 20000,
    "Ayam Geprek": 30000,
    "Sate Ayam": 35000,
    "Es Teh Manis": 5000,
    "Jus Jeruk": 10000,
}  # Inisialisasi menu di luar fungsi

st.title("Sistem Katering")
pilihan = st.radio("Pilih Mode:", ("Pengguna", "Admin"))

if pilihan == "Pengguna":
    st.header("Menu Makanan")
    tampilkan_menu()  # Memanggil fungsi untuk menampilkan menu

    st.header("Pesan Makanan")
    pesanan = pesan_makanan()  # Memanggil fungsi untuk memesan makanan

    st.header("Detail Pesanan")
    tampilkan_pesanan(pesanan)  # Memanggil fungsi untuk menampilkan pesanan

elif pilihan == "Admin":
    st.header("Login Admin")
    if login_admin():  # Memanggil fungsi untuk login admin
        menu_admin()  # Memanggil fungsi menu admin jika login berhasil
    else:
        st.error("Login gagal.")

while True:
    print("\nSelamat datang di Sistem Katering!")
    print("1. Pengguna")
    print("2. Login Admin")
    print("3. Keluar")
    pilihan = input("Pilihan Anda: ")

    if pilihan == "1":
        pesanan = pesan_makanan()
        tampilkan_pesanan(pesanan)
    elif pilihan == "2":
        if login_admin():
            menu_admin()
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid.")

print("Terima kasih!")