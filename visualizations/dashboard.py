import streamlit as st

def launch_dashboard(df):
    st.title("Crypto Visualizer Dashboard")
    st.line_chart(df.set_index('timestamp')['price'])
    st.write(df.tail())
