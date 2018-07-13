import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

img_width, img_height = 150, 150
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = model.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("Label: 
    	Celine")
  elif answer == 1:
    print("Labels: Chanel")
  elif answer == 2:
    print("Label: Givenchy")

  return answer


Celine_t = 0

Celine_f = 0
Chanel_t = 0
Chanel_f = 0
Givenchy_t = 0
Givenchy_f = 0

for i, ret in enumerate(os.walk('./test-data/
	Celine')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Label: 
    	Celine")
    result = predict(ret[0] + '/' + filename)
    if result == 0:
      
      Celine_t += 1
    else:
      
      Celine_f += 1

for i, ret in enumerate(os.walk('./test-data/Chanel')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Label: Chanel")
    result = predict(ret[0] + '/' + filename)
    if result == 1:
      Chanel_t += 1
    else:
      Chanel_f += 1

for i, ret in enumerate(os.walk('./test-data/Givenchy')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Label: Givenchy")
    result = predict(ret[0] + '/' + filename)
    if result == 2:
      Givenchy_t += 1
    else:
      Givenchy_f += 1

"""
Check metrics
"""
print("True 
	Celine: ", 
Celine_t)
print("False 
	Celine: ", 
Celine_f)
print("True Chanel: ", Chanel_t)
print("False Chanel: ", Chanel_f)
print("True Givenchy: ", Givenchy_t)
print("False Givenchy: ", Givenchy_f)