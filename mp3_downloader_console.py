import yt_dlp 

url = input('enter url: ')

ytd_opt_audio = {
    'writethumbnail': True,
    'format': 'bestaudio/best',
    'cookiefile': 'cookies.txt',  # <-- add this line
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
        {
            'key': 'FFmpegMetadata',
            'add_metadata': True,
        },
        {'key': 'EmbedThumbnail'},
    ]
}
try:
    with yt_dlp.YoutubeDL(ytd_opt_audio) as ydl:
        ydl.download([url])
except yt_dlp.utils.DownloadError as e:
    print("Download Utils", e)
