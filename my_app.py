import streamlit as st
import numpy as np
import pandas as pd
import time
st.title('My first app')

df = pd.read_csv('training_data.csv',sep=':',delimiter=None)
df
st.write("This is a  simple line chart for the training data")
st.line_chart(df)
st.vega_lite_chart(df)


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(1)

  