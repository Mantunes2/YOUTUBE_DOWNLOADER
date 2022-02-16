import pytube

url = input('#> Digite o link do video: ')

yt = pytube.YouTube(url)

video = yt.streams.get_by_itag(22)

video.download()
