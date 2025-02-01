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

print(dict([['name','Dicoding'],['age',17]]))


# KUISS
"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000

# TODO: Silakan buat kode Anda di bawah ini.
if dico >=500000:
    diskon = 10/100 * dico
else:
    diskon= dico
total_harga = dico - diskon
print(diskon)
print(total_harga)

# one liner
x=1
y=2
z=3
x,y,z = z,x,y
print(x)
print(y)

# LIST KOMPREHENSION
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

# KUISS
"""
TODO:
Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
- variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

Tips:
Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
"""

# TODO: Silakan buat kode Anda di bawah ini.
# evenNumber = [i%2==0 for i in range(501)]
# print(evenNumber)
evenNumber = []
# for i in range(501):
#     if i % 2 == 0:
#         evenNumber.append(i)
# print(evenNumber)

evenNumber = [i for i in range(501) if i%2 == 0]
print(evenNumber)

# try except
x=2
try:
    print(0.0+"tr")
except:
    print("tidak bisa boss")
z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")

var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

# error sengaja raise
# var = -1
# if var < 0:
#     raise ValueError("Bilangan negatif tidak diperbolehkan")
# else:
#     for i in range(var):
#         print(i+1)


for i in range(1,3):
    for j in range(1,3):
        print(i,j)


# array dipython itu list
x = [1, 2, 3, 4, 5] #list
# array
import array
x = array.array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))

siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
for i in siswa:
    print(i-1)

# deklarasi
var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)
print(type(var_arr))

var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")

# two pointer 
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)

# KUISS
"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah, 
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""
# Jangan ubah kode ini
var_array = [i for i in range(101)]

# TODO: Silakan buat kode Anda di bawah ini.
nilai = 0
for i in range(len(var_array)):
    nilai += i

result = nilai/len(var_array)
print(result)


# MATRIKS
matriks = [[0 for j in range(4)] for i in range(3)]
print(matriks)

# Membuat matriks 2x2
var_mat = [[5, 0],
          [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j]*2

print(def_mat)


# METHOD ATAU FUNGSI
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)

# FUNGSI DENGAN TUPLE
# JIKA PARAMETER ADA / MAKA ARGUMEN TANPA NAMA VARIABEL, JIKA PARAMETER ADA * MAKA ARGUMEN DENGAN NAMA VARIABEL
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

# FUNGSI DENGAN DICTIONARY KEY AND VALUE
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

# FUNGSI DENGAN LAMDA EXSPRESION
# dari ini: 
# def func(args):
#     return ret_val

# berubah jadi ini :
# func = lambda args: ret_val

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))


# KUISS
"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.
def minimal(a,b):
    if a>b :
      return b
    elif a==b :
      return a
    else :
        return a
  
cetak = minimal(5,3)
print(cetak)

# fungsi
# def perhitungan(a,b):
#     nilai = a * 2
#     nilai2 = b * 2
#     jumlah = nilai+nilai2
#     return print("jumlahnya adalah %i" % (jumlah))

# inputA = int(input("masukkan nilai A"))
# inputB = int(input("masukkan nilai B"))
# perhitungan(inputA, inputB)

# OOP
class Mobil:
    # Atribut
    warna = "Merah"

mobil_1 = Mobil()
print(mobil_1.warna)

# class construtor agar jika merubah atribut nilainya juga tidak ikut berubah
class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'
        
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        
mobil_1 = Mobil('Merah', 'DicodingCar', 160)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

# DEKORATOR
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

# METODE DARI OBJEK
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)


# METODE SECARA STATIS
class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()


# METODE DARI KELAS
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

# INHERITANCE (PEWARISAN)
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)
mobil_1.tambah_kecepatan()
print(mobil_1.kecepatan)

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

# OVERRIDE
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)
print(mobil_sport_1.warna)


# SUPER
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

# KUISS
"""
TODO:
1. Buatlah class bernama Animal dengan ketentuan:
    - Memiliki properti:
      - name: string
      - age: int
      - species: string
    - Memiliki constructor untuk menginisialisasi properti:
      - name
      - age
      - species
2. Buatlah class bernama Cat dengan ketentuan:
    - Merupakan turunan dari class Animal
    - Memiliki method:
      - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
        "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
      - bernama "suara" yang akan mengembalikan nilai string "meow!"
 3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
    - Atribut name bernilai: "Neko"
    - Atribut age bernilai: 3
    - Atribut species bernilai: "Persian".
"""

#TODO: Silakan buat kode Anda di bawah ini.
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    def suara(self):
        return "meow!"

myCat = Cat("Neko", 3, "Persian")
print(myCat.deskripsi())
print(myCat.name)