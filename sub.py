from PIL import Image
import numpy as np

image1=Image.open('new_image.png')
image2=Image.open('Encoded_image.png')

list1=np.asarray(image1)
list2=np.asarray(image2)

subtracted_list=np.subtract(list2,list1)
data=Image.fromarray(subtracted_list)
data.save('Decoded_message.png')