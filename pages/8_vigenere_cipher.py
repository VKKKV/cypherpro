import streamlit as st

def vigenere_cipher(text, key, mode='encrypt'):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    key = key.lower()
    key_length = len(key)
    key_as_int = [letters.index(c) for c in key]
    text = text.lower()
    result = ""

    for i, c in enumerate(text):
        if c in letters:
            key_c = key_as_int[i % key_length]
            if mode == 'encrypt':
                idx = (letters.index(c) + key_c) % 26
            elif mode == 'decrypt':
                idx = (letters.index(c) - key_c) % 26
            result += letters[idx]
        else:
            result += c

    return result

def main():
    st.title("维尼吉亚密码编解码器")

    operation = st.radio("选择操作", ("加密", "解密"))
    text = st.text_area("输入文本")
    key = st.text_input("输入密钥（仅限英文字母）")

    if text and key:
        if operation == "加密":
            result = vigenere_cipher(text, key, mode='encrypt')
            st.text_area("加密结果", result, height=100)
        else:
            result = vigenere_cipher(text, key, mode='decrypt')
            st.text_area("解密结果", result, height=100)

if __name__ == "__main__":
    main()
