import streamlit as st

st.set_page_config(page_title='视频', page_icon='📺︎')

# 读取视频数据
video_file = 'trailer.mp4'

# 显示视频
st.subheader("展示视频")
st.video(video_file)
