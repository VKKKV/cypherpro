import streamlit as st
import module.func_encode as encode
import module.func_decode as decode

st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)
st.header('cypher', divider='rainbow')
st.caption('Hello, *World!* :sunglasses:')

# 分列
col1, col2, col3 = st.columns(3)
with col1:

     base_type = ["base16", "base32", "base64", "base85_ASCII85", "base85_RFC1924"]
     # 函数：Base编码
     def base_encode(encoding, text):
          try:
               return encode.en_base(encoding, text).decode('utf-8')
          except Exception as e:
               return f'编码错误: {e}'

     # 函数：Base解码
     def base_decode(decoding, text):
          try:
               return decode.de_base(decoding, text).decode('utf-8')
          except Exception as e:
               return f'解码错误: {e}'

     st.subheader("Base")
     base_select = st.selectbox("选择编码类型", base_type, key="base_select")
     base_str = st.text_input('输入字符串', "test", key="base_input")

     col1_1, col1_2=st.columns(2)

     with col1_1:
          if st.button('开始编码', key="base_button"):
               base_res = base_encode(base_select, base_str)
               st.code(base_res)
     with col1_2:
          if st.button('开始解码', key="base_decode_button"):
               base_res = base_decode(base_select, base_str)
               st.code(base_res)



with col2:

     st.subheader("ASCII")
     # 选择进制
     encoding_options = ["二进制", "八进制", "十进制", "十六进制"]
     ASCII_type = st.selectbox("选择进制类型", encoding_options)
     # 用户输入
     ASCII_input = st.text_input("输入字符串",  key="ASCII_input")
     col2_1, col2_2=st.columns(2)
     with col2_1:
          # 转换并显示结果
          if st.button("开始编码", key="ASCII_button"):
               try:
                    result=encode.en_ASCII(ASCII_type, ASCII_input)
                    st.code(result)
               except Exception as e:
                    st.error(f"转换错误: {e}")
     with col2_2:
          if st.button("开始解码",key="ASCII_decode_button"):
               try:
                    result = decode.de_ASCII(ASCII_type, ASCII_input)
                    st.code(result)
               except Exception as e:
                    st.error(f"解码错误: {e}")


with col3:
     st.subheader("Unicode")
     # 用户输入
     Unicode_input = st.text_input("输入字符串", key="Unicode_input")
     col3_1, col3_2=st.columns(2)

     with col3_1:
          # 转换并显示结果
          if st.button("开始编码", key="Unicode_button"):
               try:
                    result=encode.en_unicode(Unicode_input).decode("utf-8")
                    st.code(result)
               except Exception as e:
                    st.error(f"转换错误: {e}")
     with col3_2:
          if st.button("开始解码",key="Unicode_decode_button"):
               try:
                    result = decode.de_unicode(Unicode_input)
                    st.code(result)
               except Exception as e:
                    st.error(f"解码错误: {e}")
