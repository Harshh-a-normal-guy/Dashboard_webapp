import streamlit as st


import process

st.header("Dashboard application Supermarket Sales Data")
st.markdown('0.1.1')
path= st.file_uploader('upload_file_here')
df= process.load_Data(path)

with st.expander("Sales Data Expand"):

    st.dataframe(df)

