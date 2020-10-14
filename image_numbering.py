import os
import glob

# If you are working in another directory, you can use the line below.
# os.path.join(r'C:\Users\OZCAN\Desktop\images')

# filename = "img%d" # 5 -> img5
filename = "img%05d" # 5 -> img00005

number = 100

for image_file in glob.glob("*.jpg"):
    os.rename(image_file, filename % number + ".jpg")
    txt_file = image_file.replace(".jpg",".txt")
    if os.path.exists(txt_file):
        os.rename(txt_file, filename % number + ".txt")
    xml_file = image_file.replace(".jpg",".xml")
    if os.path.exists(xml_file):
        with open(xml_file, "rt") as r_xml:
            data = r_xml.read()
            data = data.replace(image_file, filename % number + ".jpg")
        with open(xml_file, "wt") as w_xml:
            w_xml.write(data)
        os.rename(xml_file, filename % number + ".xml")
    number+=1