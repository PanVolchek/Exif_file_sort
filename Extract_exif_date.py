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
#pic extentions:
pic_extentions = ['JPG', 'jpg', 'tif']
#scan_folder = 'C:\\Users\\UUser\\Documents\\Projects\\Python\\Test\\PicScan'
scan_folder = 'C:\\Users\\UUser\\Pictures\\Test'


def read_exif(file):
    """Reads EXIF DateTime tag to determine date when picture was taken"""
    f = open(file, 'rb')
    try: 
        tags = exifread.process_file(f)
    except:
        return "_"
    f.close()
    if 'Image DateTime' in tags.keys():
        return tags['Image DateTime']
    else:
        return ""

def rename_file(file):
    """Append YYYYMMDD to filename based on result of read_exif function
    """
    print(filename, 'it is picture!!!')
    Year=str(read_exif(os.path.join(root, filename)))[:4]
    Month=str(read_exif(os.path.join(root, filename)))[5:7]
    Day=str(read_exif(os.path.join(root, filename)))[8:10]
    new_filename = filename[:-4]+' '+Year+Month+Day+'.'+filename[-3:]
    print(Year, Month, Day, " ", new_filename)
    os.rename(os.path.join(root, filename), os.path.join(root, new_filename))

for (root,dirs,files) in os.walk(scan_folder):
    for filename in files:
        if filename[-3:] in pic_extentions:
            rename_file(filename)
            
       
       
