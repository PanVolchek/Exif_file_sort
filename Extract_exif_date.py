import os
import exifread
import time
""" Read conten of folder
Scan filename
Scan EXIF creation date
Compare
Amend if necessary"""
for (root,dirs,files) in os.walk('C:\\Users\\UUser\\Documents\\Projects\\Python\\Test\\PicScan'):
    for filename in files:
        f = open( "DSCF9150.JPG", 'rb')
        print(filename)
        tags = exifread.process_file(f)