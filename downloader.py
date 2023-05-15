import yt_dlp as youtube_dl
import threading
from tkinter import messagebox

def download(url):
    yt_options = {
                'format': 'bestaudio/best',
                'postprocessors': [
                {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                }
            ]
        }
    
    with youtube_dl.YoutubeDL(yt_options) as ydl:            
            ydl.download([url])  
            info = messagebox.showinfo(message="downloading is completed!")
   
if __name__ == '__main__':
    t1 = threading.Thread(target=download, args=("https://www.youtube.com/watch?v=F_TV4vZRSE8&pp=ygULbHVuYXIgYWJ5c3M%3D",))
    t2 = threading.Thread(target=download, args=("https://www.youtube.com/watch?v=LKBdeEJWcb4",))