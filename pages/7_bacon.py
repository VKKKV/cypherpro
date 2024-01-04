import streamlit as st

# 培根密码字典
BACON_DICT = {
    'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
    'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
    'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
    'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
    'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
    'Z': 'BBAAB'
}
# 验证输入的字符串是否只包含'A'和'B'，并且其长度是5的倍数。
def is_valid_bacon_code(code):
    return all(c in 'AB' for c in code) and len(code) % 5 == 0

def encode_bacon(text):
    return ' '.join(BACON_DICT.get(char.upper(), '') for char in text if char.upper() in BACON_DICT)

def decode_bacon(code):
    if not is_valid_bacon_code(code):
        return "无效的培根密码编码"
    inv_bacon_dict = {v: k for k, v in BACON_DICT.items()}
    # st.write([inv_bacon_dict.get(char,'') for char in code])
    # st.write([inv_bacon_dict.get(char,'') for char in code])
    # st.write(inv_bacon_dict)

    res = ''
    for i in range(0, len(code), 5):
        c_str = ''.join(code[i:i+5])
        res+=''.join(inv_bacon_dict.get(c_str, ''))
        print(res)
    # 您的处理逻辑
    return res

def main():
    st.title("培根密码编解码器")

    operation = st.radio("选择操作", ("编码", "解码"))
    if operation == "编码":
        input_text = st.text_area("输入要编码的文本（只包含字母）")
        if st.button("编码"):
            result = encode_bacon(input_text)
            st.text_area("编码结果", result, height=100)
    else:
        input_code = st.text_area("输入要解码的培根密码（例如: AAAAAAAABA等）")
        if st.button("解码"):
            result = decode_bacon(input_code.replace(" ", ""))
            st.write('asd')
            st.text_area("解码结果", result, height=100)

if __name__ == "__main__":
    main()
