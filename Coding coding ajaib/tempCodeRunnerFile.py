#BASIC PYTHON 1 #
print('#BASIC PYTHON 1 #')
print("\n")
print('big cooc')
print('helloooo')
"""python adalah bahasa pemograman yang berjalan layaknya penerjemah. Python akan mengambil
 source code dan akan langsung menjalankannya/
menampilkannya sesuai urutan tanpa harus membuat compile """ #Comment Multiline
"""python bisa compile source code ke dalam bentuk bytecode daripada syntax
Contoh membuat compile source code ke dalam bentuk bytcode (lakukan ini di terminal) : python
-m py_compile second.py"""
print("\n")
print('##BASIC PYTHON 1 ##')
##BASIC PYTHON 1 ##
print(2*"\n")

#DATA, VARIABEL, ARGUMEN 2 #
print('#DATA, VARIABEL, ARGUMEN 2 #')
print('\n')

#Penempatan data/ Assignment
print('penempatan data/ Assignment')
"""Variabel di python sama seperti di matematika, dia bisa menjadi apa saja tergantung
nilai/data yang dimasukkan. Contoh : a = 10. Ini berarti 10 (Data) mendefinisikan sebagai/
menempatkan variabel a, yang berarti sekarang a "adalah" 10 dan tidak sebaliknya."""

a = 10
ab = 29

print('nilai a = ', a)
print('nilai ab = ', ab)
meme = 23
print('variabel meme setelah dimasukkan data menjadi ', meme)
print('\n')

#Penamaan
print('Penamaan')
"""Dalam penamaan variabel, untuk penulisan spasi tidak bisa, untuk mengganti kompensasi atas
hal tersebut maka dapat digunakan "_" sebagai ganti daari spasi"""
"""Dalam penamaan variabel, tidak bisa menaruh angka didepan, seperti "10juta" """

harga_minyak = 14000
HargaMinyak = 15000
Harga_1liter_minyak = 13000

print('harga_minyak =',harga_minyak)
print('HargaMinyak =',HargaMinyak)
print('Harga_1liter_minyak =', Harga_1liter_minyak)
print('\n')

#Penempatan Data Kedua/ the second assignment
print('Penempatan Data Kedua/ the second assignment')
"""Penempatan Data/Nilai bisa dilakukan pada variabel yang sama, ini berarti sebuah variabel
bisa ditempatkan pada banyak data/nilai sekaligus mengikuti alur sebuah program. Dimana sebuah
variabel bisa diubah datanya ditengah tengah program. Contoh data a sudah dimasukkan oleh 10,
lalu pada program berikutnya data a dimasukkan angka 9. Maka data terakhirlah yang akan muncul
Jika ada pemanggilan ulang """

harga_minyak = 20000
HargaMinyak = 30000
Harga_1liter_minyak = 50000
print('harga_minyak =', harga_minyak)
print('HargaMinyak =', HargaMinyak)
print('Harga_1liter_minyak =', Harga_1liter_minyak)
print('\n')

#Indirect Assignment
print('Indirect Assignment')
"""Indirect assignment adalah penempatan variabel kepada variabel yang sudah dimasukkan
data/assignment (bukan langsung kepada data)"""

x = harga_minyak
z = HargaMinyak
y = Harga_1liter_minyak

print('x = harga_minyak =', x)
print('y = HargaMinyak =', y)
print('z = Harga_1liter_minyak', z)
print('##DATA, VARIABEL, ARGUMEN 2 ##')
print(2*'\n')

#JENIS JENIS DATA 3
print('#JENIS JENIS DATA 3 #')
print('\n')

#Integer
print('integer')
"""Integer adalah tipe data angka bilangan bulat, seperti 4, 69, 200, 348, dan seterusnya
. Dan bukan angka desimal maupun pecahan seperti 2.1 ; 2.3 ; 3.4 dan seterusnya. biasanya 
disingkat int"""

angka_integer = 400
print('angka_integer =', angka_integer, ', bertipe ', type(angka_integer))
print('\n')

#Float
print('float')
"""Float adalah tipe data angka desimal, seperti 4.5, 5.5, 3.5, 4.4, dan seterusnya"""
angka_float = 4.5
print('angka_float =', angka_float, ', bertipe ', type(angka_float))
print('\n')

