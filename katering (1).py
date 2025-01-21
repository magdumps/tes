import streamlit as st

def tampilkan_menu(menu):
    st.subheader("Menu Katering")
    for item, harga in menu.items():
        st.write(f"- {item}: Rp{harga:,}")

def pesan_makanan(menu):
    st.subheader("Pesan Makanan")
    pesanan = {}
    for item, harga in menu.items():
        jumlah = st.number_input(f"Jumlah {item} (Rp{harga:,}):", min_value=0, step=1, key=item)
        if jumlah > 0:
            pesanan[item] = jumlah
    return pesanan

def hitung_total_harga(menu, pesanan):
    total_harga = 0
    for item, jumlah in pesanan.items():
        total_harga += menu[item] * jumlah
    return total_harga

def tampilkan_pesanan(menu, pesanan):
    if pesanan:
        st.subheader("Detail Pesanan")
        for item, jumlah in pesanan.items():
            st.write(f"- {item} x {jumlah} = Rp{menu[item] * jumlah:,}")
        total_harga = hitung_total_harga(menu, pesanan)
        st.write(f"**Total Harga: Rp{total_harga:,}**")
    else:
        st.write("Anda belum memesan apa pun.")

def login_admin():
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        if username == "admin" and password == "admin123":
            st.success("Login admin berhasil!")
            return True
        else:
            st.error("Login admin gagal.")
    return False

def menu_admin():
    st.subheader("Menu Admin")
    st.write("Fitur admin belum tersedia.")

# Program utama
menu = {
    "Nasi Goreng": 25000,
    "Mie Goreng": 20000,
    "Ayam Geprek": 30000,
    "Sate Ayam": 35000,
    "Es Teh Manis": 5000,
    "Jus Jeruk": 10000,
}

st.title("Sistem Katering")
pilihan = st.radio("Pilih Mode:", ("Pengguna", "Admin"))

if pilihan == "Pengguna":
    tampilkan_menu(menu)
    pesanan = pesan_makanan(menu)
    tampilkan_pesanan(menu, pesanan)

elif pilihan == "Admin":
    if login_admin():
        menu_admin()
