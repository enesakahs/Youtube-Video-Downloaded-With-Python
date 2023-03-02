from pytube import YouTube
import pytube

link = input("Please, Enter Your Youtube Video URL:")
link = str(link)
youtube = pytube.YouTube(link)
path="c:/Users/enes_/OneDrive/Masaüstü/YouTubeVideoDowloader"
youtube.streams.first().download(path)

print("Video Has Been Downloaded", link)