import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐒')

# 图片对象数组
images = [
    {
        'url':'https://www.thehappycatsite.com/wp-content/uploads/2020/12/What-does-it-mean-if-a-cat-winks-at-you-HC-long.jpg',
        'parm':'猫'
    },
    {
         'url': 'https://www.birds.cornell.edu/home/wp-content/uploads/2018/10/program-bps.jpg',
         'parm':'鸟'
    },
    {
          'url':'https://housing.com/news/wp-content/uploads/2023/07/Cute-dog-breeds-that-make-the-best-pets-f-686x400.jpg',
          'parm':'狗'
    },
    {
          'url':'https://n.sinaimg.cn/sinakd20113/179/w1290h1289/20230326/79b7-3d2a1863258979bbb1dd6ba371ae1a0e.jpg',
          'parm':'猫meme'
     },
    {
          'url':'https://v-huya-img2.msstatic.com/process/1745313478458/1055760708/99.jpg?x-oss-process=image/resize,limit_0,m_lfit,h_460/sharpen,80/format,jpg/interlace,1/quality,q_80',
          'parm':'danking'
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

# st.image()总共两个参数，url：图片地址 caption:图片的备注
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])

#将一行分成两列
c1,c2 = st.columns(2)

with c1:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('上一张',on_click=lastImg,use_container_width=True)
    
with c2:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
    st.button('下一张',on_click=nextImg,use_container_width=True)

