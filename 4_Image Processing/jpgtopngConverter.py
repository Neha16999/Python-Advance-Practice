import sys
import os
import pathlib
from PIL import Image

#grabing the image folder and the output folder

image_folder = sys.argv[1]
output_folder = sys.argv[2]

print("Img Ip :", image_folder)
print("Img Op :", output_folder)

#check if the folder exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through the images in input folder and convert it 
for filename in os.listdir(image_folder):
    img=Image.open(f'{image_folder}\{filename}')
    cleanname=os.path.splitext(filename)[0]         #splits the text into touple of filename and extention
    img.save(f'{output_folder}\{cleanname}.png','png')
    #print("All Done")

