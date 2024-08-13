import streamlit as st
from PIL import Image
import os
import numpy as np
import requests
from io import BytesIO
import tensorflow as tf
import cv2

model = tf.keras.models.load_model('model.h5')

def Prediction(image):
    image = Image.open(image)
    image = image.resize((128, 128))
    image = image.convert('RGB')
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    return 'Mask' if prediction > 0.5 else 'No Mask'


def url():
    url = st.text_input('Enter Url')
    if st.button('Submit'):
        st.snow()
        response = requests.get(url)
        image = BytesIO(response.content)
        st.image(image, caption='Image from URL', use_column_width=True)
        result = Prediction(image)
        st.success(result)

def Image_Upload():
    file = st.file_uploader('Upload File',type=['jpg','jpeg','png','webp'])
    if st.button('Submit'):
        st.snow()
        st.image(file, caption='Image from URL', use_column_width=True)
        result = Prediction(file)
        st.success(result)

def Live():
    st.caption('Alert! You have Camera in your Device')
    st.caption('First Adjust Your Face in Camera')
    st.caption('Then Press ESC to Click Image')
    if st.button('Click Here To Continue'):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("Error: Unable to open camera.")
            return None
        
        path = 'capture.jpg'
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Camera', frame)
                if cv2.waitKey(1) & 0xFF == 27:  # ESC key to capture
                    out = cv2.imwrite(path, frame)
                    break

        cap.release()
        cv2.destroyAllWindows()
        st.image(path, caption='Image from URL', use_column_width=True)
        result = Prediction(path)
        st.success(result)



def main():
    st.title('Face Mask Detection')
    with st.sidebar:
        st.title('Please Fill Requirement 🖋 ')
        option = st.radio(
            "Select Type",
            ("Image Upload", "Url",'Live'))
        st.write('')
        st.subheader('Follow Me 🎓')
        st.link_button("Connect LinkedIn",'https://www.linkedin.com/in/alihassanml')
        st.link_button("Connect On Github",'https://github.com/alihassanml',type="secondary")
        st.caption('Develop by: Ali Hassan')
    if option =='Url':
        url()
    elif option == 'Live':
        Live()
    else:
        Image_Upload()
    

if __name__ == '__main__':
    main()