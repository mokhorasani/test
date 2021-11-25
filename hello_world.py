import streamlit as st

st.title('Hello world')
st.write('From ***Streamlit Cloud***')

st.write(st.secrets['secret'])
st.write(st.secrets['section']['password'])
