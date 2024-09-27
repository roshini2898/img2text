import streamlit as st 
import google.generativeai as genai
import os
from dotenv import load_dotenv
#load the environment 
load_dotenv()
#Configure the genai secret key
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
#Designing the page
st.title("Image to the application")
user_input=st.text_input("Input Prompt:")
uploaded_file=st.file_uploader("Upload the image...",type=["jpg","jpeg","png"])
#Displat the image on the page
from PIL import Image
img=""
if uploaded_file is not None:
    img=Image.open(uploaded_file)
    st.image(img,caption="uploaded_Image",use_column_width=True)

# Function fo revaluating the Image and Annotating it
def gemini_response(user_input,img):
    model = genai.GenerativeModel("gemini-1.5-flash") # we are not using gemini-pro bc it is useful in text
    if user_input!="":
        response= model.generate_content([user_input,img])
    else:
        response=model.generate_content(img)
    return response.text

submit=st.button("submit")


if submit:
    response=gemini_response(user_input=user_input,img=img)
    st.subheader("The response is:")
    st.write(response)
    




#st.sidebar.title("Model Diagnostics")
#st.sidebar.markdown("Click to know more")
#st.sidebar.button("Univariate Analysis")