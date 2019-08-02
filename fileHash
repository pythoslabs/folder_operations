# prints the hash of the file 
# To check if the same file is present as a different file name

from PIL import Image
import imagehash

def getImageMetaData(file_path):
    with Image.open(file_path) as img:
        img_hash = imagehash.phash(img)
        return img.size, img.mode, img_hash
