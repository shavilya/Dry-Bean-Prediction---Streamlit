import pandas as pd 
import numpy as np 

import streamlit as st 
import pickle 

with open('model.pkl' ,'rb') as file : 
    model = pickle.load(file)


def predict_class(Area,Perimeter,MajorAxisLength,MinorAxisLength,AspectRation,Eccentricity,ConvexArea,EquivDiameter,Extent,Solidity,roundness,Compactness,ShapeFactor1,ShapeFactor2,ShapeFactor3,ShapeFactor4) : 

    input = np.array([[Area,Perimeter,MajorAxisLength,MinorAxisLength,AspectRation,Eccentricity,ConvexArea,EquivDiameter,Extent,Solidity,roundness,Compactness,ShapeFactor1,ShapeFactor2,ShapeFactor3,ShapeFactor4]]).astype(float)
    prediction = model.predict(input)

    return int(prediction)


def main() : 

    st.title("Dry Bean Prediction - Streamlit Application")
    html_temp = """
        <div style="background:grey ;padding:10px">
        <b style="color:white;text-align:center;">The actual Class are 'SEKER' : 0 , 'BARBUNYA' : 1 , 'BOMBAY' : 2 ,'CALI' : 3 , 'HOROZ' : 4 , 'SIRA' : 5 , 'DERMASON' : 6</b>
        </div> """

    st.markdown(html_temp , unsafe_allow_html = True)

    Area = st.text_input("Area: ")
    Perimeter = st.text_input("Perimeter: ")
    MajorAxisLength = st.text_input("MajorAxisLength: ")
    MinorAxisLength = st.text_input("MinorAxisLength: ")
    AspectRation = st.text_input("AspectRation: ") 
    Eccentricity = st.text_input("Eccentricity: ") 
    ConvexArea = st.text_input("ConvexArea: ") 
    EquivDiameter = st.text_input("EquivDiameter: ")
    Extent = st.text_input("Extent: ")
    Solidity = st.text_input("Solidity: ")
    roundness = st.text_input("roundness: ")
    Compactness = st.text_input("Compactness: ") 
    ShapeFactor1 = st.text_input("ShapeFactor1: ")
    ShapeFactor2 = st.text_input("ShapeFactor2: ")
    ShapeFactor3 = st.text_input("ShapeFactor3: ")
    ShapeFactor4 = st.text_input("ShapeFactor4: ")

   

    if st.button("Predict the Class") : 
        output = predict_class(Area,Perimeter,MajorAxisLength,MinorAxisLength,AspectRation,Eccentricity,ConvexArea,EquivDiameter,Extent,Solidity,roundness,Compactness,ShapeFactor1,ShapeFactor2,ShapeFactor3,ShapeFactor4)
        st.success(f"The class of dry beans is {output}")

        

if __name__ == "__main__" : 
    main()