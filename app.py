import streamlit as st

st.set_page_config(
    page_title="TraceMap",
    layout="wide",
)

st.title("TraceMap")
st.caption("Visual execution tracing for Python")

st.markdown(
    """
    Upload Python code and explore:
    - execution timeline
    - call hierarchy
    - runtime costs
    - variable mutations
    """
)
