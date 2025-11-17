# fungsi args dan kwargs

# ringkasan fungsi dengan args
# fungsi ini menerima jumlah argumen yang tidak terbatas
# berupa tuple
def fungsi_args(*args):
    return sum(args)
print(fungsi_args(1, 2, 3))  # Output: 6

# ringkasan fungsi dengan kwargs
# fungsi ini menerima argumen kunci-nilai yang tidak terbatas
# berupa dictionary
def fungsi_kwargs(**kwargs):
    return kwargs
print(fungsi_kwargs(nama="Alice", umur=25))  # Output: {'nama': 'Alice', 'umur': 25}

# penggunaan args tidak harus menggunakan nama 'args'
def fungsi_bebas(*angka):
    return angka
# begitu juga dengan kwargs
def fungsi_bebas_kwargs(**data):
    return data

# lambda function
# fungsi anonim yang biasanya digunakan untuk operasi sederhana
tambah = lambda x, y: x + y
print(tambah(5, 3))  # Output: 8

# list comprehension
# cara singkat untuk membuat list baru dari iterable

# tanpa list comprehension
hasil = []
for i in range(10):
    hasil.append(i * 2)

# dengan list comprehension

hasil = [i * 2 for i in range(10)]
# hasil sama seperti di atas

# dengan kondisi
hasil_genap = [i for i in range(10) if i % 2 == 0]

# dictionary comprehension

# cara singkat untuk membuat dictionary baru dari iterable
# tanpa dictionary comprehension
hasil_dict = {}
for i in range(5):
    hasil_dict[i] = i * i
    
# dengan dictionary comprehension
hasil_dict = {i: i * i for i in range(5)}
# hasil_dict sama seperti di atas

# contoh dictionary comprehension menggunakan list menjadi key dan panjang string sebagai value
user = ["miru", "andi", "budi"]
dict_user = {u: len(u) for u in user}
print(dict_user)  # {'miru': 4, 'andi': 4, 'budi': 4}