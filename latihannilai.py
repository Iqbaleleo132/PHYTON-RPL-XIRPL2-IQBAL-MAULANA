print('kalkulator luas bidang datar')
print('1. segitiga')
print('lingkaran')
print('persegi panjang')
print('jajar genjang')

operasi = input('pilih operasi 1/2/3/4 :')
bil_1 = int(input ('masukan bilangan pertama:'))
bil_2 = int(input ('masukan bilangan kedua:'))

if operasi == '1':
    hasil1 = 0.5*bil_1*bil_2
    print("luas segitiga =", hasil1)
elif operasi == '2':
    hasil2 = 3.14*bil_1*bil_2
    print("luas lingkaran =", hasil2)
elif operasi == '3':
    hasil3 = bil_1*bil_2
    print("luas persegi panjang =", hasil3)
elif operasi == '4':
    hasil4 = bil_1*bil_2
    print("luas jajar genjang =", hasil4)
else :
    print('tidak valid')

3