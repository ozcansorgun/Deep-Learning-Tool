import os
import glob

extension = ".jpg"

# If you are working in another directory, you can use the line below.
# os.path.join(r'C:\Users\OZCAN\Desktop\images')

for filename in glob.glob('*' + extension):
        txt_name = filename.replace(extension,'') + '.txt'
        if not os.path.exists(txt_name):
            f = open(txt_name,"w+")
            f.close()