#String 
print('String')
"""String adalah tipe data kumpulan karakter dalam tanda kutip baik huruf
maupun angka atau apapun, biasanya disingkat str"""
huruf_string = "Saya pergi ke pasar"
print('huruf_string =', huruf_string, ', bertipe ', type(huruf_string))
print('\n')


#Boolean
print('Boolean')
"""Boolean adalah tipe data biner, yaitu salah satu
antara True atau False, biasanya disingkat bool"""
data_boolean = True
print('data_boolean = ',data_boolean, ', bertipe', type(data_boolean))
data_boolean = False
print('data_boolean = ',data_boolean,  ', bertipe', type(data_boolean))
print('\n')


#Complex
print('Complex')
"""Tipe data complex adalah tipe data yang melibatkan bilangan imajiner.
Contoh : complex(4,2). Dimana 2 adalah bilangan imajiner"""
data_complex = complex(5,3)
print('data_complex = ',data_complex,  ', bertipe', type(data_complex))
print('\n')


#Bahasa C
print('Bahasa C')
"""python bisa menggunakan tipe data dari bahasa C, seperti c_double, c_char,
caranya adalah dengan mengetik from ctypes import (masukkan tipe data dari bahasa c)"""
from ctypes import c_double
data_c_double = c_double(3.4)
print('data_c_double = ',data_c_double)
print ('bertipe', type(data_c_double))
print("\n")
##DATA, VARIABEL, ARGUMEN 2##
print('##DATA, VARIABEL, ARGUMEN 2 ##')
print("\n")

#CASTING DATA 3 #
print("# CASTING DATA 3 #")
"""mengubah suatu tipe data ke tipe yang lain. Untuk mengubah tipe suatu data ke data yang lain
, masukkan terlebih dahulu data yang inin tipenya diubah ke suatu variabel. Lalu Masukkan 
variabel tersebut ke tipe data yang diinginkan."""
print("\n")

print('# Casting dari tipe data integer')
a = 100
print('a =',  a, type(a))
print("\n")

print('Casting ke Float')
a_float = float(a)
print('a_float =', a_float, type(a_float) )
print("\n")

print('Casting ke Bool')
"""Untuk tipe data Bool setiap angka yang selain 0 akan menghasilkan True, sebaliknya akan 
menghasilkan False """
a_bool = bool(a)
print('a_bool =', a_bool, type(a_bool))
print("\n")

print('Casting ke string')
a_str = str(a)
print('a_str =', a_str, type(a_str))
print('\n')

print('# Casting dari float')
b = 10.6
print('b', b, type(b))
print('\n')

print('Casting ke Int')
'''Saat mengubah tipe data dari float ke inteer, maka akan dibylatkan ke bawah'''
b_int = int(b)
print('b_int =', b_int, type(b_int))
print('\n')

print('Casting ke str')
b_str = str(b)
print('b_str =', b_str, type(b_str))
print('\n')

print('Casting ke bool')
b_bool = bool(b)
print("b_bool =", b_bool, type(b_bool))
print('\n')

print('# Casting dari Boolean')
b = True
print('b =', b, type(b))
print('\n')

print('Casting ke Int')
'''Saat casting dari tipe data boolean ke integer atau float, jika data boolean mengatakan true
maka akan menghasilkan angka 1 atau 1.0, jika false akan menghasilkan angka 0'''
b_int = int(b)
print('b_int =', b_int, type(b_int))
print('\n')

print('Casting ke str')
b_str = str(b)
print('b_str =', b_str, type(b_str))
print('\n')

print('Casting ke float')
b_float = float(b)
print("b_float =", b_float, type(b_float))
print('\n')

print('# Casting dari String')
b = '10'
print('b =', b, type(b))
print('\n')

print('Casting ke Int')
'''Untuk Casting dari string ke integer, maka angka string haurs karakter angka'''
b_int = int(b)
print('b_int =', b_int, type(b_int))
print('\n')

print('Casting ke bool')
'''Jika string kosong (dimana tidak ada apa apa didalam tanda kutip), maka data boolean akan 
menghasilkan False, dan sebaliknya'''
b_bool = bool(b)
print('b_bool =', b_bool, type(b_bool))
print('\n')

print('Casting ke float')
b_float = float(b)
print("b_float =", b_float, type(b_float))
print('\n')

##CASTING DATA 3 ##
print("## CASTING DATA 3 ##")
print('\n')

