titik = []
for i in range(3):
    x = float(input(f"masukkan koordinat x titik {i+1}:"))
    y = float(input(f"masukkan koordinat y titik {i+1}:"))
    titik.append([x, y])

print(f"[titik 1, titik 2, titik 3] = {titik}")

a = ((titik[0][0]-titik[1][0])**2 + (titik[0][1]-titik[1][1])**2)**0.5
b = ((titik[1][0]-titik[2][0])**2 + (titik[1][1]-titik[2][1])**2)**0.5
c = ((titik[0][0]-titik[2][0])**2 + (titik[0][1]-titik[2][1])**2)**0.5

if a == b or b == c or a == c:
    print("Tiga titik tersebut membentuk segitiga sama kaki")
else:
    print("Tiga titik tersebut TIDAK membentuk segitiga sama kaki") 
