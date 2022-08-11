import os
import exifread
import time
""" 
1. Read conten of folder
2. Scan filename
3. Scan EXIF creation date
4. Compare
5. Amend if necessary
"""
for (root,dirs,files) in os.walk('C:\\Users\\UUser\\Documents\\Projects\\Python\\Test\\PicScan'):
    for filename in files:
        f = open( "DSCF9150.JPG", 'rb')
        print(filename)
        tags = exifread.process_file(f)
