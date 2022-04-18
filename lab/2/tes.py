total_mutu = 0.0
total_mutu_lulus = 0.0
total_sks = 0
total_sks_lulus = 0.0
jumlah_sks = 0

print("Selamat datang di Kalkulator IPK!")

jml_matkul = int(input("Masukkan jumlah mata kuliah: "))
while(jml_matkul < 0):
    print("Nilai yang kamu masukkan tidak valid")
    jml_matkul = int(input("Masukkan jumlah mata kuliah: "))

if(jml_matkul == 0):
    print("Tidak ada mata kuliah yang diambil.")
else:
    for i in range(1,jml_matkul+1):
        print("\nMasukkan nama mata kuliah ke-"+str(i)+": ",end="")
        nama_matkul = input()
        
        print("Masukkan jumlah SKS "+nama_matkul+": ",end="")
        jumlah_sks = int(input())
        while(jumlah_sks < 0):
            print("Nilai yang kamu masukkan tidak valid")
            print("Masukkan jumlah SKS",nama_matkul,": ",end="")
            jumlah_sks = int(input())
        
        print("Masukkan nilai yang kamu dapatkan: ",end="")
        nilai_matkul = float(input())
        while(nilai_matkul < 0):
            print("Nilai yang kamu masukkan tidak valid")
            print("Masukkan nilai yang kamu dapatkan: ",end="")
            nilai_matkul = float(input())

        if(nilai_matkul >= 85):
            mutu = 4.00 * jumlah_sks
        elif(80 <= nilai_matkul < 85):
            mutu = 3.70 * jumlah_sks
        elif(75 <= nilai_matkul < 80):
            mutu = 3.30 * jumlah_sks
        elif(70 <= nilai_matkul < 75):
            mutu = 3.00 * jumlah_sks
        elif(65 <= nilai_matkul < 70):
            mutu = 2.70 * jumlah_sks
        elif(60 <= nilai_matkul < 65):
            mutu = 2.30 * jumlah_sks
        elif(55 <= nilai_matkul < 60):
            mutu = 2.00 * jumlah_sks
        elif(40 <= nilai_matkul < 55):
            mutu = 1.00 * jumlah_sks
        elif(nilai_matkul < 40):
            mutu = 0.00 * jumlah_sks
            
        total_sks += jumlah_sks
        total_mutu += mutu

        if nilai_matkul < 55:
            jumlah_sks = 0
        else:
            total_sks_lulus += jumlah_sks
            total_mutu_lulus += mutu

    print("\nJumlah SKS lulus :",total_sks_lulus,"/",total_sks)
    print("Jumlah mutu lulus: {:.2f}".format(total_mutu_lulus),"/ {:.2f}".format(total_mutu))
    print("Total IPK kamu adalah {:.2f}".format(total_mutu_lulus/total_sks_lulus))
    print("Total IPT kamu adalah {:.2f}".format(total_mutu/total_sks))
