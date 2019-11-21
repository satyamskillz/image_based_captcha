from PIL import Image
import os
size_1000=(1000,1000)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i=Image.open(f)
        fn,fext=os.path.splitext(f)

        i.thumbnail(size_1000,Image.NEAREST)
        i.save('1000/{}.png'.format(fn))
#image1=Image.open('bicycle00.jpg')
#image1.show()