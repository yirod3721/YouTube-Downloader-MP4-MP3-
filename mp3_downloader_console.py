import yt_dlp 
url = str(input('enter url:'))
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
yt_dlp.YoutubeDL(ytd_opt_audio).download(url)

