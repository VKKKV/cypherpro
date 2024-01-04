import streamlit as st
import base64

def encode_to_base64(input_text):
    return base64.b64encode(input_text.encode()).decode()

def decode_from_base64(input_text):
    return base64.b64decode(input_text).decode()

st.title('Base64 编解码工具')

# 用户输入
user_input = st.text_input("输入你的文本", "")

# 编码和解码按钮
if st.button('编码'):
    st.text("编码结果:")
    st.code(encode_to_base64(user_input))

if st.button('解码'):
    try:
        st.text("解码结果:")
        st.code(decode_from_base64(user_input))
    except Exception as e:
        st.error("解码错误: " + str(e))

