import pandas as pd
import streamlit as st
import process
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as px

st.set_page_config(page_title='Sales Dashboard',page_icon=':bar_chart:'
                   ,layout='wide')
col1,col2= st.columns(2)
# function Gender_wise###################################
import plotly.graph_objects as go

def plot_gauge(val) :
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = val,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Ratings"}))

    return fig
def plot_gender_wise():
    with st.expander('Total Spend'):

        fig = plt.figure(figsize=(3, 4))
        st.text("In Every Branch women dominated men During Purchase ")
        g=sns.barplot(data=df, x='Branch', y="Total", hue="Gender")
        plt.ylabel('one time Spent($)')
        st.pyplot(fig)
    # 2nd

    with st.expander('Total Revenue($'):
        st.text("In Terms on Revenue: Women Brought 20k($) Dollars more than Men ")
        Gender_wise_analysis=df.groupby('Gender').agg({'Total':'sum'}).reset_index()
        g=sns.catplot(data=Gender_wise_analysis,x='Gender',y='Total',kind='bar')
        plt.ylabel('Total Sales($).')
        st.pyplot(g)
    #3rd

    with st.expander('One time Spend($) By Customer Type.'):


        st.text('We can see there is Not much Increase in Purcahse in  Women %  even if they Become Member')
        st.text('But there is a Certain Increase in Purchase in Men if they are a regualr member.')
        st.text('We can use some schemes to attract new customers and make them our Regulars.')
        g=sns.catplot(data=df, x="Customer type", y="Total",hue='Gender',kind='bar')

        plt.ylabel('One time spend($')
        st.pyplot(g)
    with st.expander("Distribution of Income/Revenue"):

    # 4t
        st.text("We can see there is a lot of man in the 0-200 $ distribution ")
        st.text("Certainly they dominated a Area but in terms of spending Money but compare to women they did not "
            "Spent Much ")
        st.text('in the higher Distribution.')
        g=sns.displot(data=df,x='Total',hue='Gender')
        st.pyplot(g)
        plt.xlabel('Total Spent($)')
        plt.ylabel('Frequency')
    with st.expander('Density Estimation'):

        st.subheader("We can Understand the whole thing using density estimation")
        g=sns.displot(data=df, x="Total", hue="Gender", kind="kde")
        plt.xlabel('Total One time Spend($)')
        st.text("We Can see the Male is Densely populated in 200 $ Region and then Dropped interest.")
        st.text("But in Women we can see that they started to take interest after 200$ region")
        st.pyplot(g)

    with st.expander("branch rating "):

        st.pyplot(sns.catplot(df,x='Branch',y='Rating',hue='Gender',kind='bar'))
    with st.expander("Gauge Ratings"):
        gauge_graph=df.groupby("Gender")['Rating'].mean()
        st.header("Ratings Overall")
        st.subheader("Ratings by Male")
        st.plotly_chart(plot_gauge(gauge_graph.Male))
        st.subheader('Ratings by Female')
        st.plotly_chart(plot_gauge(gauge_graph.Female))

# branch A is rated more by men the reason must be that the interaction with males is good and  the population of women is less there or not good interaction with Females
    #####################################################
st.header("Dashboard application ")
st.markdown('V 0.1.3')
with st.sidebar:
    st.header("configuration")
    # path= st.file_uploader('upload_file_here')
    path= 'supermarket_sales.csv'
# if path is None:
#     st.info('Please upload Here')
#     st.stop()

df= process.load_Data(path)


user_menu= st.sidebar.radio('Select an option',['Basic','Gender-Wise-Analysis','Branch_wise'])
if user_menu=="Basic":

    with st.expander("Sales Table Expand"):
        st.dataframe(df)
    with st.expander("Overall Revenue Density Estimation"):
        st.text("we can see the Density of Revenue is in the range 0-400 $")
        st.pyplot(sns.displot(data=df,x='Total',kind='kde'))
    with st.expander("Revenue Bar chart"):

        st.text('To understand it better let us look at the histogram')
        st.text("we can see that More than half the Data Belongs in the region 0-400 $")
        st.text(" To lure them more we can provide discount in that Region.")
        st.pyplot(sns.displot(data=df,x='Total'))

if user_menu=="Gender-Wise-Analysis":

    plot_gender_wise()
    # df= process.load_Data(path)



