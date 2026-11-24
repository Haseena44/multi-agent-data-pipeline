import streamlit as st
from pipeline import MultiAgentPipeline

st.title("Multi-Agent Data Pipeline - Apple Retail")
st.write("3 AI Agents working together")

user_input = st.text_area("Enter Sales Data (one per line)", "iPhone Sales 100\nMac Sales 50\n iPad Sales 75")

if st.button("Run Agents"):
    data = user_input.split("\n")
    pipeline = MultiAgentPipeline()
    result = pipeline.run(data)
    st.success("Agents Completed!")
    st.code(result)
