import streamlit as st

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
                   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
                   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
                   'Y': '-.--', 'Z': '--..',

                   '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

                   ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
                   '(': '-.--.', ')': '-.--.-'}

def encode_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(i.upper(), '') for i in text)

def decode_morse(morse_code):
    morse_code_dict_inv = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(morse_code_dict_inv.get(i, '') for i in morse_code.split())

def main():
    st.title("摩斯密码编解码器")

    operation = st.radio("选择操作", ("编码", "解码"))
    input_text = st.text_input("输入文本")

    if operation == "编码":
        if st.button("编码"):
            result = encode_morse(input_text)
            st.text_area("编码结果", result, height=100)
    else:
        if st.button("解码"):
            result = decode_morse(input_text)
            st.text_area("解码结果", result, height=100)

if __name__ == "__main__":
    main()
