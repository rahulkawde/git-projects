
# pending
import os

def fileNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# def move(foldername,files):
    # os.replace(file,f'{foldername}/{file}')


files = os.listdir('cleaner/') # get list of all
# print(files)
files.remove('main.py') # for remove main file
# print(files)


# for when file is exist 
fileNotExist('cleaner/Images')
fileNotExist('cleaner/Docs')
fileNotExist('cleaner/Medias')
fileNotExist('cleaner/Pythons')
fileNotExist('cleaner/Others')

imgExt=['.jpg','.png','.jpeg']
images = []
for file in files :
    if os.path.splitext(file)[1].lower in imgExt:
        images.append(file)
print(images)
# print(files)

docExt=['.txt','.pdf','.csv','.doc']
docs = [file for file in files if os.path.splitext(file)[1].lower in docExt ]
print(docs)


# mediaExt = ['.mp4','.mp3','.flv','.wav','.mov']
# medias = [file for file in files if os.path.splitext(file)[1].lower in mediaExt ]
# print(medias)


# pythonExt = ['.py','.csv']
# python= [file for file in files if os.path.splitext(file)[1].lower in pythonExt ]
# print(python)

# others= []
# for file in files:
#     ext = os.path.splitext(file)[1].lower
#     if (ext not in imgExt) and (ext not in docExt) and (ext not in mediaExt) and (ext not in pythonExt)and os.path.isfile(file):
#         others.append(file)
# print(others)

      
# move('cleaner/Image',images)
# move('cleaner/Docs',docs)
# move('cleaner/Medias',medias)
# move('cleaner/Python',python)
# move('cleaner/Others',others)    


