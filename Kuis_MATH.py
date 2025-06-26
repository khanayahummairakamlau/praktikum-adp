import pygame, sys, random, time
pygame.init()

def tampilan_awal():
    teks = "MATH ATTACK, knc edition"
    ukuran = 10
    while ukuran < 60:
        layar.fill(PINK)
        font_animasi = pygame.font.SysFont(None, ukuran)
        gambar_teks = font_animasi.render(teks, True, PUTIH)
        posisi = gambar_teks.get_rect(center=(lebar // 2, tinggi // 2))
        layar.blit(gambar_teks, posisi)
        pygame.display.flip()
        ukuran += 1
        waktu.tick(60)
    pygame.time.delay(3000)

def input_nama():
    nama = ""
    while True:
        layar.fill(PINK)
        layar.blit(font.render("NAMA :", True, PUTIH), (200, 200))
        layar.blit(font.render(nama + "|", True, PUTIH), (200, 300))
        layar.blit(font2.render("TEKAN ENTER", True, PUTIH), (400, 500))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nama = nama[:-1]
                elif event.key == pygame.K_RETURN and nama != "":
                    return nama
                elif len(event.unicode) == 1:
                    nama += event.unicode

def pilih_level():
    level_terpilih = 1
    while True:
        layar.fill(PINK)
        layar.blit(font.render("Pilih Level Kuis", True, PUTIH), (250, 100))
        for i in range(1, 4):
            warna = HIJAU if i == level_terpilih else PUTIH
            layar.blit(font.render(f"Level {i}", True, warna), (330, 150 + i* 80))
        layar.blit(font2.render("Gunakan <- -> lalu ENTER", True, PUTIH), (200, 500))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    level_terpilih = max(1, level_terpilih - 1)
                elif event.key == pygame.K_RIGHT:
                    level_terpilih = min(3, level_terpilih + 1)
                elif event.key == pygame.K_RETURN:
                    return level_terpilih

def tampilan_mulai_kuis():
    while True:
        layar.fill(PINK)
        layar.blit(font.render("MULAI KUIS", True, PUTIH), (290, 260))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

def animasi_benar():
    layar.fill(HIJAU)
    layar.blit(font.render("Benar!", True, PUTIH), (350, 250))
    pygame.mixer.Sound.play(suara[BENAR])
    pygame.display.update()
    pygame.time.delay(2000)

def animasi_salah(pesan):
    layar.fill(MERAH)
    layar.blit(font.render(pesan, True, PUTIH), (300, 250))
    pygame.mixer.Sound.play(suara[SALAH])
    pygame.display.update()
    pygame.time.delay(2000)

def simpan_skor(nama, skor):
    with open("skor_kuis.txt", "a") as file:
        file.write(f"{nama} : {skor} poin\n")

def kuis_matematika(nama, level):
    skor = 0
    soal_level = random.sample(soal[level], len(soal[level]))
    for data in soal_level:
        pertanyaan = data["soal"]
        jawaban_benar = data["jawaban"]
        jawaban = ""
        waktu_mulai = time.time()
        kuis = False

        while not kuis:
            sisa_waktu = max(0, 15 - int(time.time() - waktu_mulai))
            layar.fill(PINK)
            layar.blit(font.render(f"Skor: {skor}", True, PUTIH), (10, 10))
            warna_waktu = MERAH if sisa_waktu <= 5 else PUTIH
            layar.blit(font.render(f"Waktu: {sisa_waktu} detik", True, warna_waktu), (10, 60))
            layar.blit(font.render(pertanyaan, True, PUTIH), (250, 200))
            layar.blit(font.render(f"Jawaban: {jawaban}", True, PUTIH), (150, 280))
            pygame.display.update()

            if sisa_waktu == 0:
                animasi_salah("Waktu Habis!")
                break

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        jawaban = jawaban[:-1]
                    elif event.key == pygame.K_RETURN and jawaban != "":
                        try:
                            hasil = eval(jawaban)
                        except:
                            hasil = None
                        if hasil == jawaban_benar:
                            skor += 20
                            animasi_benar()
                        else:
                            animasi_salah("Salah!")
                        kuis = True
                    elif len(event.unicode) == 1:
                        jawaban += event.unicode

    simpan_skor(nama, skor)
    pilihan = 0
    while True:
        layar.fill(PINK)
        layar.blit(font.render(f"Selamat, {nama}!", True, PUTIH), (250, 180))
        layar.blit(font.render(f"Skor Akhir: {skor}", True, PUTIH), (260, 250))
        warna_main = HIJAU if pilihan == 0 else PUTIH
        warna_keluar = HIJAU if pilihan == 1 else PUTIH
        layar.blit(font.render("Main Lagi", True, warna_main), (160, 360))
        layar.blit(font.render("Keluar", True, warna_keluar), (480, 360))
        layar.blit(font2.render("Gunakan <- -> lalu ENTER", True, PUTIH), (200, 450))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pilihan = 0
                elif event.key == pygame.K_RIGHT:
                    pilihan = 1
                elif event.key == pygame.K_RETURN:
                    return pilihan == 0
                

lebar, tinggi = 800, 600
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("KUIS MATEMATIKA")
font = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None, 40)
waktu = pygame.time.Clock()

PUTIH = (255, 250, 240)
PINK = (255, 182, 193)
HIJAU = (0, 200, 0)
MERAH = (200, 0, 0)

suara = [
    pygame.mixer.Sound("benar.wav"),
    pygame.mixer.Sound("salah.wav")
]

BENAR, SALAH = 0, 1 
pygame.mixer.music.load("backsound.wav")

soal = {
    1: [
        {"soal": "8 x 5", "jawaban": 40},
        {"soal": "144 / 4", "jawaban": 36},
        {"soal": "9 x 6", "jawaban": 54},
        {"soal": "21 / 7", "jawaban": 3},
        {"soal": "22 x 4", "jawaban": 88}
    ],
    2: [
        {"soal": "6 + 4 x 5", "jawaban": 26},
        {"soal": "3, 6, 9, 12, ... ?", "jawaban": 15},
        {"soal": "1, 4, 9, 16, ... ?", "jawaban": 25},
        {"soal": "11 x 5 - 5", "jawaban": 50},
        {"soal": "(9 - 9) x 9", "jawaban": 0}
    ],
    3: [
        {"soal": "100 - (25 x 3) + 5", "jawaban": 30},
        {"soal": "(7 + 3) x 2 - 4", "jawaban": 16},
        {"soal": "2, 4, 8, 16, ... ?", "jawaban": 32},
        {"soal": "3, 6, 18, 72, ... ?", "jawaban": 360},
        {"soal": "1, 2, 6, 24, ... ?", "jawaban": 120}
    ]
}


pygame.mixer.music.play(loops=-1)
tampilan_awal()
while True:
    nama = input_nama()
    level = pilih_level()
    tampilan_mulai_kuis()
    ulang = kuis_matematika(nama, level)
    if not ulang:
        break