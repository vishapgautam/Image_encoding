from PIL import Image
from numpy import asarray

image=Image.open('new_image.png')
image1=Image.open('message.png')

a,b=image.size
if a<500 or b<500:
   print("Size of original Image is less")

a,b=image1.size
if a<500 or b<500:
   print("Size of message image is less") 

#image.resize((500,500))
image1.resize((500,500))

#image.save('image121.png',format='png')
image1.save('message.png',format='png')

pixel_map=image.load()
pixel_map1=image1.load()

indexs=[]

for i in range(500):
    for j in range(500):
         r,g,b,a=image1.getpixel((i,j))
         if r<250 and g<250:
            indexs.append([i,j])

for i in indexs:
     r,g,b=image.getpixel((i[0],i[1]))
     if r==0 or g==0:
        pixel_map[i[0],i[1]]=(0,0,0)
     else:
        pixel_map[i[0],i[1]]=(r-1,g-1,b)
image.save("Encoded_image.png",format="png")
