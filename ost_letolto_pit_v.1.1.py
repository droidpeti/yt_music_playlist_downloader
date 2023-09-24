import pytube
import os
import re
import http.client
import math
import winsound
from pytube import Playlist
from pytube import YouTube

def illegalis_karakter_kitorlo(szoveg):
    helyes_szoveg = szoveg
    illegalis_karakterek = [":","|","/","\\","?","*",">","<", '"']
    for i in illegalis_karakterek:
        helyes_szoveg = helyes_szoveg.replace(i, "")
    re.sub(' +', ' ', helyes_szoveg)
    return helyes_szoveg

zene_szam = 0
zene_szam_string = ""
szamoz = False

valasz = input("Szeretnéd hogy a zene sorszámát belefűzzük a fájlnév elejébe? (i): ").lower()
if valasz == "i":
    szamoz = True

playlist = Playlist(input("add meg a lejátszási lista linkjét, amit leszeretnél tölteni: "))
helyes_playlist_cim = illegalis_karakter_kitorlo(playlist.title)

os.mkdir(helyes_playlist_cim)
os.chdir(helyes_playlist_cim)

print(f"A következő lejátszasi listát töltjük le: {playlist.title}")

for video in playlist.video_urls:
    cim = illegalis_karakter_kitorlo(YouTube(video).title)
    print("Most töltjük: "+cim)
    
    if szamoz:
        zene_szam += 1
        zene_szam_string = ""
        for i in range(math.floor((math.log10(len(playlist.video_urls))+1)-(math.floor(math.log10(zene_szam)) + 1))):
            zene_szam_string += "0"
        zene_szam_string += str(zene_szam)
    
    while(True):
        try:
            pytube.YouTube(video).streams.get_audio_only().download(filename=zene_szam_string+" "+cim+".mp3")
            break
        except http.client.RemoteDisconnected:
            winsound.Beep(1500, 300)
            print("A letöltés közben hiba történt. Próbálkozás újra...")

print("Sikeresen letöltöttük!")
winsound.Beep(1000, 1000)
