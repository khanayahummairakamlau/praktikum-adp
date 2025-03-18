while True :
    angka1=float(input("Masukkan angka pertama : "))
    angka2=float(input("Masukkan angka kedua : "))

    print('===Pilih Operasi===')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('5. Keluar')

    operasi =input('Pilih operasi (1/2/3/4/5) :')

    if operasi == '1' :
         hasil = angka1+angka2
         print(f'Hasil = {hasil}')
    elif operasi == '2' :
         hasil = angka1-angka2
         print(f'Hasil = {hasil}')
    elif operasi == '3' :
         hasil = angka1*angka2
         print(f'Hasil = {hasil}')
    elif operasi == '4' :
        if angka2 == 0 :
            print('Error : tidak terdefenisi')
        else :
            hasil = angka1/angka2
            print(f'Hasil = {hasil}')
    else :
        print('Terimakasih')
        break





        
