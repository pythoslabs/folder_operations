# Created : 5 Jan 2022 
# To do 
# Handle conditions where 
# 1. File is not present in the imagefolder 
    

import os 
import pandas as pd
from  PIL import Image 
import pickle
import shutil

import time 

def get_class(class_str):
    class_ = d.get(class_str)
    return class_  

# ---------- function to create folders
# Usage : create_folders(METAFILE_CLASS,BASE_DIR,ENCODED_FOLDERS)
# 

def create_folders(METAFILE_PATH,BASE_DIR, create_encoded= False): 

    df = pd.read_csv(METAFILE_PATH,sep = ',',header= None)
    L_folders = list(df.iloc[:,0])
    L_folders_encode = list(df.iloc[:,1])
    print(L_folders)
    print("************")
    print(L_folders_encode)
    L_folders = [k for k in L_folders if len(k)>0]  # make sure that you remove the null lines also
    #L_folders_encode = [k for k in L_folders_encode if len(k)>0]  # make sure that you remove the null lines also


    #create CLASSIFICATION_DIR
    if not os.path.isdir(f'{BASE_DIR}'):
        print(f'creating ... {BASE_DIR}')
        os.mkdir(f'{BASE_DIR}')

    # name the folders as text or encoded 0, 1, 2 etc 
    if  create_encoded == False :
        L_new_folders =L_folders
    else : 
        L_new_folders =L_folders_encode
          
    for new_dir in L_new_folders:
        if not os.path.isdir(f'{BASE_DIR}/{new_dir}'):
            print(f'creating ... {BASE_DIR}/{new_dir}')
            os.mkdir(f'{BASE_DIR}/{new_dir}')

def move_files(DF_PATH,IMAGE_DIR,DEST_BASE_DIR,ENCODED_FOLDERS=False) :
    # todo : Change this to an apply function instead of loop
    df = pd.read_csv(DF_PATH)
    for index, data in df.iterrows() : 
        fname_ = data['fname']
        folder_ = data['class']
        L_folders_encode = data['class_encode']

        src = f'{IMAGE_DIR}/{fname_}'
        dst = f'{BASE_DIR}/{folder_}/{fname_}'
        k= shutil.move(src,dst)
        
#    if create_encoded == False 
#       create the additional condition for checking if you want to create 
#       encoded directories 


# --------------------- -------------
#       Declarations 
# --------------------- -------------

BASE_DIR  = '../data/recreate'
IMAGE_DIR = '../data/images'
METAFILE_CLASS = '../data/classes.txt'
ENCODED_FOLDERS = False 
DF_PATH  = '../data/metadata.csv'

create_folders(METAFILE_CLASS,BASE_DIR,ENCODED_FOLDERS)
move_files (DF_PATH,IMAGE_DIR,BASE_DIR,ENCODED_FOLDERS)


