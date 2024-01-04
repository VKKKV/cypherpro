import streamlit as st

st.title("我的网页导航")

st.header("欢迎使用网页导航模板")
st.write("这是一个简单的网页导航模板，帮助你快速访问常用网站。")

st.subheader("搜索引擎")
st.markdown("[Google](https://www.google.com)", unsafe_allow_html=True)
st.markdown("[Bing](https://www.bing.com)", unsafe_allow_html=True)
st.markdown("[Baidu](https://www.baidu.com)", unsafe_allow_html=True)

st.subheader("社交媒体")
st.markdown("[Facebook](https://www.facebook.com)", unsafe_allow_html=True)
st.markdown("[Twitter](https://www.twitter.com)", unsafe_allow_html=True)
st.markdown("[Instagram](https://www.instagram.com)", unsafe_allow_html=True)

st.subheader("教育资源")
st.markdown("[Coursera](https://www.coursera.org)", unsafe_allow_html=True)
st.markdown("[Khan Academy](https://www.khanacademy.org)", unsafe_allow_html=True)
st.markdown("[edX](https://www.edx.org)", unsafe_allow_html=True)

st.subheader("新闻网站")
st.markdown("[CNN](https://www.cnn.com)", unsafe_allow_html=True)
st.markdown("[BBC News](https://www.bbc.com/news)", unsafe_allow_html=True)
st.markdown("[The New York Times](https://www.nytimes.com)", unsafe_allow_html=True)
