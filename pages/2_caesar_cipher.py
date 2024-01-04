import streamlit as st

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + shift_amount if mode == 'encrypt' else ord(char) - shift_amount

            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26

            result += chr(char_code)
        else:
            result += char
    return result


st.title("凯撒密码加密与解密")

operation = st.radio("选择操作", ('加密', '解密'))
text = st.text_area("输入文本")
shift = st.number_input("输入位移量", min_value=1, max_value=25, value=3, step=1)

if st.button("执行"):
    if operation == '加密':
        st.success("加密结果: ")
        st.code(caesar_cipher(text, shift, mode='encrypt'))
    else:
        st.success("解密结果: ")
        st.code(caesar_cipher(text, shift, mode='encrypt'))

