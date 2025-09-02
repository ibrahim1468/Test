import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit 🚀")
st.write("This is a test deployment from Python 3.12.7 ✅")

# Add some sample data
df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)

st.line_chart(df)
