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
        data_list.append([root.find('filename').text,
                          int(root.find("size/width").text),
                          int(root.find("size/height").text),
                          member.find("name").text,
                          int(member.find("bndbox")[0].text),
                          int(member.find("bndbox")[1].text),
                          int(member.find("bndbox")[2].text),
                          int(member.find("bndbox")[3].text)
                          ])

data_df = pd.DataFrame(data_list, columns=['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'])
data_df.to_csv("od_api_csv.csv", index=None)




