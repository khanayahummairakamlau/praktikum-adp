import time
import os
from termcolor import cprint

teks = "   ✨ HAPPY EID!✨    "*5
lebar = 20
durasi = 20
jeda = 0.2
perulangan = int(durasi / jeda)  
line = " " *lebar + teks
             
for i in range(perulangan):
    os.system('cls')
    scrolled = line[i:i+lebar]
    bingkai_atas =  '╔' + ('═' * (lebar + 2)) + '╗'
    bingkai_bawah = '╚' + ('═' * (lebar + 2)) + '╝'
    if i % 2 == 0:
        cprint(bingkai_atas, 'magenta', attrs=['dark'])
        cprint(" " + scrolled + " ", 'cyan', attrs=['dark'])
        cprint(bingkai_bawah, 'magenta', attrs=['dark'])
    else:
        cprint(bingkai_atas, 'cyan', attrs=['bold'])
        cprint(" " + scrolled + " ", 'magenta', attrs=['bold']) 
        cprint(bingkai_bawah, 'cyan', attrs=['bold'])  
    time.sleep(jeda)