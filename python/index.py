gretting = 'hello world!!'
print(gretting)

additional = 2+2
result = additional - 1
print(result)

for i in range(2):
    print(i)

for i in range(1,3):
    print(i)

for i in range(1,10,2):
    print(i)


i=1
while i <= 5:
    print(i)
    i+=1


for i in range(1, 5):
    if i%2 == 0:
        print(i, "= genap")

# input
# nama = str(input("Masukkan nama kamu : "))
# print(nama)


# TO DO KUIS VARIABEL

gretting = "Saya mulai belajar python"
print(gretting)


# tipe data
umur = 18
harga = 50000.0
string = "103 satu"

print(type(umur))
print(type(harga))
print(type(string))

x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

x = 'Dicoding'
print(x[2:])

name = "Rasio F"
print(f"Hello, nama saya {name}")

name = "RAS"
umr = 22
print("Nama saya %s dan umur saya %i" % (name, umr))

name = "Perseus Evans"
print("Nama saya {}".format(name))

arrayList = [1, "nama", "Rasio", "umur", 22]
for i in range(len(arrayList)):
    print(arrayList[i])

arrayList = [1, "nama", "Rasio", "umur", 22]
tampung = " ".join(map(str, arrayList))  # Konversi semua elemen ke string
print(tampung)

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:7:3])
print(x[1:])
print(x[:3])


# tuple tidak bisa dirubah nilainya atau tergantikan
x = (1, "Dicoding", 1+3j)
print(type(x))

# bisa untuk menghilangkan data dupikat
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)


# key and value
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(type(x))

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(x ['name'])

# hapus data
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
del x['isMarried']
print(x)

# konversi tipedata
print(int(5.6))
print(int(-5.6)) 

# konversi ke dictionary
print(dict([[1,2],[3,4]]))


# KUISS
"""
TODO:
Buatlah variabel firstName, lastName, age, isMarried dengan ketentuan:
- firstName: isi dengan nama depan Anda bertipe data string.
- lastName: isi dengan nama belakang Anda bertipe data string.
- age: isi dengan umur Anda bertipe data integer.
- isMarried: isi dengan status pernikahan Anda bertipe data boolean.

Catatan:
- Value variabel harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""

# TODO: Silakan buat kode Anda di bawah ini.
firstName = "Rasio"
lastName = "Fernandis"
age = 22
isMarried = False


# KUISS
"""
TODO:
Buatlah variabel dictionary dengan nama "data_diri",
variabel tersebut berisi identitas diri Anda berdasarkan ketentuan berikut.
- Memiliki key bernama "firstName":
    - Isi value dengan nama depan Anda, pastikan bertipe data string.
- Memiliki key bernama "lastName":
    - Isi value dengan nama terakhir Anda, pastikan bertipe data string.
- Memiliki key bernama "age":
    - Isi value dengan umur Anda, pastikan bertipe data integer.
- Memiliki key bernama "isMarried":
    - Isi value dengan status pernikahan Anda, pastikan bertipe data boolean.

Catatan:
- Value pada dictionary harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""


# TODO: Silakan buat kode Anda di bawah ini.
data_diri = {
    'firstName' : "Rasio",
    'lastName' : "Fernandis",
    'age' : 22,
    'isMarried' : False
    }

# uppercase and lowercase
kata = 'DICODING'
kata = kata.lower()
kataUpper = kata.upper()
print(kata)
print(kataUpper)

# hapus whitespace atau spasi
print("Dicoding          ".rstrip())
print("           Dicoding".lstrip())
print("         Dicoding          ".strip())

kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

# awal kalimat atau kata deteksi
print('Indonesia Dicoding '.startswith('Indonesia'))
# akhir kata
print('Dicoding Indonesia'.endswith('Indonesia'))

# memisahkan 
print('Dicoding Indonesia !'.split())

# gabungkan
print('123'.join(['Dicoding','Indonesia']))

# ganti elemen string
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

kata = 'DICODING'
print(kata.isupper())
kata = 'dicoding'
print(kata.islower())
kata = 'dicoding'
print(kata.isalpha())
kata = 'dicoding123'
print(kata.isalnum())
print('123'.isdecimal())
print('         '.isspace())
print('Dicoding Indonesia'.istitle())

teks = 'Cod'
tambah_number = teks.zfill(5)
print(tambah_number)

print('Dicoding'.rjust(20))
print('Dicoding'.rjust(20, '!'))
print('Dicoding'.ljust(20))
print('Dicoding'.center(10, '-'))

# panjang data dan jumlah
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))
# String
contoh_list = "Belajar Python"
print(contoh_list)
print(len(contoh_list))

contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_list)
print(len(contoh_list))

# min max nilai data angka
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# untuk mengetahui jumlah data muncul berapa kali atau bisa dikatakan ini adalah modus
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
# untuk string
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# cek ada tidaknya kalimat data di teks
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# multiple variabel tuple
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

# sort 
# jika tipedata sama bisa
# dan jika sort ada kapital pada teks maka akan didahulukan
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)
# jika kebalikan
kendaraan =  ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan)

kendaraan = ['MOTOR', 'MOBIL', 'Helikopter', 'Pesawat']
for i in range(len(kendaraan)):
    kendaraan[i]=kendaraan[i].lower()
kendaraan.sort()
print(kendaraan)
# atau ini
kendaraan = ['MOTOR', 'MOBIL', 'Helikopter', 'Pesawat']
kendaraan_lower = [item.lower() for item in kendaraan]
cetakHasil = sorted(kendaraan_lower)  # Mengembalikan daftar baru yang diurutkan
print(cetakHasil)

# KUISSS
"""
TODO:
Diberikan sebuah variabel berisi nilai list dengan nama "var_list". 
Berdasarkan list tersebut, cari hal-hal berikut ini:
- Panjang list tersebut dan simpan dengan nama variabel "panjang".
- Nilai maksimal list tersebut dan simpan dengan nama variabel "maksimal".
- Nilai minimal list tersebut dan simpan dengan nama variabel "minimal".
- Berapa banyak angka 605132 dalam list tersebut dan simpan dalam variabel bernama "banyak"

Tips:
- Anda bisa menggunakan berbagai kode yang ada di materi operasi, 
  tidak diperbolehkan memasukan nilai secara langsung.
"""

# Jangan ubah kode ini
var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250
]

# TODO: Buat kode Anda di bawah ini
panjang = len(var_list)
maksimal = max(var_list)
minimal = min(var_list)
banyak = var_list.count(605132)
print(panjang)
print(maksimal)
print(minimal)
print(banyak)
