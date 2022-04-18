print('Selamat datang di Kalkulator IPK!')
jumlah_matkul = int(input('Masukkan jumlah mata kuliah:'))
x = 0
jumlah_SKS_lulus = 0
jumlah_mutu_lulus = 0
jumlah_mutu_total = 0
mutu = 0
jumlah_SKS_total = 0
total_IPK = 0
total_IPT = 0

while jumlah_matkul>0 :
    jumlah_matkul = jumlah_matkul -1
    x = x+1
    nama_matkul = input("Masukkan nama mata kuliah ke-"+ str(x) + ":")
    jumlah_SKS =  float(input("Masukkan jumlah SKS " + nama_matkul + ":"))
    nilai_SKS = float(input('Masukkan nilai yang kamu dapatkan:'))

    
    while nilai_SKS <0 :
        print("Nilai yang kamu masukkan tidak valid")
        nilai_SKS = float(input('Masukkan nilai yang kamu dapatkan:'))
    print(" ")

    
    # konversi nilai ke bobot
    if nilai_SKS>85:
        bobot = 4.00
    elif 80 <=nilai_SKS<85 :
        bobot = 3.70
    elif 75<=nilai_SKS<80 :
        bobot = 3.30
    elif 70<=nilai_SKS<75 :
        bobot = 3.00
    elif 65<=nilai_SKS<70 :
        bobot = 2.70
    elif 60<=nilai_SKS<65 :
        bobot = 2.30
    elif 55<=nilai_SKS<60 :
        bobot = 2.00
    elif 40<=nilai_SKS<55 :
        bobot = 1.00
    elif nilai_SKS<40 :
        bobot = 0.00
    
    mutu = bobot * jumlah_SKS
    jumlah_SKS_total += jumlah_SKS 
    jumlah_mutu_total +=  mutu

    if bobot<= 1.00 : 
        jumlah_SKS = 0
    else :
        jumlah_SKS_lulus += jumlah_SKS
        jumlah_mutu_lulus += mutu
        total_IPK = jumlah_mutu_lulus/jumlah_SKS_lulus
    
    total_IPT = jumlah_mutu_total/jumlah_SKS_total
    
total_IPT = format(total_IPT, ".2f")
total_IPK = format(total_IPK, ".2f")  
jumlah_mutu_total = format(jumlah_mutu_total, ".2f")
jumlah_mutu_lulus = format(jumlah_mutu_lulus, ".2f")    
print("Jumlah SKS lulus :" + str(jumlah_SKS_lulus) + "/" + str(jumlah_SKS_total) )
print("Jumlah mutu lulus:" + str(jumlah_mutu_lulus)+ "/" + str(jumlah_mutu_total))
print("Total IPK kamu adalah " + str(total_IPK))
print("Total IPT kamu adalah " + str(total_IPT))