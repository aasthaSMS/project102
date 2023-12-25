import os
import shutil

from_dir = "C:/Users/LENOVO/Downloads"
to_dir = "C:/Users/LENOVO/Downloads/pdfs"

list_files = os.listdir(from_dir)
#print(list_files) 

for file_name in list_files:
    name,ext = os.path.splitext(file_name)
    # print("File name",name)
    # print("Extension",ext)
    if ext == "":
        continue
    if ext in [".pdf"]:
        path1 = from_dir+"/"+file_name
        path2 = to_dir+"/"+"pdf_file"
        path3 = to_dir+"/"+"pdf_file"+"/"+file_name
        if os.path.exists(path2):
            print("moving.."+file_name+"....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving.."+file_name+"....")
            shutil.move(path1,path3)
            