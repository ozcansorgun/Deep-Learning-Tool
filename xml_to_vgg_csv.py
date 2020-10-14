import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

# If you are working in another directory, you can use the line below.
# os.path.join(r'C:\Users\OZCAN\Desktop\images')

data_list = []

for xml_file in glob.glob("*.xml"):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.findall('object'):
        filename = root.find('filename').text
        xmin = int(member.find("bndbox")[0].text)
        ymin = int(member.find("bndbox")[1].text)
        xmax = int(member.find("bndbox")[2].text)
        ymax = int(member.find("bndbox")[3].text)
        data_list.append([filename, ymax - ymin, xmax - xmin, xmin, ymin])

data_df = pd.DataFrame(data_list, columns=['filename', 'height', 'width', 'x', 'y'])
data_df.to_csv("vgg_csv.csv", index=None)