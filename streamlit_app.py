import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config("AirScanAI Dashboard", layout="wide")

st.title("AirScanAI: Threat Detection Dashboard")
data = data = pd.read_csv("/Users/shrutiraj/Desktop/AirScanAI/data/radar_mock.csv")
st.line_chart(data[['time', 'signal_strength']].set_index('time'))
st.map(data.rename(columns={'lat': 'latitude', 'lon': 'longitude'}))