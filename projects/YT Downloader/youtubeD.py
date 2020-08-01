#Youtube video downlaod√√
from pytube import YouTube

link = input('Enter the link :')
yt = YouTube(link)

videos = yt.streams.all()
# videos= videos.index(res)
# print(videos)
# https://www.youtube.com/watch?v=Yqur47HdKd8

i = 1
for stream in videos:
    print(stream)

    print(str(i)+' '+ str(stream))
    i+=1

stream_no = int(input('Enter the number: '))
video = videos[stream_no -1]
video.download('/Users/sachinkawde/Downloads')  
print('Downloaded')
  



