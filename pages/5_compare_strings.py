import streamlit as st
from difflib import SequenceMatcher

def compare_strings(str1, str2):
    ratio = SequenceMatcher(None, str1, str2).ratio()
    return ratio

st.title("字符串对比工具")

st.header("输入两个字符串进行对比")
str1 = st.text_area("输入字符串 1", height=100)
str2 = st.text_area("输入字符串 2", height=100)

if st.button("对比"):
    similarity = compare_strings(str1, str2)
    st.success(f"字符串相似度: {similarity:.2%}")

    if similarity == 1:
        st.info("两个字符串完全相同。")
    elif similarity == 0:
        st.error("两个字符串完全不同。")
    else:
        st.warning("两个字符串部分相似。")

