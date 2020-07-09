from PIL import Image

photo = Image.open('video/1.png')
min_size = (100,100)
photo.thumbnail(min_size)
photo.save('video/video.png')
