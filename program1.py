import os,shutil
dict_extension = {
    'audio_extension' : ('.mp3','.m4a','.wav','.flac'),
    'video_extension' : ('.mp4','.mkv','.MKV','.flv'),
    'document_extension' : ('.doc','.txt','.pdf','.py'),
}

folderpath = input('enter your path: ')

# give file and extension
document_extension = ('.doc','.txt','.pdf','.py')
audio_extension =('.mp3','.m4a','.wav','.flac')
video_extension = ('.mp4','.mkv','.MKV','.flv')
def file_finder(folder_path, file_extension):
    # return[ file for file in os.listdir(folder_path) 
    # for extension in file_extension if file.endwith(extension)]
    files = [ ]
    for file in os.listdir(folder_path):  #make foler_path folder
        for extension in file_extension:
            if file.endswith(extension):
                files.append[file]
    return files 
print(file_finder(folderpath, document_extension))

# for extension_type, extension_truple in dict_extension.items():
#     folder_name= extension_type.split('_')[0]+'files'           # make folder name
#     folder_path = os.path.join(folderpath, folder_name)         # path for folder
#     os.mkdir(folder_path)
#     for item in file_finder(folderpath, extension_truple):
#         item_path= os.path.join(folderpath, item)     # path for item
#         item_new_path= os.path.join(folder_path, item)  #path for new item
#         shutil.move(item_path, item_new_path)          #move item to new item

# /Users/sachinkawde/Desktop/rahul_python_program