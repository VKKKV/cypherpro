import streamlit as st

def fence_cipher(text, rails, mode='encrypt'):
    if rails == 1 or len(text) <= 1:
        return 0,text

    if mode == 'encrypt':
        try:
            n = int(rails)
            res = ''
            for i in range(n):
                for j in range(int(len(text) / n + 0.5)):
                    try:
                        res += text[j * n + i]
                    except:
                        pass
            if res != '':
                return 1, res
            else:
                return 0,'加密失败!'
        except Exception as e:
            return 0, '请输入正确的分组!' + str(e)

    else:  # decrypt
        try:
            # 确定每个栏中的字符数量
            rail_lens = [len(text) // rails + (1 if i < len(text) % rails else 0) for i in range(rails)]
            # 将加密文本分割到各个栏中
            rails_text = []
            start = 0
            for r_len in rail_lens:
                rails_text.append(text[start:start + r_len])
                start += r_len

            # 逐字符解密
            result = []
            idx = 0
            for _ in text:
                row = idx % rails
                result.append(rails_text[row][0])
                rails_text[row] = rails_text[row][1:]
                idx += 1

            return 1,''.join(result)
        except Exception as e:
            return 0,'解密失败' + str(e)


def guess_rails_for_decryption(text):
    try:
        result_text = ''
        for rails in range(1, len(text)):
            status,decrypted_text = fence_cipher(text, rails, mode='decrypt')
            if status: 
                # 这里可以添加一些逻辑来判断解码是否有效
                result_text += "分为%s栏，解密结果为:%s\n" % (rails, decrypted_text)
        return rails, result_text
    except Exception as e:
        return None, '解密失败' + str(e)



def is_valid_decryption(text):
    # 这里可以添加一些逻辑来判断解码是否有效
    # 例如，检查解码结果是否包含可打印字符
    return all(char.isprintable() for char in text)

################################################################

st.title("栅栏密码")
operation = st.radio("选择操作", ('加密','解密'))
specify_rails = st.checkbox("指定栏杆数", value=True)
text = st.text_area("输入文本")
rails = st.number_input("栏杆数", min_value=1, value=2, step=1,disabled=not specify_rails)
st.write(operation)


if st.button("执行"):

        if operation == '加密':
            st.success("加密结果: ")
            status,result = fence_cipher(text, rails, mode='encrypt')
            if status : st.code(result) 
            else : st.error(result)
        else :
            if specify_rails:
                status,result = fence_cipher(text, rails, mode='decrypt')
                st.success("解密结果: ")
                if status : st.code(result) 
                else : st.error(result)
            else:
                guessed_rails, result = guess_rails_for_decryption(text)
                if guessed_rails:
                    st.write(guessed_rails)
                    st.code(result)
                else:
                    st.write(guessed_rails)
                    st.error(result)
            
