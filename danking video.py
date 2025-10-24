import streamlit as st

# 创建一个标题展示元素，内容是全中文的
# 如不定义anchor参数，则无锚点
st.title("📺︎简易danking播放器")

st.set_page_config(page_title='视频', page_icon='📺︎')

# 读取视频数据
video_url = [
    {
   'url':'https://upos-sz-estghw.bilivideo.com/upgcxcode/73/18/32384681873/32384681873-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&gen=playurlv3&deadline=1761303356&mid=0&uipk=5&oi=2672555743&os=estghw&og=hw&trid=cb7e064860274d17aaa41986b8a5073h&nbs=1&upsig=66171c5af2c1f5bf3313ae55a4ce8c9e&uparams=e,platform,gen,deadline,mid,uipk,oi,os,og,trid,nbs&bvc=vod&nettype=0&bw=329593&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
   'title':'danking',
   'number':'1'
   },
    {
   'url':'https://upos-sz-estgcos.bilivideo.com/upgcxcode/32/16/1503841632/1503841632-1-192.mp4?e=ig8euxZM2rNcNbNgnWdVhwdlhbNHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=cos&uipk=5&platform=html5&oi=1782024106&nbs=1&trid=efa9da65cdf04612871efecb2cec25eh&deadline=1761303280&mid=0&gen=playurlv3&os=estgcos&upsig=6f58a9ce873193a162dae190a4aeb997&uparams=e,og,uipk,platform,oi,nbs,trid,deadline,mid,gen,os&bvc=vod&nettype=0&bw=1843750&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
   'title':'乌兰巴托',
   'number':'2'
   },
    {
   'url':'https://upos-sz-estgcos.bilivideo.com/upgcxcode/19/77/28647557719/28647557719-1-192.mp4?e=ig8euxZM2rNcNbNVnWdVhwdlhbdHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=1782024106&os=estgcos&trid=9e12356f2f814775b1a288d92adbe0fh&nbs=1&uipk=5&platform=html5&mid=0&gen=playurlv3&og=cos&deadline=1761303429&upsig=cffe660fa75b1febe6cd6f713390befe&uparams=e,oi,os,trid,nbs,uipk,platform,mid,gen,og,deadline&bvc=vod&nettype=0&bw=1677456&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
   'title':'“我会装作不在乎 直到真正不在乎”',
   'number':'3'
           }
]

#将ind的值存储到streamlit的内存中，如果内存中没有ind，才要设置成0，否则不需要设置
if 'ind' not in st.session_state:
    st.session_state['ind']=0

st.title(video_url[st.session_state['ind']]['title']+'-第'+video_url[st.session_state['ind']]['number']+'集')
st.video(video_url[st.session_state['ind']]['url'])


#将一行分成三列
c1,c2,c3 = st.columns(3)

def play(arg):
         #点击哪个按钮，就播放第几集
         #将传递过来的值，赋值给内存中的ind
         st.session_state['ind']=int(arg)

for i in range(len(video_url)):
    st.button('第' + str(i+1) + '集',use_container_width=True,on_click=play,args=([i]))

