import streamlit as st
from PIL import Image
import io

def image_to_hex(image):
    # 转换图片为Hex
    with io.BytesIO() as output:
        image.save(output, format="PNG")
        hex_data = output.getvalue().hex()
    return hex_data

def main():
    st.title("图片转换工具")

    st.subheader("to hex")
    # 文件上传
    uploaded_file = st.file_uploader("上传图片", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # 读取图片
        image = Image.open(uploaded_file)
        
        col1=st.columns(2)
        with col1: 
            # 显示图片
            st.image(image, caption='上传的图片', use_column_width=True)

        # 转换并显示Hex
        hex_data = image_to_hex(image)
        st.text_area("图片的Hex值", hex_data, height=250)

if __name__ == "__main__":
    main()

