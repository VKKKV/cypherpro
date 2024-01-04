import streamlit as st

st.title('st.secrets')
# 配置文件
st.write(st.secrets['message'])