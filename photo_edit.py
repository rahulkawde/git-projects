# ---change image extension-------
from PIL import Image,ImageEnhance,ImageFilter
import os

img1 = Image.open('practice/1.png')        # create objet
img1.save('img1.png')       # .save for save image  and convert png,pdf
# img1.show()                 # .show for show image
# resize
min_size = (100,100)       # pixel store in variable
img1.thumbnail(min_size)            #.thumbnail for edit
img1.save('1n.png') 
# ('1n.png').show()             # save image
# # more than 1 image covert
# for i in os.listdir():                   # give a list of folder
#     if i.endswith('.jpg'):              #scarch extension
#         img1= Image.open(i)             #open item
#         filename,extension = os.path.splitext(i)    # split name extension
#         img1.save(f'{filename}.png')      # save and convert


# sharpness,brightness,blur,contrast      #add module ImageEnhance
# img1 = Image.open('IMG-20200521-WA0064.jpg')  
# obj= ImageEnhance.Sharpness(img1)       # obj=module.class(c)
# obj.enhance(2).save('img2.jpg')   # obj.enhance(value).save(newname)
#value 0 = blurry
# 1 = original
# 2 = sharper

#-----------colour----------
# img1 = Image.open('IMG-20200521-WA0064.jpg')  
# obj= ImageEnhance.Color(img1)       # obj=module.class(c)
# obj.enhance(2).save('img2.jpg')     # obj.enhance(value).save(newname)
#value 0 = B/W
# 1 = original
# 2 = increase colour

#----------brightness---------
# img1 = Image.open('IMG-20200521-WA0064.jpg')  
# obj= ImageEnhance.Brightness(img1)       # obj=module.class(c)
# obj.enhance(2).save('img2.jpg')     # obj.enhance(value).save(newname)
#value 0 = Black
# 1 = original
# 2 = increase brightness

#---------contrast----------
# img1 = Image.open('IMG-20200521-WA0064.jpg')  
# obj= ImageEnhance.Contrast(img1)       # obj=module.class(c)
# obj.enhance(2).save('img2.jpg')     # obj.enhance(value).save(newname)
#value 0 = B/W
# 1 = original
# 2 = increase contrast

# ----------------blur-------
#we also use sharpnesss class with value 0
# add Imagefilter in module
# img1 = Image.open('IMG-20200521-WA0064.jpg')  
# img1.filter(ImageFilter.GaussianBlur()).save('img3.png') # we use imagefilter and 
                                                         #gaussianblur(radius=2)
       #we can change radius                                                  