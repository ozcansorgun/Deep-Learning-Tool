import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

# If you are working in another directory, you can use the line below.
# os.path.join(r'C:\Users\OZCAN\Desktop\images')

data_list = []

for xml_file in glob.glob("*.xml"):
    image_name = xml_file.replace(".xml",".jpg")
    if os.path.exists(image_name):
        filesize = os.path.getsize(image_name)
    else:
        filesize = 0
    tree = ET.parse(xml_file)
    root = tree.getroot()
    count=0
    for member in root.findall('object'):
        filename = root.find('filename').text
        xmin = int(member.find("bndbox")[0].text)
        ymin = int(member.find("bndbox")[1].text)
        xmax = int(member.find("bndbox")[2].text)
        ymax = int(member.find("bndbox")[3].text)
        data_list.append([filename, filesize, "{}", len(root.findall('object')), count,
                          "{\"name\":\"rect\",\"x\":%d,\"y\":%d,\"width\":%d,\"height\":%d}" %
                          (xmin, ymin, xmax - xmin, ymax - ymin), "{}"])
        count += 1

data_df = pd.DataFrame(data_list, columns=['filename','file_size','file_attributes','region_count','region_id',
                                           'region_shape_attributes','region_attributes'])
data_df.to_csv("detailed_csv.csv", index=None)