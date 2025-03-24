n= int(input('Masukkan jumlah baris (minimal 4)= '))
jumlah_boom  = 0
tengah = int(n/2)

if n<4 :
    print('Jumlah baris minimal adalah 4')  
else:
    for i in range (n) :
        for j in range (n) :
            if i == j :
                if n % 2 == 1 and i == tengah :
                    print('HORE', end ="  ")
                else : 
                    print(' 1 ', end="   ")
            elif i + j == n - 1 :
                print (' 2 ', end="   ")
            else : 
                print('BOOM', end="  ")
                jumlah_boom = jumlah_boom + 1
        print()
    print(f'Total BOOM yang muncul sebanyak = {jumlah_boom}')
