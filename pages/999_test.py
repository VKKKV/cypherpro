import streamlit as st

def method(n,a,b,c):
    # 汉诺塔
    if(n == 1):
        st.write(a,"->",c)
        return 
    method(n-1, a, c, b)
    method(1, a, b, c)
    method(n-1, b, a, c)



st.title("test")
# operation = st.radio("选择操作", ('r1', 'r2'))
text = st.text_area("输入文本")
# shift = st.number_input("输入位移量", min_value=1, max_value=25, value=3, step=1)

method(int(text), "a", "b", "c")


# if st.button("b1"):
    # if operation == 'r1':
        # st.success("s1: ")
    # else:
    #     st.success("s2: ")
    #     st.code(method(text))
