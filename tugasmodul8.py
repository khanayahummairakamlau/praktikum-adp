data_praktikan= [('2410431017', 'Inaya', 98, 95, 99),
        ('2410432017', 'Irodi', 77, 80, 70),
        ('2410433017', 'Dhira', 98, 95, 99),
        ('2410431002', 'Salma', 65, 60, 70),
        ('2410432002', 'Sarah', 85, 88, 84),
        ('2410433002', 'Laila', 56, 65, 62),
        ('2410431006', 'Viola', 70, 75, 78),
        ('2410432006', 'Nindi', 95, 85, 90),
        ('2410433006', 'Ghina', 88, 90, 85),
        ('2410431726', 'Naswa', 77, 73, 75)]

#menyimpan data praktikan ke file
with open("data_praktikan.txt", "w") as file:
    for nim, nama, pretest, postest, tugas  in data_praktikan:
        file.write(f"{nim}, {nama}, {pretest}, {postest}, {tugas}\n")

#membaca file data_praktikan dan menyimpan ke dictionary
data_dictionary = {}
with open("data_praktikan.txt", "r") as file:
    for baris in file:
        nim, nama, pretest, postest, tugas  = baris.strip("").split(",")
        data_dictionary[nim] = {
            "nama": nama ,
            "pretest": int(pretest),
            "postest": int(postest),
            "tugas": int(tugas)
        }

#menghitung nilai akhir dan menulis ke file data_nilai_akhir
with open("data_nilai_akhir.txt", "w") as file:
    file.write("NIM, Nama, Pretest, Postest, Tugas, Nilai Akhir\n")
    for nim, data in data_dictionary.items():
        nilai_akhir = (0.35 * data["pretest"] + 0.35 * data["postest"] +0.30 * data["tugas"])
        nilai_akhir = float(f"{nilai_akhir:.2f}")
        data_dictionary[nim]["nilai_akhir"] = nilai_akhir
        file.write(f"{nim}, {data['nama']}, {data['pretest']}, {data['postest']}, {data['tugas']}, {nilai_akhir}\n")
 
#analisa nilai
nilai_akhir_list = [data["nilai_akhir"] for data in data_dictionary.values()]
rata_rata = sum(nilai_akhir_list)/len(nilai_akhir_list)
nilai_tertinggi = max(nilai_akhir_list)
nilai_terendah = min(nilai_akhir_list)

#menenukan praktikan dengan nilai tertinggi dan terendah
nama_nilai_tertinggi = [data['nama'] for data in data_dictionary.values() if data['nilai_akhir'] == nilai_tertinggi]
nama_nilai_terendah = [data['nama'] for data in data_dictionary.values() if data['nilai_akhir'] == nilai_terendah]
nim_nilai_tertinggi = [nim for nim, data in data_dictionary.items() if data['nilai_akhir'] == nilai_tertinggi]
nim_nilai_terendah = [nim for nim, data in data_dictionary.items() if data['nilai_akhir'] == nilai_terendah] 

#menghitung jumlah praktikan di bawah rata-rata
jumlah_dibawah_rata2 = sum(1 for nilai in nilai_akhir_list if nilai < rata_rata)

#menampilkan hasil
print("="*50)
print("          HASIL ANALISIS NILAI PRAKTIKAN          ")
print("="*50)
print(f"Nilai Tertinggi: {nilai_tertinggi:.2f}")
for nim, data in data_dictionary.items():
    if data['nilai_akhir'] == nilai_tertinggi:
        print(f"  - Nama : {data['nama']}, NIM : {nim}")
        
print("-"*50)
print(f"Nilai Terendah: {nilai_terendah:.2f}")
for nim, data in data_dictionary.items():
    if data['nilai_akhir'] == nilai_terendah:
        print(f"  - Nama : {data['nama']}, NIM : {nim}")
       
print("-"*50)
print(f"Rata-rata Nilai Akhir : {rata_rata:.2f}")
print(f"Jumlah praktikan di bawah rata-rata: {jumlah_dibawah_rata2} orang")
print("="*50)


