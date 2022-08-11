import os
import exifread
import time

for (root,dirs,files) in os.walk('C:\\Users\\UUser\\Documents\\Projects\\Python\\Test\\PicScan'):
    for filename in files:
        f = open( "DSCF9150.JPG", 'rb')
        print(filename)
        tags = exifread.process_file(f)