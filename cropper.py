import PIL
from PIL import Image
import io
import os
import cv2
import glob
import sys
import platform as pl
import numpy as np

def dir_Korean_change(path):
    dir_n = open(path.encode("utf-8"), "rb")
    change_by = bytearray(dir_n.read())
    npA = np.asarray(change_by, dtype=np.uint8)
    return cv2.imdecode(npA, cv2.IMREAD_UNCHANGED)

def add_zero_to_name(imnum):
    if imnum < 10:
        return '00' + str(imnum)
    elif imnum < 100:
        return '0' + str(imnum)
    else:
        return str(imnum)

directory = input("Enter Direcory : ")
EX = input("Enter extension(.jpg, .png) : ")

final_jpg_list = []
final_jpg_dir = []


if(EX == '.jpg'):
    extention = '*.jpg'
    if (pl.system() == 'Windows' or pl.system() == 'Linux' or pl.system() == 'Darwin'):
        for name in glob.glob(os.path.join(directory, extention)):
            final_jpg_list.append(name.split('\\')[-1].split('.')[0])  # split as '\\' ony available on WIndows and Linux
            final_jpg_dir.append(name)
    else:
        print("Unsupporting Operating System")
elif(EX == '.png'):
    extention = '*.png'
    if (pl.system() == 'Windows' or pl.system() == 'Linux' or pl.system() == 'Darwin'):
        for name in glob.glob(os.path.join(directory, extention)):
            final_jpg_list.append(name.split('\\')[-1].split('.')[0])  # split as '\\' ony available on WIndows and Linux
            final_jpg_dir.append(name)
    else:
        print("Unsupporting Operating System")
else:
    print("That format is not supported")
    sys.exit()

print("List of Directory : ",final_jpg_dir)
print("List of Img File name : ",final_jpg_list)

#size of width for cropping
crop_size_w = int(input("Enter width for Cropping : "))
#size of height for cropping
crop_size_h = int(input("Enter height for Cropping : "))

#overlap percentage value
crop_overlap_w =int(input("Enter width overlap degree(Standard : Percentage) : "))
crop_overlap_h = int(input("Enter height overlap degree(Standard : Percentage) : "))


for count in range(0,len(final_jpg_dir)):
    n_dir = directory + "\\" + final_jpg_list[count]

    try:
        if not(os.path.isdir(n_dir)):
            os.mkdir(n_dir)
    except OSError as OE:
        print("Unable to Create Directory in " + n_dir)
        sys.exit()

    #get pixel size of image with PIL.Image
    n_data_size = Image.open(final_jpg_dir[count])
    data_width,data_height = n_data_size.size


    #range_w = (int)(data_width / crop_size_w) + 1
    #range_h = (int)(data_height/crop_size_h) + 1
    print("In Process image size(Width,Value) : ",data_width,data_height)

    #starting point
    width_now = 0
    height_now = 0

    #overlap pixel data
    overlap_w = (int)(crop_size_w * ((100 - crop_overlap_w) / 100))
    overlap_h = (int)(crop_size_h * ((100 - crop_overlap_h) / 100))

    #image's numpy data for OpenCV
    n_data = dir_Korean_change(final_jpg_dir[count])
    #OpenCV lib has default setting as BGR so need to Convert RGB
    n_data = cv2.cvtColor(n_data,cv2.COLOR_BGR2RGB)
    #for img name
    imgcount = 1

    while(height_now < data_height):
        width_now = 0
        if (data_height - height_now) < crop_size_h:
            break
        while(width_now < data_width):
            if (data_width - width_now) < crop_size_w:
                break
            # Array slicing According to Numpy Array : [y : y+h,x:x+w] 'h' refers to height 'w' refers to width
            n_img = n_data[height_now:(height_now + crop_size_h),width_now:(width_now + crop_size_w)]
            imgname = final_jpg_list[count] + "_" + str(add_zero_to_name(imgcount))
            final = n_dir + "\\"+ imgname +".jpg"
            print(final)
            img_data = Image.fromarray(n_img,"RGB")
            img_data.save(final)
            #cv2.imwrite(final,n_img)
            width_now += overlap_w
            imgcount += 1
        height_now += overlap_h