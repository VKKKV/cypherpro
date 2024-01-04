import streamlit as st

def method(operation,text):
    pass





st.title("test")

operation = st.radio("选择操作", ('加密', '解密'))
text = st.text_area("输入文本")
# shift = st.number_input("输入位移量", min_value=1, max_value=25, value=3, step=1)


if st.button("执行"):
    if operation == '加密':
        st.success("加密结果: ")
        st.code(method(operation,text))
    else:
        st.success("解密结果: ")
        st.code(method(operation,text))