# 1. Fungsi register_user(**data)

import  random

def register_user(**data):
    data = {"id": random.randint(100000, 999999), **data}
    return data
print(register_user(name="Mirul", email="mirul@gmail.com", age=30))

# 2.  List comprehension: 1–50, hanya bilangan dibagi 3

list_bilangan = [i for i in range(1, 51) if i % 3 == 0]
print(list_bilangan)

# 3. Dictionary comprehension dari list nama

nama_list = ["mirul", "andi", "budi", "cici"]
dict_nama = {nama: len(nama) for nama in nama_list}
# print(dict_nama)

# 4.  function untuk menghitung total harga dengan diskon
def calculate_total(*prices):
    total = sum(prices)
    return total
print(calculate_total(10000, 20000, 30000))  # Output: 60000

# 6. Filter umur di atas 18 tahun
users = [ 
    {"name": "amir", "age": 17},
    {"name": "budi", "age": 20}, 
    {"name": "cici", "age": 15}, 
    {"name": "dedi", "age": 30}]

filtered_users = [user for user in users if user["age"] > 18]
print(filtered_users)