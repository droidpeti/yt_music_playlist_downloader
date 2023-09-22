import pytube
import os
import re
from pytube import Playlist
from pytube import YouTube

def illegalis_karakter_kitorlo(szoveg):
    helyes_szoveg = szoveg
    illegalis_karakterek = [":","|","/","\\","?","*",">","<", '"']
    for i in illegalis_karakterek:
        helyes_szoveg = helyes_szoveg.replace(i, "")
    re.sub(' +', ' ', helyes_szoveg)
    return helyes_szoveg

playlist = Playlist(input("add meg a lejátszási lista linkjét, amit leszeretnél tölteni: "))
helyes_playlist_cim = illegalis_karakter_kitorlo(playlist.title)

os.mkdir(helyes_playlist_cim)
os.chdir(helyes_playlist_cim)

print(f"A következő lejátszasi listát töltjük le: {playlist.title}")

for video in playlist.video_urls:
    cim = illegalis_karakter_kitorlo(YouTube(video).title)
    print("Most töltjük: "+cim)
    pytube.YouTube(video).streams.get_audio_only().download(filename=cim+".mp3")

print("Sikeresen letöltöttük!")