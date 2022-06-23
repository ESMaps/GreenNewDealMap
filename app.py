import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)
