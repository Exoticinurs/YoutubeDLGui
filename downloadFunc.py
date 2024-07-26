import yt_dlp as ytdl
audio={'format':'bestaudio/best'}
video={'format':'bestvideo/best'}

def downloadAudio(link):
    with ytdl.YoutubeDL(audio) as ydl:
        ydl.download([link])

def downloadVideo(link):
    with ytdl.YoutubeDL(video) as ydl:
        ydl.download([link])