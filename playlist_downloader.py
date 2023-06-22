from pytube import Playlist

py=Playlist("https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY")

print(f'Downloading: {py.title}')

for video in py.videos:
	video.streams.first().download()