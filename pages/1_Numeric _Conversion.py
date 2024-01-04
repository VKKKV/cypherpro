import streamlit as st
from module.func_binary import Class_Binary

binary= Class_Binary()

st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

st.header('进制转换', divider='rainbow')

num = ['2','8','10','16']

# 输入原始数据和其进制
original_data = st.text_input("输入原始数据", "1010")
original_base = st.selectbox("输入原始数据的进制",num)
# 输入目标进制
target_base = st.selectbox("输入目标进制", num,2)

# 转换按钮
if st.button("转换"):
    
    status,res,process=binary.exec_Binary(original_data,original_base,target_base)
    if status:
        st.code(f"process: {process}")
        st.code(res)
    else:
        st.error(f"转换错误: {res}")


        