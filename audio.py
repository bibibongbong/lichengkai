import streamlit as st

# 创建一个标题展示元素，内容是全中文的
# 如不定义anchor参数，则无锚点
st.title("🎧️简易音乐播放器")

# 第一个普通文本展示元素，无工具提示
st.text("使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

    # 数组
images = [
        {
            'url':'https://music.163.com/song/media/outer/url?id=2526625.mp3',
            'author':'歌手：Deep Side',
            'photo':'https://p1.music.126.net/dUSiZ5ASRpWgaq9OTMtoDw==/860917604602698.jpg?param=250y250',
            'name':'booty music'
        },
        {
            'url':'https://music.163.com/song/media/outer/url?id=1842728629.mp3',
            'author':'歌手：郑润泽',
            'photo':'https://p1.music.126.net/-xMsNLpquZTmMZlIztTgHg==/109951165953469081.jpg?param=250y250',
            'name':'如果呢'
        },
        {
            'url':'https://music.163.com/song/media/outer/url?id=18638059.mp3',
            'author':'歌手：Justin Bieber',
            'photo':'https://p1.music.126.net/w-KG9LFj7Z2F9bjtlHG3JA==/109951165476414199.jpg?param=250y250',
            'name':'One Time'
        }
]

#将ind的值存储到streamlit的内存中，如果内存中没有ind，才要设置成0，否则不需要设置
if 'ind' not in st.session_state:
    st.session_state['ind']=0


#define:定义
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1)%len(images)
def lastImg():
    st.session_state['ind']=(st.session_state['ind']-1)%len(images)


b1,b2=st.columns([1,2])
with b1:
# st.image()总共两个参数，url：图片地址 caption:图片的备注
   st.image(images[st.session_state['ind']]['photo'],caption=images[st.session_state['ind']]['name'])

with b2:
   st.title(images[st.session_state['ind']]['name'])
   st.header(images[st.session_state['ind']]['author'])
   
   #将一行分成两列
   c1,c2 = st.columns(2)

   with c1:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('上一首',on_click=lastImg,use_container_width=True)
    
   with c2:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('下一首',on_click=nextImg,use_container_width=True)

st.audio(images[st.session_state['ind']]['url'])