# MENGAMBIL INPUT DATA DARI USER 4 #
print('# MENGAMBIL INPUT DATA DARI USER 4 #')
"""Adalah proses memasukkan/mengambil data dara interface penggunea, seperti terminal"""
print('\n')

print('Mengambil input tipe data string')
"""Dalam kasus string, kita tidak perlu mengcasting tipe data dari source code"""

string = input('Masukkan data:')
print('string =', string, type(string))
print('\n')

print('Mengambil input tipe float dan integer')
'''Untuk menambil tipe data integer dan float, kita harus memngcasting tipe data input terlebih
dahulu'''

float = float(input('Masukkan data float :'))
print('float = ', float, type(float))

integer = int(input('Masukkan data integer :'))
print('integer =', integer, type(integer))
print('\n')

print('Mengambil input tipe data boolean')
'''Untuk mengambil tipe data boolean, kita harus casting tipe data input ke integer terlebih
dahulu, lalu casting lagi ke tipe data boolean'''
boolean = bool(int(input('Masukkan data boolean (0/1) :')))
print('boolean =', boolean, type(boolean))
print('\n')

## MENGAMBIL INPUT DATA DARI USER 4 ##
print('## MENGAMBIL INPUT DATA DARI USER 4 ##')
print('\n')

# OPERASI ARITMATIKA 5 #
print('# OPERASI ARITMATIKA 5')
'''Operasi aritmatika adalah operasi yang melibatkan penjumlahan, pengurangan, pembagian,
perkailan, dan laiinya. Operasi ini bisa dijalankan pada data, atau variabel yang sudah
dimasukkan data, bahkan menjadi data dari variabel itu sendiri'''
print('\n')

print('Operasi penjumlahan')
a = 5
b = 4
print('a =', a)
print('b =', b)
a_plus_b = a + b
print(a, "+", b, '=', a_plus_b)
print('a + 5 =', a + 5)
print('type a_plus_b', type(a_plus_b))
print('\n')

print('Operasi pengurangan')
a = 5
b = 4
print('a =', a)
print('b =', b)
a_mines_b = a - b
print(a, "-", b, '=', a_mines_b)
print('a - 5 =', a - 5)
print('type a_mines_b', type(a_mines_b))
print('\n')

print('Operasi perkalian')
a = 5
b = 4
print('a =', a)
print('b =', b)
a_times_b = a * b
print(a, "*", b, '=', a_times_b)
print('a * 5 =', a * 5)
print('type a_times_b', type(a_times_b))
print('\n')

print('Operasi pembagian')
a = 5
b = 4
print('a =', a)
print('b =', b)
a_divide_b = a / b
print(a, "/", b, '=', a_divide_b)
print('a / 5 =', a / 5)
print('type a_divide_b', type(a_divide_b))
print('\n')

print('Operasi perpangkatan')
a = 5
b = 4
print('a =', a)
print('b =', b)
a_power_b = a ** b
print(a, "**", b, '=', a_power_b)
print('a ** 5 =', a ** 5)
print('type a_power_b', type(a_power_b))
print('\n')

print('Operasi modulus')
'''Modulus adalah operasi yang menghasilkan angka sisa dari suatu pembagian'''
a = 5
b = 4
print('a =', a)
print('b =', b)
a_modulus_b = a % b
print(a, "%", b, '=', a_modulus_b)
print('a % 5 =', a % 5)
print('type a_modulus_b', type(a_modulus_b))
print('\n')

