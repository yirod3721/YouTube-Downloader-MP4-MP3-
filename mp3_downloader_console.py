import yt_dlp 
choice = str(input("Enter File for file use or cmd for cmd use: "))
while ((choice != "File") and (choice != "cmd")):
    print("please enter either file or cmd")
    choice = str(input("Enter File for file use or cmd for cmd use: "))
if choice == "File":
    file_path = str(input("enter appropiate file path: "))
    with open(file_path, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
if choice == "cmd":
    urls = input("enter your urls: ")
#multiple url download
ytd_opt_audio = {
    'writethumbnail': True,
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    #cookie input
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
#Error Handling
try:
    with yt_dlp.YoutubeDL(ytd_opt_audio) as ydl:
        ydl.download(urls)
except yt_dlp.utils.DownloadError as e:
    print("Download Utils", e)
