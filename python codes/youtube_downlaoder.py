from pytube import YouTube
print('download started')
ytube=YouTube('https://www.youtube.com/watch?v=nvmOhpuIhfI')

print('title',ytube,title)
ytube.streams.first().download('/Users/vickysharma/Desktop')
print('downlaoded successfully')
