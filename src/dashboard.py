import pandas as pd
import os
import plotly.express as px
import streamlit as st

# st.set_page_config(page_title="Weather Dashboard",
#                    page_icon=":umbrella:",
#                    layout="wide")

path = os.curdir
data_path = os.path.join(path, 'data')

data_file_path = os.path.join(data_path, 'weather_report_data.csv')
df = pd.read_csv(data_file_path)

# st.dataframe(df)

print("Colunas do DataFrame:", df.columns)


#SIDEBAR

# st.sidebar.header("Filter Here:")
# desc_day = st.sidebar.multiselect(
#     "Select the description of the day:",
#     options=df["desc_day"].unique(),
#     default=df["desc_day"].unique()
# )
