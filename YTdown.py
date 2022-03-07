import PySimpleGUI as sg
import pytube

def download():
    layout = [
        [sg.Text('Youtuber Downloader', font='Helverica 11', pad=(100, 1))],
        [sg.HorizontalSeparator()],
        [sg.Text('Link'), sg.InputText("", key='media_down')],
        [sg.Radio('MP4', 'GROUP1', key='mp4'), sg.Radio('MP3', 'GROUP1', key='mp3')],
        [sg.Button('Fechar'), sg.Button('Fazer Download')]
    ]

    #Criando a janela
    window = sg.Window('Youtuber Downloader', layout, size=(400, 150), resizable=False)
    while True:
        #Criando a os eventos
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Fechar'):
            break
        elif event == 'Fazer Download':
            if values['mp4'] == True:
                url = values['media_down']
                yt = pytube.YouTube(url)
                video = yt.streams.get_by_itag(22)
                video.download()
                return sg.popup('Download feito com Sucesso!')
            elif values['mp3'] == True:
                link = values['media_down']
                yt = pytube.YouTube(link)
                audio = yt.streams.get_by_itag(140)
                audio.download()
                return sg.popup('Download feito com sucesso!', size=(200, 50))
        window.close()

if __name__ == '__main__':
    download()
