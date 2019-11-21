from imageai.Detection import ObjectDetection
import random
import os
from PIL import Image

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

name=[]
with open("iname.csv","r") as f:
    for lines in f:
        name.append(lines[:-1])
        random.shuffle(name)
print(name)

item=[]
pname=[0]*10
for i in range(50):
    image_in='C:\\Users\\Satyamskillz\\PycharmProjects\\project1\\1000\\{}.png'.format(name[i])
    image_out ='C:\\Users\\Satyamskillz\\PycharmProjects\\project1\\1000\\output\\{}.png'.format(name[i])
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image_in), output_image_path=os.path.join(execution_path , image_out))
    item.append(detections)

for i in item:
    for eachObject in i:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
