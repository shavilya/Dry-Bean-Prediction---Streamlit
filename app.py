import pandas as pd 
import numpy as np 

import streamlit as st 
import pickle 

from sklearn.preprocessing import StandardScaler 

with open('./artifacts/model.pkl' ,'rb') as file : 
    model = pickle.load(file)


def predict_class(Area,Perimeter,MajorAxisLength,MinorAxisLength,AspectRation,Eccentricity,ConvexArea,EquivDiameter,Extent,Solidity,roundness,Compactness,ShapeFactor1,ShapeFactor2,ShapeFactor3,ShapeFactor4) : 

    input_data = pd.DataFrame({
        'Area' : [Area],
        'Perimeter' : [Perimeter],
        'MajorAxisLength' : [MajorAxisLength],
        'MinorAxisLength': [MinorAxisLength],
        'AspectRation': [AspectRation],
        'Eccentricity': [Eccentricity],
        'ConvexArea': [ConvexArea],
        'EquivDiameter': [EquivDiameter],
        'Extent': [Extent],
        'Solidity': [Solidity],
        'roundness': [roundness],
        'Compactness': [Compactness],
        'ShapeFactor1': [ShapeFactor1],
        'ShapeFactor2': [ShapeFactor2],
        'ShapeFactor3': [ShapeFactor3],
        'ShapeFactor4': [ShapeFactor4]

    })

    st = StandardScaler()
    input_data_scaled = st.fit_transform(input_data)
    prediction = model.predict(input_data_scaled)
    return prediction[0]

def main() : 

    st.title("Dry Bean Prediction - Streamlit Application")
    html_temp = """
        <div style="background:grey ;padding:10px">
        <b style="color:white;text-align:center;">The actual Class are 'SEKER' : 0 , 'BARBUNYA' : 1 , 'BOMBAY' : 2 ,'CALI' : 3 , 'HOROZ' : 4 , 'SIRA' : 5 , 'DERMASON' : 6</b>
        </div> """

    st.markdown(html_temp , unsafe_allow_html = True)

    Area = st.number_input("Area: " , min_value = 20420 , max_value = 254616 , value= 20523)
    Perimeter = st.number_input("Perimeter: " , min_value = 525 , max_value = 740 ,value = 630)
    MajorAxisLength = st.number_input("MajorAxisLength: " , min_value =184 , max_value=738 , value = 200)
    MinorAxisLength = st.number_input("MinorAxisLength: " , min_value=122 , max_value=460 , value = 150)
    AspectRation = st.number_input("AspectRation: ", min_value = 1 , max_value = 3  , value = 2) 
    Eccentricity = st.number_input("Eccentricity: " , min_value = 0 , max_value= 1 , value = 1) 
    ConvexArea = st.number_input("ConvexArea: " , min_value=20684 , max_value=263261 ,value = 30000) 
    EquivDiameter = st.number_input("EquivDiameter: " , min_value=161 , max_value=570 , value = 500)
    Extent = st.number_input("Extent: " , min_value= 0 , max_value= 1 , value = 1)
    Solidity = st.number_input("Solidity: " , min_value= 1 , max_value= 2 , value = 1)
    roundness = st.number_input("roundness: " , min_value=0 , max_value=1 , value = 1)
    Compactness = st.number_input("Compactness: " , min_value=0 , max_value= 1 , value = 1) 
    ShapeFactor1 = st.number_input("ShapeFactor1: " , min_value=0 , max_value= 1 , value = 1)
    ShapeFactor2 = st.number_input("ShapeFactor2: " , min_value=0 , max_value= 1 , value = 1)
    ShapeFactor3 = st.number_input("ShapeFactor3: " , min_value=0 , max_value= 1 , value = 1)
    ShapeFactor4 = st.number_input("ShapeFactor4: " , min_value=0 , max_value= 1 , value = 1)

   

    if st.button("Predict the Class") : 
        output = predict_class(Area,Perimeter,MajorAxisLength,MinorAxisLength,AspectRation,Eccentricity,ConvexArea,EquivDiameter,Extent,Solidity,roundness,Compactness,ShapeFactor1,ShapeFactor2,ShapeFactor3,ShapeFactor4)
        st.success(f"The class of dry beans is {output}")



if __name__ == "__main__" : 
    main()