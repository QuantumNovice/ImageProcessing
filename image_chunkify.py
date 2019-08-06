'''
Code to split image into n*m blocks.

'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def chunkify(img, block_width=4, block_height=4):
    shape = img.shape
    x_len = shape[0]//block_width
    y_len = shape[1]//block_height
    #print(x_len, y_len)
    
    chunks = []
    x_indices = [i for i in range(0, shape[0]+1, block_width)]
    y_indices = [i for i in range(0, shape[1]+1, block_height)]

    shapes = list(zip(x_indices, y_indices))
    
    for i in range(len(shapes)):
        try:
            start_x = shapes[i][0]
            start_y = shapes[i][1]
            end_x = shapes[i+1][0]
            end_y = shapes[i+1][1]
            chunks.append( shapes[start_x:end_x][start_y:end_y] )
        except IndexError:
            print('End of Array')

    return chunks
    
img = Image.open('image_data/lena.jpg')
img = np.array(img)

blocks = chunkify(img)

#print(img.shape)
#plt.matshow(img)
#plt.show()
