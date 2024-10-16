import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')
else:
    print("File is not empty. file size is ", size)
