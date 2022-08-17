# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:19:06 2022

@author: user
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt
st.set_page_config(page_title="Fuel Monetering System Dashboard")
@st.cache
def get_data_from_excel():
    df=pd.read_csv('fuel_monetering-system_dashboard\dashboard.csv')
#st.dataframe(df)
    df["year"]=pd.to_datetime(df["Time"]).dt.year
    return df
df=get_data_from_excel()


st.sidebar.header("please filter here")
port = st.sidebar.multiselect("select port name",options=df["Port_name"].unique(),default=df["Port_name"].unique())
date = st.sidebar.multiselect("select date",options=df["Time"].unique(),default=df["Time"].unique())




df_selection=df.query("Port_name == @port & Time == @date")



st.title("fuel dashboard")
st.markdown('##')

total_fuelConsumed = int(df_selection["fuel_consumed"].sum()) 
average_fuelConsumed=round(df_selection['fuel_consumed'].mean(),2)
cost=int(df_selection["cost"].sum()) 
left_column,middle_column,right_column =st.columns(3)
with left_column:
    st.subheader("Total fuel consumed:")
    st.subheader(f"ton {total_fuelConsumed:,}")
with middle_column:
    st.subheader("Total fuel consumed:")
    st.subheader(f"ton {average_fuelConsumed:,}")
with right_column:
    st.subheader("Total cost")    
    st.subheader(f"US $  {cost:,}")
st.markdown("----")
import plotly.graph_objects as go
fig = go.Figure(
    go.Pie(
    labels = port,
    values =df["fuel_consumed"],
    hoverinfo = "label+percent",
    textinfo = "value"
))
st.plotly_chart(fig)

#fuelConsumption_by_port =(df_selection.groupby(by=["Port_name"]).sum()[["fuel_consumed"]])
#fig_fuelConsumption=px.bar(fuelConsumption_by_port, x="fuel_consumed",orientation='h',
#                          title="<b>fuel_consumption by ports<b>",
#                           color_discrete_sequence=["#0083B8"] * len(fuelConsumption_by_port),
#                           template="plotly_white",)
#st.plotly_chart(fig_fuelConsumption)
fuelConsumption_by_time =(df_selection.groupby(by=["Time"]).sum()[["fuel_consumed"]])
fig_fuelConsumptionByTime=px.line(fuelConsumption_by_time, x="fuel_consumed",orientation='v',
                           title="<b>fuel_consumption by Time<b>",
                           color_discrete_sequence=["#0083B8"] * len(fuelConsumption_by_time),
                           template="plotly_white",)
#st.plotly_chart(fig_fuelConsumptionByTime)

fuelConsumption_by_year =(df_selection.groupby(by=["year"]).sum()[["fuel_consumed"]])
fig_fuelConsumptionByYear=px.line(fuelConsumption_by_year, x="fuel_consumed",orientation='v',
                           title="<b>fuel_consumption by year<b>",
                           color_discrete_sequence=["#0083B8"] * len(fuelConsumption_by_year),
                           template="plotly_white",)
#st.plotly_chart(fig_fuelConsumptionByYear)

left_column,right_column =st.columns(2)

left_column.plotly_chart(fig_fuelConsumptionByTime,use_container_width=True)
right_column.plotly_chart(fig_fuelConsumptionByYear,use_container_width=True)

df1=pd.read_csv('E:\samidha_SIH\datasets\indexed-dataFrame.csv')

col1,col2=st.columns(2)

scatter_chart = st.altair_chart(
    alt.Chart(df1)
        .mark_circle(size=60)
        .encode(x='fuelConsumption', y='shaftSpeed')
        .interactive()
)
scatter_chart1 = st.altair_chart(
    alt.Chart(df1)
        .mark_circle(size=60)
        .encode(x='fuelConsumption', y='draftForward')
        .interactive()
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
