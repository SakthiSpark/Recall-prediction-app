# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
#loading the saved model
loaded_model=pickle.load(open('C:/Users/Sakthi Spark/Desktop/AI and ML/Model deploying/Label data/trained_model.sav','rb'))

X_new = X_test[80]

prediction = loaded_model.predict(X_new)
print(prediction)

if (prediction[0]==0):
  print('Product wont be recalled ')
else:
  print('Product will be recalled')