print('Operasi floor division')
"""adalah operasi pembagian yang menghasilkan pembulatan ke bawah"""
a = 5
b = 4
print('a =', a)
print('b =', b)
a_floor_division_b = a // b
print(a, "//", b, '=', a_floor_division_b)
print('a // 5 =', a // 5)
print('type a_floor_division_b', type(a_floor_division_b))
print('\n')

'''Prioritas operasi, jika ada operasi dalam jumlah besar maka operasi yang akan didahulukan
untuk dikerjakan terlebih dahulu adalah 
1. dalam kurung (),
2. pangkat atau ekponen, 
3. perkalian dan temannya, 
4. dan penjumlahan dan temannya'''

## OPERASI ARITMATIKA 5 ##
print('## OPERASI ARITMATIKA 5 ##')
print('\n')

# LATIHAN MENGGUNAKAN OPERASI INPUT DATA DAN OPERASI ARITMATIKA 6 #
print('# LATIHAN MENGGUNAKAN OPERASI INPUT DATA DAN OPERASI ARITMATIKA 6 #')
print('\n')

#Konversi dari celsius
print('# konversi dari celcius')
Celcius = int(input('Masukkan suhu Celscius:'))

fahrenheit = ((9/5) * Celcius) + 32
Reamur = (4/5) * Celcius
Kelvin = Celcius + 273
print('Suhu dalam Fahrenheit adalah ', fahrenheit, 'fahrenheit')
print('Suhu dalam Reamur adalah ', Reamur, 'Reamur')
print('Suhu dalam Kelvin adalah ', Kelvin, 'Kelvin')
print('\n')

#Konversi dari Fahrenheit
print('# konversi dari fahrenheit')
Fahrenheit = int(input('Masukkan suhu fahrenheit:'))

Celcius = (Fahrenheit - 32) * (5/9)
Reamur = (Fahrenheit - 32) * (4/9)
Kelvin = ((Fahrenheit - 32) * (5/9)) + 273
print('Suhu dalam Celcius adalah ', Celcius, 'Celcius')
print('Suhu dalam Reamur adalah ', Reamur, 'Reamur')
print('Suhu dalam Kelvin adalah ', Kelvin, 'Kelvin')
print('\n')

## LATIHAN MENGGUNAKAN OPERASI INPUT DATA DAN OPERASI ARITMATIKA 6 ##
print('## LATIHAN MENGGUNAKAN OPERASI INPUT DATA DAN OPERASI ARITMATIKA 6 ##') #EEZZZ BOZZZ YHAHAHAHA
print('\n')

# OPERASI KOMPARASI 7 #
print('# OPERASI KOMPARASI')
"""Hasil dari setiap operasi komparasi adalah boolean. Operator dari operasi komparasi adalah
1. >, <, lebih dari dan kurang dari
2. >=, <=, lebih dari sama dengan dan kurang dari sama dengan
3. ==, !=, sama dengan dan tidak sama dengan
4. is, is not, untuk membandingkan variabel/objek yang memakan/tersimpan di memori"""
print('\n')
a= 5
b= 7
print( 'a =', a)
print( 'b =', b)
print('\n')

print('kurang dari dan lebih dari')
print('a < b adalah', a < b)
print('a < 4 adalah', a < 4)
print('b < a adalah', b < a)
print('a > b adalah', a > b)
print('a > 4 adalah', a > 4)
print('b > a adalah', b > a)
print('\n')

print('kurang dari sama dengan dan lebih dari sama dengan')
print('a <= b adalah', a <= b)
print('a <= 4 adalah', a <= 4)
print('b <= a adalah', b <= a)
print('a >= b adalah', a >= b)
print('a >= 4 adalah', a >= 4)
print('b >= a adalah', b >= a)
print('\n')

print('sama dengan')
print('a == b adalah', a == b)
print('a == 4 adalah', a == 4)
print('b == a adalah', b == a)
print('a == b adalah', a == b)
print('a == 4 adalah', a == 4)
print('b == a adalah', b == a)
print('\n')

print('tidak sama dengan')
print('a != b adalah', a != b)
print('a != 4 adalah', a != 4)
print('b != a adalah', b != a)
print('a != b adalah', a != b)
print('a != 4 adalah', a != 4)
print('b != a adalah', b != a)
print('\n')

print('is dan is not')
print('a is b adalah', a is b)
print('a is 4 adalah', a is 4)
print('b is a adalah', b is a)
print('a is not b adalah', a is not b)
print('a is not 4 adalah', a is not 4)
print('b is not a adalah', b is not a)
print('\n')

# OPERASI KOMPARASI 7 #
print('# OPERASI KOMPARASI')
print('\n')

# OPERASI LOGIKA DAN BOOLEAN 8 #
print('# OPERASI LOGIKA DAN BOOLEAN #')
"""adalah operasi yang menentukan apakah sebuah data true atau false"""
print('\n')

#NOT
print('NOT')
'''Operasi boolean NOT adalah operasi yang mengubah data dari false
menjadi true dan sebaliknya'''
a = True
b = False
c = not a
d = not b
print('data a ', a)
print('data b ', b)
print('data c not a', c)
print('data d not b', d)
print('\n')

#OR
print('OR')
'''Or adalah operasi boolean yang menentukan sebuah data dari 
kumpulan data boolean, yang jika ada data boolean true dari kumpulan
data boolean tersebut, maka data yang akan ditentukan akan menjadi true
'''

a = False
b = True
c = True
d = a or b or c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a or b or c =', d)
print('\n')
a = False
b = False
c = True
d = a or b or c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a or b or c =', d)
print('\n')
a = False
b = False
c = False
d = a or b or c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a or b or c =', d)
print('\n')
a = True
b = True
c = True
d = a or b or c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a or b or c =', d)
print('\n')


#AND
print('AND')
'''AND adalah kebalikan dari OR'''

a = False
b = True
c = True
d = a and b and c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a and b and c =', d)
print('\n')
a = False
b = False
c = True
d = a and b and c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a and b and c =', d)
print('\n')
a = False
b = False
c = False
d = a and b and c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a and b and c =', d)
print('\n')
a = True
b = True
c = True
d = a and b and c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a and b and c =', d)
print('\n')

#XOR
print('XOR')
'''XOR adalah operasi yang menentukan sebuah data dari kumpuluan data boolean, jika dari 
kumpulan data tersebut jumlah true adalah ganjil, maka data yang akan ditentukan menjadi
true, dan sebaliknya'''

a = False
b = True
c = True
d = a ^ b ^ c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a ^ b ^ c =', d)
print('\n')
a = False
b = False
c = True
d = a ^ b ^ c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a ^ b ^ c =', d)
print('\n')
a = False
b = False
c = False
d = a ^ b ^ c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a ^ b ^ c =', d)
print('\n')
a = True
b = True
c = True
d = a ^ b ^ c
print('data a', a)
print('data b', b)
print('data c', c)
print('data d = a ^ b ^ c =', d)
print('\n')

## OPERASI LOGIKA DAN BOOLEAN 8 ##
print('## OPERASI LOGIKA DAN BOOLEAN ##')
"""adalah operasi yang menentukan apakah sebuah data true atau false"""
print('\n')

# LATIHAN OPERASI LOGIKA DAN KOMPARASI 9 #
print('# LATIHAN OPERASI LOGIKA DAN KOMPARASI 9 #')
''''Buat kode untuk mencari angka yang lebih dari 0 dan kurang dari 5, dan lebih dari 8
kurang dari 11'''
print('soal no. 1')
print('\n')

Data = float(input('Masukkan angka Lebih dari 0 dan kurang dari 5'
                   '\n dan \n lebih dari 8 dan kurang dari 11 = ' ))
apa_betul = ((Data > 0) and (Data < 5)) or ((Data > 8) and (Data < 11)) 
print(' apakah betul?', apa_betul)
print('\n')

''''Buat kode untuk mencari angka yang kurang dari 0, lebih dari 5 dan kurang dari 8, 
dan lebih dari 11'''
print('soal no. 2')
Data = float(input('Masukkan angka kurang dari nol \n Lebih dari 5 dan kurang dari 8 \n'
                   'dan lebih dari 11 = '))
apa_betul = (Data < 0) or ((Data > 5) and (Data < 8)) or (Data > 11)
print('apakah betul?', apa_betul)
print('\n')
## LATIHAN OPERASI LOGIKA DAN KOMPARASI 9 ##
print('## LATIHAN OPERASI LOGIKA DAN KOMPARASI 9 ##')

# OPERASI BITWISE 10 #
print('# OPERASI BITWISE 10 #')
'''operasi bitwise adalah operasi yang bekerja pada binary dari sebuah data, seperti
00000001 jika diorkan dengan 10000011 akan menjadi 100000011'''
print('\n')

#BITWISE OR
print('BITWISE OR')
a = 9
b = 4
c = a | b
print('nilai a = ', a, 'bitwise a = ', format(a,'08b'))
print('nilai b = ', b, 'bitwise b = ', format(b,'08b'))
print('a | b = c =', c, 'bitwise =', format(c, '08b'))
print('\n')

#BITWISE AND
print('BITWISE AND')
a = 9
b = 4
c = a & b
print('nilai a = ', a, 'bitwise a = ', format(a,'08b'))
print('nilai b = ', b, 'bitwise b = ', format(b,'08b'))
print('a & b = c =', c, 'bitwise =', format(c, '08b'))
print('\n')


#BITWISE XOR
print('BITWISE XOR')
a = 9
b = 4
c = a ^ b
print('nilai a = ', a, 'bitwise a = ', format(a,'08b'))
print('nilai b = ', b, 'bitwise b = ', format(b,'08b'))
print('a ^ b = c =', c, 'bitwise =', format(c, '08b'))
print('\n')

#BITWISE NOT
'''bitwise not adalah operasi memirorkan biner. jadi jika angka 10 dinotkan, maka akan 
menjadi -11'''
a = 90
c = ~a
print('nilai a =', a, 'bitwise = ', format(a, '08b'))
print('nilai c = ~a =', c, 'bitwise = ', format(c, '08b'))
print('\n')

#OPERASI SHFITING
'''Yaitu operasi menggeser angka yang ada di binary'''
a = 90
a >> 3
a << 3
print('nilai a =', a, 'bitwise = ', format(a, '08b'))
print('nilai a =', a, 'bitwise = ', format(a, '08b'))
print('nilai a =', a, 'bitwise = ', format(a, '08b'))
## OPERASI BITWISE 10 ##
print('## OPERASI BITWISE 10 ##')
print('\n')

# OPERATOR ASSIGNMENT 11 #
print('# OPERATOR ASSIGNMENT 11 #')
'''adalah operator yang mempersingkat, yaitu dengan sekaligus mengassignment dan menambah
operator dalam satu syntax. Sebelum menggunakan operator assignment, variabel yang 
ingin diassignmentkan harus sudah diassignment terlebih dahulu'''
print('\n')

# Operator assignment aritmatika
print('# Operator assignment aritmatika')
a = 5 #variabel diassignment terlebih dahulu
print('nilai a =', a)
a += 6
print('nilai a += 6 adalah', a)
a -= 3
print('nilai a -= 3 adalah', a)
a *= 4
print('nilai a *= 4 adalah', a)
a /= 2
print('nilai a /= 2 adalah', a)
a //= 3
print('nilai a //= 3 adalah', a)
a %= 2
print('nilai a %= 2 adalah', a)
a **= 2
print('nilai a **= 2 adalah', a)
print('\n')

# Operator assignment bitwise
print('# Operator assignnment bitwise')
c = True
print('c =', c)
c |=False
print('c |= False =', c)
c &= False
print('c &= False =', c)
c ^= True
print('c ^= True =', c)
print('\n')

# Operator assignment binary
print("# Operator assignment binary")
a = 90
print('nilai a =', a, format(a, "012b"))
a >>= 5
print('nilai a >>= 3, a =', a, format(a, "012b"))
a <<= 5
print('nilai a <<= 5, a =', a, format(a, "012b"))

## OPERATOR ASSIGNMENT 11 ##
print('## OPERATOR ASSIGNMENT 11 ##')
print('\n')

# PENGENALAN STRING 12 #
print('# PENGENALAN STRING 12 #')
'''SEGALA BENTUK DATA/KARAKTER DALAM TANDA KURUNG (QUOTE)'''
print('\n')

# Menggunakan backslash
print('# Menggunakan backslash')
'''Backslash digunakan untuk memanggil perintah khusus dalam string'''
print('\n')

print('Backslash untuk membuat tanda kutip menjadi string')
Data = 'Mari berdo\'a'
Data_2 = 'Let\'s Go'
print(Data)
print(Data_2)
print('\n')

print('backslash untuk TAB')
Data = 'Mari \tberdoa \tbersama \tsama'
print(Data)
print('\n')

print('Backslash untuk membuat backslash jadi string')
Data = "C:User\\program files\\Windows\\mudin"
print(Data)

#Raw string
'''Menmbuat semua yang ada di dalam tanda kutip (quote) menjadi string, kecuali tanda kutip'''
print('# Raw string')
print('\n')
print(r'C:User\Programfiles\Windows\T')
print(r'\t\b\n\\')
print('\n')

#Multi line string
'''Membuat string dalam beberapa baris/line sekaligus'''
print('# Multiline string')
print('''
Nama\t\t: Miftakhudin
Kelas\t\t: A1/R1
Semester\t: 3
Fakultas\t: Sastra Nuklir''')
print('\n')

# Raw MUltiline String
'''Membuat semua yang ada dalam kutip menjadi string dalam beberapa baris sekaligus'''
print('# Raw Multiline String')
print(r'''
Nama\t\t: Miftakhudin
Kelas\t\t: A1/R1
Semester\t\t: 3
Fakultas\t\t: Sastra Nuklir''')
print('\n')
## PENGENALAN STRING 12 ##
print('## PENGENALAN STRING 12 ##')
print('\n')