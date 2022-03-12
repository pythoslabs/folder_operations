# This creates the train.csv from the images in the training folder 
# Created : 26 Dec 2021 

# Does the following 
# finds if there are 4 channels in an image , then and convert to 3 channel AND saves as JPG


# To do : 
#Remove the svg / webp / gif - formats or convert them into JPEG

import os 
import pandas as pd
from  PIL import Image 
import pickle 
import time 

def get_class(class_str):
    class_ = d.get(class_str)
    return class_  

# --------------------- 
#       DECLARATIONS & VARS 
# --------------------------

FILES_DIR  = '../data/images'
OUTPUT_META_DATA_FILE = '../report/MALE_FEMALE_CHILD.csv'
CLASSES_TXT = '../report/MALE_FEMALE_CHILD.txt'

L_classes = os.listdir(f'{FILES_DIR}')
enum_ = list(enumerate(L_classes))
d=dict((i,j) for j,i in enum_)

cols_ = ['fname','class']
df_out = pd.DataFrame(columns = cols_)

for dir_ in L_classes: 
    L_files = os.listdir(f'{FILES_DIR}/{dir_}')
    for files_ in L_files :
       
        # Check if it has 4 channels ( or a PNG file)
        fpath  = f'{FILES_DIR}/{dir_}/{files_}'
        data_values = [files_ , dir_]   
        new_row = pd.Series(data_values,index=df_out.columns )
        df_out = df_out.append(new_row, ignore_index=True)

df_out['class_encode'] = df_out['class'].apply(lambda x:get_class(x)) 
df_out.to_csv(OUTPUT_META_DATA_FILE,index=False)
print("Done creating metadata files")

# ----------------  Export to text ( classes.txt )

df_classes = pd.DataFrame.from_dict(d,orient='index')
df_classes.to_csv(CLASSES_TXT,header=False)


