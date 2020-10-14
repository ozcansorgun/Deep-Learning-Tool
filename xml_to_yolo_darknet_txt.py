import os
import glob
import xml.etree.ElementTree as ET

# If you are working in another directory, you can use the line below.
# os.path.join(r'C:\Users\OZCAN\Desktop\images')

classes = []

if os.path.exists("classes.txt"):
    with open("classes.txt", "r") as classes_txt_file:
        classes = classes_txt_file.read().splitlines()
else:
    classes = ["dog", "person", "cat", "tv", "car", "meatballs", "marinara sauce",
               "tomato soup", "chicken noodle soup", "french onion soup",
               "chicken breast", "ribs", "pulled pork", "hamburger", "cavity"
               ]

for xml_file in glob.glob("*.xml"):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filename = root.find("filename").text
    txt_file = open(filename.replace(".jpg",".txt"), "w")
    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)
    for member in root.findall('object'):
        class_name = member.find("name").text
        xmin = int(member.find("bndbox")[0].text)
        ymin = int(member.find("bndbox")[1].text)
        xmax = int(member.find("bndbox")[2].text)
        ymax = int(member.find("bndbox")[3].text)
        if not class_name in classes:
            classes.append(class_name)
        class_id = classes.index(class_name)
        text = "%d %.6f %.6f %.6f %.6f\n" % (class_id, ((xmax + xmin) / 2) / width, ((ymax + ymin) / 2) / height,
                                             (xmax - xmin) / width, (ymax - ymin) / height)
        txt_file.write(text)
    txt_file.close()

with open("classes.txt", "w") as classes_txt_file:
    classes_txt_file.writelines(["%s\n" % c for c in classes])
