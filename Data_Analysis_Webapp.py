#Vaishnavi Kenjale

#Imports
import streamlit as st

#to load dataset
import pandas as pd

#to visualize data
import seaborn as sns
import matplotlib.pyplot as plt

# Add Image
st.image("https://cdn.vectorstock.com/i/500p/56/73/data-analysis-concept-vector-25125673.jpg", width=100)

# 1.Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis using Python")

st.write(" ")
st.write(" ")
st.write(" ")

# Upload Dataset
upload = st.file_uploader("Upload Your Dataset (In csv or xlsx Format)", type = ["csv", "xlsx"])

if upload is not None:
    if upload.name.endswith('.csv'):
        data = pd.read_csv(upload)
    elif upload.name.endswith('.xlsx'):
        data = pd.read_excel(upload)
    
    
# Show Dataset
if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
        
st.write(" ")
        
# Check Datatype of Each Column
if upload is not None:
    if st.checkbox("Check DataType Of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)
        
st.write(" ")

# Find shape of Dataset (No. of rows and columns)
if upload is not None:
    if st.checkbox("Check Dimension"):
        data_shape = st.radio("What Dimension Do You Want To Check ?",('Rows','Columns'))
    
        if data_shape=='Rows':
            st.text("Number Of Rows")
            st.write(data.shape[0])
        if data_shape=='Columns':
            st.text("Number of columns")
            st.write(data.shape[1])
            
st.write(" ")
            
# Find Null Values in The Dataset
if upload is not None:
    text = data.isnull().values.any()
    if text == True:
        if st.checkbox("Null Values in the Dataset"):
            st.text("Yes, missing values are present.")
            fig, ax = plt.subplots()
            sns.heatmap(data.isnull(), ax=ax, cbar=False)
            st.pyplot(fig)
            
            hmissing = st.selectbox("Do You Want To Handle Missing Data",("Choose One","Yes","No"))
            if hmissing == "Yes":
                filopt = st.selectbox("How Do You Want To Handle Missing Data",("Select One", "Fill Missing Values", "Make A Guess On Missing Values", "Drop Missing Values"))
                
                if filopt == "Fill Missing Values":
                    filmis = st.selectbox("How Do You Want To Fill Missing Data",("Select One", "Fill Missing Values With 0", "Fill Missing Values With 'NA'", "Forward Fill", "Backward Fill"))
                    if filmis == "Fill Missing Values With 0":
                        data=data.fillna(0, inplace=True)
                        st.success("Missing Values Successfully Filled With 0")
                    if filmis == "Fill Missing Values With 'NA'":
                        data=data.fillna('NA', inplace=True)
                        st.success("Missing Values Successfully Filled With 'NA'")
                    if filmis == "Forward Fill":
                        data=data.fillna(method = "ffill", inplace=True)
                        st.success("Missing Values Successfully Filled")
                    if filmis == "Backward Fill":
                        data=data.fillna(method = "bfill", inplace=True)
                        st.success("Missing Values Successfully Filled")
                        
                if filopt == "Make A Guess On Missing Values":
                    data=data.interpolate()
                    st.success("Missing Values Successfully Filled")
                    
                if filopt == "Drop Missing Values":
                    dropval = st.selectbox("How Do You Want To Drop Missing Values",("Select One", "Row Wise", "Column Wise"))
                    if dropval == "Row Wise":
                        data.dropna(axis=0, inplace=True)
                        st.success("Missing Values Successfully Drop")
                    if dropval == "Column Wise":
                        data.dropna(axis=1, inplace=True)
                        st.success("Missing Values Successfully Drop")
                        
            if hmissing == "No":
                st.text("Ok No Problem")
            
    else:
        st.success("Congratulations!! No Missing Values")
        

st.write(" ")
        
# Find Duplicate Values in the Dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Choose One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
        
st.write(" ")

# Returns series with frequency of each value
if upload is not None:
    if st.checkbox("Returns series with frequency of each value"):
        st.write(data.value_counts())
       
st.write(" ")

# Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))

st.write(" ")
        
# Getting Information About Memory
import io
if upload is not None:
    if st.checkbox("Information About Dataset"):
        buffer = io.StringIO()
        data.info(verbose=False, memory_usage="deep", buf=buffer)
        s = buffer.getvalue()
        st.success(s)

st.write(" ")
        
# About Section
if st.button("About App"):
    st.text("Upload csv or xlsx format dataset and analyze it using python.")

st.write(" ")
    
# Download Updated File
if upload is not None:
    if st.button("Save Updated DataFrame"):
        open('data_streamlit.csv', 'w').write(data.to_csv())
        st.text("Saved To local Drive")


st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

# By
if st.checkbox("By", value=True):
    st.success("Vaishnavi Kenjale")
    st.write("Checkout My Linkedin Profile","<https://www.linkedin.com/in/vaishnavikenjale/>")
    st.write("Checkout My GitHub","<https://github.com/VaishnaviKenjale>/<https://github.com/VaishnaviKenjale/Data-Analysis-WebApp>")
    



# Set the background image
def set_background(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({url});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image URL
set_background("https://img.freepik.com/free-photo/global-communication-background-business-network-design_53876-160250.jpg?t=st=1724753211~exp=1724756811~hmac=28589fa0cf5120ee6c23a09b9f88d7f376505012da50c19f482b51dae9143856&w=996")

