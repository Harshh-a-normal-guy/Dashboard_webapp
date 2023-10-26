import streamlit as st


import process

st.header("Dashboard application Supermarket Sales Data")
st.markdown('0.1.1')
path= r'D:\data structures Notes\python_pro\venv\supermarket_sales - Sheet1.csv'
df= process.load_Data(path)

with st.expander("Sales Data Expand"):

    st.dataframe(df)

