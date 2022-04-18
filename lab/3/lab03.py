
# memasukkan input dari user
a = input("Masukkan input himpunan A: ") 
b = input("Masukkan input himpunan B: ") 

# menambahkan koma dibelakang agar bisa di slice
a += ","
b += ","

# menghitung koma di a dan b untuk iterasi
jmlh_koma_a = a.count(",")
jmlh_koma_b = b.count(",")

# menentukan index untung slicing string
awal_a = 0
akhir_a = a.find(",")

hasil = ""

for x in range(0, jmlh_koma_a):
    # slicing string
    str_a = a[awal_a:akhir_a]

    # merubah index untuk slice ke koma berikutnya
    awal_a = akhir_a + 1
    akhir_a = a.find(",", awal_a)

    # menentukan index untung slicing string b
    awal_b = 0
    akhir_b = b.find(",")

    for y in range(0, jmlh_koma_b):
        # slicing string
        str_b = b[awal_b:akhir_b]

        # increament string
        hasil += "(" + str_a + "," + str_b + ")" + ", "

        # merubah index untuk slice ke koma berikutnya
        awal_b = akhir_b + 1
        akhir_b = b.find(",", awal_b)

# print hasil string
print("{" + hasil[:-2] + "}")