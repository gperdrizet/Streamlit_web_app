'''Simple Streamlit web app.'''
import pickle
import pandas as pd
import streamlit as st

# Load the model
model_file='../models/model.pkl'

with open(model_file, 'rb') as input_file:
    model=pickle.load(input_file)

# Dictionary to translate numerical predictions into
# human readable strings
class_dict={
    '0': 'Not diabetic',
    '1': 'Diabetic'
}

# Page title
st.title('Diabetes prediction')

# Sliders for input data
glucose=st.slider('Glucose', min_value=0.0, max_value=200.0, step=1.0)
insulin=st.slider('Insulin', min_value=0.0, max_value=300.0, step=1.0)
bmi=st.slider('BMI', min_value=0.0, max_value=100.0, step=1.0)
age=st.slider('Age', min_value=1, max_value=90, step=1)

# When the user clicks 'Predict'
if st.button('Predict'):

    # Format the data for inference
    data=pd.DataFrame.from_dict({
        'Glucose': [glucose],
        'Insulin': [insulin],
        'BMI': [bmi],
        'Age': [age]
    })

    # Print out the input features to the terminal for troubleshooting
    print(data.head())

    # Do the prediction
    prediction=str(model.predict(data)[0])

    # Convert the predicted value to a human readable string
    pred_class=class_dict[prediction]

    # Display the prediction to the user
    st.write('Prediction:', pred_class)