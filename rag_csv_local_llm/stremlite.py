import streamlit as st
from ollama_csv_app import query_agent

st.title(" 🔥 Lets do Some analysis on CSV 🔥 ")
st.header(" ✨ Please upload your csv file here: ✨")

#capture the csv file
data = st.file_uploader("Upload CSV file",type="csv")
query = st.text_area("Enter your query ?")
button = st.button("Generate Response")

if button:
    #Get response
    answer = query_agent(data,query)
    st.write(answer)