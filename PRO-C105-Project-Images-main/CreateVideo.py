import os
import cv2

path = "Images/"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)

print(len(images))
count = (len(images))
frame = cv2.imread(images[0])
height,width,fps = frame.shape

m =  cv2.VideoWriter("m.mp4",cv2.VideoWriter_fourcc(*'DIVX'),24,(width,height))

for x in range (0,count):
    image_reader = cv2.imread(images[x])
    m.write(image_reader)
    cv2.imshow("m",image_reader)
    cv2.waitKey(1112)
    
m.release()