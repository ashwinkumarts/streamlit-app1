import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Dataset Viewer", page_icon="📊")
st.title("📊 Dataset Viewer")
st.write(
    """
    This app visualizes data from the provided CSV file.
    """
)

# Load the data from a CSV. We're caching this so it doesn't reload every time the app reruns.
@st.cache_data
def load_data():
    df = pd.read_csv("test3.csv")
    return df

df = load_data()

# Show the dataframe.
st.dataframe(df, use_container_width=True)

# Display the data as an Altair chart.
chart = (
    alt.Chart(df)
    .mark_line()
    .encode(
        x=alt.X("Date:T", title="Date"),
        y=alt.Y("V/D:Q", title="V/D"),
        color="Report:N",
    )
    .properties(height=320)
)
st.altair_chart(chart, use_container_width=True)
