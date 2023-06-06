#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data = pd.read_csv('MovieGenre.csv', encoding='latin1')

data[['Title', 'Year']] = data['Title'].str.split('(', 1, expand=True)
columns = ['Title','Year','IMDB Score','Genre']
df = data[columns]
print(df)


# In[1]:


import pandas as pd
import requests
from PIL import Image
import numpy as np
import io

data = pd.read_csv('MovieGenre.csv', encoding='latin1')
df1 = data['Poster']

# Function to convert image link to NumPy array
def image_link_to_array(link):
    try:
        response = requests.get(link)
        img = Image.open(io.BytesIO(response.content))
        img_array = np.array(img)
        return img_array
    except Exception as e:
        print(f"Error converting image link to array: {e}")
        return None
    
# Function to resize the image array    
def resize_image(image_array, input_size):
    try:
        image = Image.fromarray(image_array)
        resized_image = image.resize((input_size, input_size))
        resized_array = np.array(resized_image)
        return resized_array
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None
    
image_arrays = []

for i in range(10):
    image_link = df1.iloc[i]
    image_array = image_link_to_array(image_link)
    if image_array is not None:
        new_array = resize_image(image_array, 299)
        if new_array is not None:
            print(f"Image {i+1} extracted")
            image_arrays.append(new_array)
        else:
            print(f"Error resizing image {i+1}")
    else:
        print(f"Error converting image {i+1} link to array")

all_images = np.array(image_arrays)
np.save('image_arrays.npy', all_images)

