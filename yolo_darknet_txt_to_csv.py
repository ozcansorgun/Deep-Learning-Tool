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
    img = Image.open(filename)
    width, height = img.size
    with open(txt_file, 'r') as txt:
        lines = txt.read().splitlines()
        for line in lines:
            values = [float(value) for value in line.split(' ')]
            class_name = classes[int(values[0])]
            xmin = (values[1] * 2 - values[3]) * width / 2
            ymin = (values[2] * 2 - values[4]) * height / 2
            xmax = (values[1] * 2 + values[3]) * width / 2
            ymax = (values[2] * 2 + values[4]) * height / 2
            data_list.append([filename, width, height, class_name, int(xmin), int(ymin), int(xmax), int(ymax)])

data_df = pd.DataFrame(data_list, columns=['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'])
data_df.to_csv("od_api_csv.csv", index=None)


