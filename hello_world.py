import streamlit as st

st.write('**Secret:**',st.secrets['secret'])
st.write('**Password:**',st.secrets['section']['password'])
