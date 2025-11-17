# Contoh untuk setiap tipe data di Python

# str → teks
teks = "Halo, dunia!"

# int → angka bulat
angka_bulat = 42

# float → desimal
angka_desimal = 3.14

# bool → True/False
nilai_boolean = True

# list → array
array = [1, 2, 3, 4, 5]

# tuple → tidak bisa diubah
tuple_data = (1, 2, 3)

# dict → key-value
kamus = {
    "nama": "John",
    "umur": 30
}

# None → kosong
kosong = None

# Menampilkan semua tipe data
print(teks)
print(angka_bulat)
print(angka_desimal)
print(nilai_boolean)
print(array)
print(tuple_data)
print(kamus)
print(kosong)

# Contoh penggunaan operator

# Operator aritmatika
penjumlahan = 10 + 5
pengurangan = 10 - 5
perkalian = 10 * 5
pembagian = 10 / 5
modulus = 10 % 3
pangkat = 2 ** 3

# Operator perbandingan
lebih_besar = 10 > 5
lebih_kecil = 10 < 5
sama_dengan = 10 == 10
tidak_sama = 10 != 5

# Operator logika
dan = True and False
atau = True or False
negasi = not True

# Menampilkan hasil operator
print("Penjumlahan:", penjumlahan)
print("Pengurangan:", pengurangan)
print("Perkalian:", perkalian)
print("Pembagian:", pembagian)
print("Modulus:", modulus)
print("Pangkat:", pangkat)

print("Lebih Besar:", lebih_besar)
print("Lebih Kecil:", lebih_kecil)
print("Sama Dengan:", sama_dengan)
print("Tidak Sama:", tidak_sama)

print("Logika AND:", dan)
print("Logika OR:", atau)
print("Logika NOT:", negasi)

# Contoh control flow

# If-else
angka = 10
if angka > 5:
    print("Angka lebih besar dari 5")
else:
    print("Angka tidak lebih besar dari 5")

# For loop
for i in range(5):
    print(f"Perulangan ke-{i}")

# While loop
hitung = 0
while hitung < 3:
    print(f"Hitung: {hitung}")
    hitung += 1
    
# Contoh fungsi
def sapa(nama):
    """Fungsi untuk menyapa seseorang."""
    return f"Halo, {nama}!"

def hitung_luas_persegi(panjang, lebar):
    """Fungsi untuk menghitung luas persegi panjang."""
    return panjang * lebar

# Memanggil fungsi
print(sapa("Alice"))
print("Luas persegi panjang:", hitung_luas_persegi(5, 3))

# Contoh error handling
try:
    angka = int(input("Masukkan sebuah angka: "))
    print(f"Angka yang dimasukkan adalah {angka}")
except ValueError:
    print("Input tidak valid! Harus berupa angka.")
finally:
    print("Program selesai.")