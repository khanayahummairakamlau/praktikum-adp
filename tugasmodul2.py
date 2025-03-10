
print("===Daftar Menu Makanan===")
print("Menu         Harga")
print("Ayam         Rp20000")
print("Sapi         Rp35000")
print("Cumi-Cumi    Rp45000")

menu = input('Masukkan menu yang anda pesan :').lower()

if menu == "ayam":
    harga = 20000
elif menu == "sapi" :
    harga = 35000
else :
    harga = 45000

jarak = float(input('Masukkan jarak rumah anda ke restoran (dalam km) :'))

if jarak < 1 :
    ongkir = 0
elif 1<=jarak<=3 :
    ongkir = 7000
else :
    ongkir = 15000

total = harga + ongkir

print(f'Biaya total pesanan anda adalah Rp{total}')
















    