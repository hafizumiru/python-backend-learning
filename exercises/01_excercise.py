# 1. Buat variabel yang menyimpan: nama, umur, tinggi, status menikah. Print semuanya.

nama = "Mirul"
umur = 30
tinggi = 170
status_menikah = False

print("Nama:", nama)
print("Umur:", umur)   
print("Tinggi:", tinggi)
print("Status Menikah:", status_menikah)

# 2. Hitung luas persegi panjang dari panjang=8, lebar=5.

panjang = 8
lebar = 5
luas = panjang * lebar
print("Luas Persegi Panjang:", luas)

# 3. Buat list berisi 5 angka, lalu print angka terbesar.

angka_list = [12, 45, 7, 23, 34]
angka_terbesar = max(angka_list)
print("Angka Terbesar:", angka_terbesar)

# 4. Buat dictionary user dengan key: name, email, age. Lalu print email.

user = {
    "name": "Mirul",
    "email": "mirul@gmail.com",
    "age": 30
}
print("Email:", user["email"])

# 5. Loop: print angka 1–20 tapi hanya yang genap.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        
# 6. Buat fungsi is_login_allowed(age) → return True jika umur ≥ 17.

def is_login_allowed(age):
    return age >= 17
print(is_login_allowed(30))  # True

# 7. Buat fungsi yang menerima list angka dan mengembalikan totalnya.

def total_angka(angka_list):
    return sum(angka_list)
print(total_angka([1, 2, 3, 4, 5]))  # 15

# 8. Simulasi login sederhana:
#     input username
#     jika username == "admin": print "Welcome admin"
#     else: print "User not allowed"

def login(username):
    if username == "admin":
        return "Welcome admin"
    return "User not allowed"

print(login(input("Masukkan username: ")))

# 9. Buat loop while yang berjalan 5 kali dan print "Processing..."

count = 0
while count < 5:
    print("Processing...")
    count += 1
    
# 10. Tangani error pembagian angka dengan try/except:
#     Jika user masukkan 0 → tampilkan “Error: divide by zero”.

def bagi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: divide by zero"
print(bagi(10, 0))  # Error: divide by zero 
    
