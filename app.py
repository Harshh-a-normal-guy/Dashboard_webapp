import pandas as pd
import streamlit as st
import process
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Sales Dashboard',page_icon=':bar_chart:'
                   ,layout='wide')
col1,col2= st.columns(2)
# function Gender_wise###################################
def plot_gender_wise():
    fig = plt.figure(figsize=(5, 4))
    g=sns.barplot(data=df, x='Branch', y="Total", hue="Gender")
    st.pyplot(fig)
    # 2nd
    st.subheader("Total Sales by Gender")
    Gender_wise_analysis=df.groupby('Gender').agg({'Total':'sum'}).reset_index()
    g=sns.catplot(data=Gender_wise_analysis,x='Gender',y='Total',kind='bar')
    st.pyplot(g)
    #####################################################
st.header("Dashboard application ")
st.markdown('V 0.1.2')
with st.sidebar:
    st.header("configuration")
    # path= st.file_uploader('upload_file_here')
    path= 'supermarket_sales.csv'
# if path is None:
#     st.info('Please upload Here')
#     st.stop()
# @st.cache_data
df= process.load_Data(path)
# with st.expander("Sales Data Expand"):


user_menu= st.sidebar.radio('Select an option',['Basic','Gender-WiseAnalysis','Branch_wise'])
if user_menu=="Basic":
    st.dataframe(df)

if user_menu=="Gender-WiseAnalysis":
    st.header('Total Spend by Gender ')
    plot_gender_wise()
    # df= process.load_Data(path)



