from PIL import Image
import os

path = 'photos/'
for file in os.listdir(path):
    im = Image.open(path+file)
    x, y = im.size
    small_size = int(x * 0.5), int(y * 0.5)
    out = im.resize(small_size)
    out.save(path+'new_'+file)
    print(file)










































# from PIL import Image

# im = Image.open('old.jpeg')
# x, y = im.size
# small_size = int(x * 0.5), int(y * 0.5)
# out = im.resize(small_size)
# out.save('new.jpeg')
