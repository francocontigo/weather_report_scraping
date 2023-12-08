import pandas as pd
import os
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Weather Dashboard",
                   page_icon=":umbrella:",
                   layout="wide")

@st.cache_data
def get_data():
    path = os.curdir
    data_path = os.path.join(path, 'data')

    data_file_path = os.path.join(data_path, 'weather_report_data.csv')
    df = pd.read_csv(data_file_path)
    return df

df = get_data()

#SIDEBAR
st.sidebar.header("Filter Here:")
# desc_day
desc_day = st.sidebar.multiselect(
    "Select the description of the day:",
    options=df["desc_day"].unique(),
    default=df["desc_day"].unique()
)
# desc_current
desc_current = st.sidebar.multiselect(
    "Select the description of the scheduled time:",
    options=df["desc_current"].unique(),
    default=df["desc_current"].unique()
)

df_selection = df.query(
    "desc_day == @desc_day & desc_current == @desc_current"
)

#MAINPAGE
st.title(":umbrella: Weather Dashboard")
st.markdown("##")

# KPI's
max_temp = int(df_selection["temp_max"].max())
min_temp = int(df_selection["temp_min"].min())
avg_temp_series = df_selection[["temp_max", "temp_min"]].mean()
avg_temp = int(avg_temp_series["temp_max"])
avg_temp_current = int(df_selection["temp_current"].mean())

first_column, second_column, third_column, fourth_column = st.columns(4)
with first_column:
    st.subheader("Max Temperature: ")
    st.subheader(f"°C {max_temp}")
    
with second_column:
    st.subheader("Min Temperature: ")
    st.subheader(f"°C {min_temp}")
    
with third_column:
    st.subheader("Avg Day Temperature: ")
    st.subheader(f"°C {avg_temp}")
    
with fourth_column:
    st.subheader("Avg Temperature in Scheduled Time: ")
    st.subheader(f"°C {avg_temp_current}")
    
st.markdown("---")

st.subheader(":clipboard: DataFrame Head !")
st.dataframe(df_selection.head())

st.markdown("---")

st.subheader(":bar_chart: Graphs!")
#GRAPHS
fig_temp_current_over_time = px.line(df_selection, x="date_time", y="temp_current", title="Change in Current Temperature Over Time",
              labels={"temp_current": "Current Temp (°C)"}, line_shape="linear",
              line_dash_sequence=["solid"], color_discrete_sequence=[px.colors.qualitative.Plotly[0]])
fig_temp_current_over_time.update_layout(
    xaxis_title="Date and Time", 
    yaxis_title="Current Temp (°C)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_temp_max_over_time = px.line(df_selection, x="date_time", y="temp_max", title="Change in Maximum Temperature Over Time",
              labels={"temp_max": "Max Temp (°C)"}, line_shape="linear",
              line_dash_sequence=["solid"], color_discrete_sequence=[px.colors.qualitative.Plotly[1]])
fig_temp_max_over_time.update_layout(
    xaxis_title="Date and Time", 
    yaxis_title="Max Temp (°C)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_temp_min_over_time = px.line(df_selection, x="date_time", y="temp_min", title="Change in Minimum Temperature Over Time",
              labels={"temp_min": "Min Temp (°C)"}, line_shape="linear",
              line_dash_sequence=["solid"], color_discrete_sequence=[px.colors.qualitative.Plotly[2]])
fig_temp_min_over_time.update_layout(
    xaxis_title="Date and Time",
    yaxis_title="Min Temp (°C)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_unique_desc_day = px.pie(df, names="desc_day", title="Unique Values of 'desc_day'", color_discrete_sequence=px.colors.qualitative.Set3)
fig_unique_desc_day.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column1, right_column1 = st.columns(2)
left_column1.plotly_chart(fig_temp_current_over_time, use_container_width=True)
right_column1.plotly_chart(fig_unique_desc_day, use_container_width=True)

left_column2, right_column2 = st.columns(2)
left_column2.plotly_chart(fig_temp_max_over_time, use_container_width=True)
right_column2.plotly_chart(fig_temp_min_over_time, use_container_width=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)