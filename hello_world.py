import streamlit as st

st.title('Hello world')
st.write('From ***Streamlit Cloud***')

st.write('**Secret:**',st.secrets['secret'])
st.write('**Password**',st.secrets['section']['password'])
