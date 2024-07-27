import changeDir
import downloadFunc

link = input('Link:  ')
AudVid = input('Audioo or video a / v: ')
directory = input('Directory for download: ')

changeDir.changeDownloadDir(directory)

if AudVid == 'a':
    downloadFunc.downloadAudio(link)
elif AudVid == 'v':
    downloadFunc.downloadVideo(link)
else:
    print('wrong option')
    