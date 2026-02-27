import streamlit as st
import pandas as pd
file=st.file_uploader("Upload a CSV file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    total_production = df['Production'].sum()/1e9
    st.metric("Total Production",f"{total_production:.2f}","Billions")
    topstate = df.groupby('State_Name')['Production'].sum().sort_values(ascending=False).head(5)
    st.bar_chart(topstate,sort=False)
    st.dataframe(df)