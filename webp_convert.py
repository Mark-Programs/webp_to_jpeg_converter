from PIL import Image
import os

# function to try to create a directory
def create_dir(name):
    try:
        os.system(f'mkdir {name}')
    except:
        pass


#get the path of the current working directory
cwd = os.path.dirname(__file__)

# change the current working directory to the location of the python file itself
os.chdir(cwd)

# Try to create the directories below.  If they exist, just skip and move on.
folder_names = ['convert_from', 'converted_to'] 
for item in folder_names:
    create_dir(item)

# alter this path based on the path of your cwd
# directory = cwd + '\\python_stuff\\projects\\converters\\webp_to_jpeg'
image_loc = cwd + '/convert_from'
save_loc = cwd + '/converted_to'

# empty list to store file names in the image_loc dir
file_list = []

# iterate through the images in the image_loc dir, verify they are files, if so, append
for filename in os.listdir(image_loc):
    f = os.path.join(image_loc, filename)
    if os.path.isfile(f):
        file_list.append(filename)

# Assign empty list
img_list = []

# iterate through file_list, if the format is .webp, add to img_list
for img in file_list:
    tst = img[-5:]
    webp_fmt = ['.webp']
    if ".webp" in tst:
        img_list.append(img)

# iterate through img_list, convert to RGB and save as JPG in save_loc
for img in img_list:
    noext = img[:-5]
    im = Image.open(image_loc + "\\" + img).convert("RGB")
    im.save(save_loc + "\\" + noext + ".jpg", "jpeg")
    print(f"{img} has been converted")

# NOTE: This will NOT delete the existing images, only convert them
#   After converting, verify file counts and proper conversion, then manually delete

