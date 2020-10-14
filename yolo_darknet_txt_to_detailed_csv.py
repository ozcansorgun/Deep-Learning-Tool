import os
import sys
import glob
from PIL import Image
import pandas as pd

# If you are working in another directory, you can use the line below.
# os.path.join(r'C:\Users\OZCAN\Desktop\images')

classes = []

if os.path.exists("classes.txt"):
    with open("classes.txt", "r") as classes_txt_file:
        classes = classes_txt_file.read().splitlines()
else:
    print("The file 'classes' was not found.")
    sys.exit(1)

data_list = []

for txt_file in glob.glob("*[!classes].txt"):
    filename = txt_file.replace(".txt", ".jpg")
    filesize = os.path.getsize(filename)
    img = Image.open(filename)
    width, height = img.size
    with open(txt_file, 'r') as txt:
        lines = txt.read().splitlines()
        count = 0
        for line in lines:
            values = [float(value) for value in line.split(' ')]
            xmin = int((values[1] * 2 - values[3]) * width / 2)
            ymin = int((values[2] * 2 - values[4]) * height / 2)
            xmax = int((values[1] * 2 + values[3]) * width / 2)
            ymax = int((values[2] * 2 + values[4]) * height / 2)
            data_list.append([filename, filesize, "{}", len(lines), count,
                              "{\"name\":\"rect\",\"x\":%d,\"y\":%d,\"width\":%d,\"height\":%d}" %
                              (xmin, ymin, xmax-xmin, ymax-ymin), "{}"])
            count+=1

data_df = pd.DataFrame(data_list, columns=['filename','file_size','file_attributes','region_count','region_id',
                                           'region_shape_attributes','region_attributes'])
data_df.to_csv("detailed_csv.csv", index=None)


