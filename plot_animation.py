import pandas as pd
import altair as alt
import streamlit as st
import time

df = pd.read_csv('updatedreport.csv')
chart = st.empty()


for i in df.index:
    data_to_be_added = df.iloc[0: i + 1, :]

    scatters = alt.Chart(df).mark_circle(size=80).encode(
        x=alt.X('year:O', axis=alt.Axis(title='Year')),
        y=alt.Y('Happiness Score', axis=alt.Axis(title='Happiness Score')),
        color='Region',
        tooltip=['Country', 'year', 'Region', 'Happiness Score']
    ).properties(
        width=600,
        height=300
    )
    time.sleep(0.2)

    chart.altair_chart(scatters)
