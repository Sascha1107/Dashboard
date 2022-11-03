import streamlit as st
import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt
import time
from bokeh.plotting import figure
import numpy as np


df = pd.read_excel("Rohdaten.xlsx")

st.set_page_config(page_title="ARGE-Dashboard", layout="wide")





st.title(":bar_chart: ARGE-Dashboard")

#st.header("ARGE-Dashboard")



st.sidebar.header("Bitte hier filtern")

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)

region = st.sidebar.multiselect("Auswahl Region",
options=df["Region"].unique(),
default=df["Region"].unique())


Bahnstelle = st.sidebar.multiselect("Auswahl Bahnstell",
                        options=df["Bahnstelle"].unique(),
                        default=df["Bahnstelle"].unique()
                        )


###First Row in Main-Part

contract_value = int(df["Auftragswert"].sum())
calculation_value = int(df["Kalkulationswert"].sum())


col1, col2, col3 = st.columns(3)



with col1:
   st.header("Auftragswert Gesamt")
   st.write(f"{contract_value}")


with col2:
   st.header("Kalkulationswert gesamt")
   st.write(f"{calculation_value}")


with col3:
   st.header("Projektanzahl gesamt")









#st.balloons()


## Interactive Visaulization

col4, col5, = st.columns(2)


with col4:
    st.bar_chart(df["Kalkulationswert"])

with col5:
    chart_data = pd.DataFrame(
        df.groupby(by=["Projektkategorie"]).sum(),
        columns=["Auftragswert"])
    st.bar_chart(chart_data)

col4, col5, = st.columns(2)

col6, col7, = st.columns(2)
with col6:
    st.bar_chart(df["Auftragswert"])

with col7:
    st.bar_chart(df["Kalkulationswert"])



data = st.dataframe(df)