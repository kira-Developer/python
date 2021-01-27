from pytube import YouTube


ytd = YouTube('https://youtu.be/-OYyPhHADYU')
ytd.streams.filter(adaptive=True).first().download()
