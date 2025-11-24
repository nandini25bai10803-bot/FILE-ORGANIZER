import os
import shutil

path = input("Enter Path : ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  

    
    if extension == '':
        continue

    
    if not os.path.exists(os.path.join(path, extension)):
        os.makedirs(os.path.join(path, extension))

    
    shutil.move(
        os.path.join(path, file),
        os.path.join(path, extension, file)
    )

print("Files sorted successfully!")

     





