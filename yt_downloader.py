from easygui import *
import yt_dlp 
text = 'what format do you want?'
title = 'YazanTube'
button1 = 'Video'
button2 = 'Audio'
button_list = [button1, button2]
output = buttonbox(text, title, button_list)
if (output == 'Video'):
    text1 = 'enter the url of the video'
    output1 = enterbox(text1, title,)
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
    }
    url = [str(output1)]
    yt_dlp.YoutubeDL(ydl_opts).download(url)


elif (output == 'Audio'):
    text2 = 'enter the url of the audio'
    output2 = enterbox(text2, title,)
    ydl_opts = {
    
    'format': 'bestaudio[abr>=192]/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [ 
       {
           'key': 'FFmpegExtractAudio',
           'preferredcodec': 'mp3',
           'preferredquality': '192',

        }
    ]
    }
    ytd_opt_audio = {
        'writethumbnail': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
   },{
         'key': 'FFmpegMetadata',
        'add_metadata': True,
    },
    {'key': 'EmbedThumbnail'},]}
    url = [str(output2)]
    yt_dlp.YoutubeDL(ytd_opt_audio).download(url)
    

