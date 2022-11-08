import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Interact with Gapminder Data")

df = pd.read_csv("G:/My Drive/MADS course transcripts/699 Capstone/coi_district_grouped.csv")
#df_gdp_o = df.query("continent=='Oceania' & metric=='gdpPercap'")

title = "GDP for countries in Oceania"
fig = px.line(df, x = "year", y = "NAME_LEA15", color = "year", title = title)
st.plotly_chart(fig, use_container_width=True)