# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 16:08:27 2025

@author: Sakthi Spark
"""

import numpy as np
import pickle
import streamlit as st

# Load the saved model

file_path = r"C:/Users/Sakthi Spark/Desktop/AI and ML/Model deploying/Label data/trained_model.sav"

try:
    with open(file_path, 'rb') as f:
        loaded_model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("File not found. Check the path.")
except Exception as e:
    print("Error loading model:", e)


# Prediction function
def recall_prediction(Product_Description, Manufacturing_Recall_Reason):
    input_data = [Product_Description + " " + Manufacturing_Recall_Reason]  # Combine inputs
    prediction = loaded_model.predict(input_data)
    if prediction[0] == 0:
        return "Product won't be recalled"
    else:
        return "Product will be recalled"

# Streamlit app
def main():
    st.title('Labelling Recall Webapp')
    
    # Input fields
    Product_Description = st.text_input('Product Description')
    Manufacturing_Recall_Reason = st.text_input('Manufacturing Recall Reason')
    
    # Button for prediction
    if st.button('Predict Recall'):
        if Product_Description and Manufacturing_Recall_Reason:
            recall = recall_prediction(Product_Description, Manufacturing_Recall_Reason)
            st.success(recall)
        else:
            st.warning("Please fill in all fields.")

if __name__ == '__main__':
    main()
