from pytube import YouTube # pip install pytube
import datetime 

print('YTD by MrLogon, "help" for commands')

while True:
	inp = input('>')
	if inp.startswith('info '):
		yt = YouTube(inp.split(' ')[1])
		print(yt.title)
		print('=============')
		print('Author: ' + yt.author)
		print('Duration: ' + str(datetime.timedelta(seconds=yt.length)))
		print('Views: ' + str(yt.views))
		print('Rating: ' + str(yt.rating))
		print('Description\n' + yt.description)
	if inp.startswith('download360p'):
		yt = YouTube(inp.split(' ')[1])
		print(yt.title)
		print('=============')
		print('Downloading started')
		print('Please wait...')
		stream = yt.streams.get_by_itag(18)
		stream.download()
		print('Downloading finished')
	if inp.startswith('download720p'):
		yt = YouTube(inp.split(' ')[1])
		print(yt.title)
		print('=============')
		print('Downloading started')
		print('Please wait...')
		stream = yt.streams.get_by_itag(22)
		stream.download()
		print('Downloading finished')
	if inp.startswith('download1080p'):
		yt = YouTube(inp.split(' ')[1])
		print(yt.title)
		print('=============')
		print('Downloading started')
		print('Please wait...')
		stream = yt.streams.get_by_itag(137)
		stream.download()
		print('Downloading finished')
	if inp == 'help':
		print('info <url> - Get information about video')
		print('download360p <url> - Download video with 360p quality')
		print('download720p <url> - Download video with 720p quality')
		print('download1080p <url> - Download video with 1080p quality')