import pytube

url = input('#> Digite o link do video: ')

yt = pytube.YouTube(url)

print('O video está sendo baixado | {yt.title}')

video = yt.streams.first()

video.download()