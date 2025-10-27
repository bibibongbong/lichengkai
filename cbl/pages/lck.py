import streamlit as st   # 导入Streamlit并用st代表它
# 这里为了演示创建了多个标题展示元素

# 创建一个标题展示元素
st.title("👨‍💻学生 李诚凯-数字档案")

# 创建一个章节，该章节为基础信息
st.header("🗝️基础信息")
# 创建一个文本，介绍一下基础信息
st.markdown('###### 学生ID：23031310138')
st.markdown('###### 注册时间：:green[2025年10月20日11:19:34]|精神状态：✅正常')
st.markdown('###### 当前教室：:green[实训楼204]|安全等级：:green[绝密]')

# 创建一个标题展示元素
st.header("📊技能矩阵")

# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="C语言", value="95%", delta="2%")
c2.metric(label="Python", value="90%", delta="-5%")
c3.metric(label="Java", value="70%", delta="0", delta_color="off")

st.markdown('#### streamlit课程进度')
st.text('streamlit课程进度')


# 创建一个标题展示元素
st.header("📔任务日志")

import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

# 定义数据,以便创建数据框
data = {
    '日期':['2023-10-11','2023-10-16','2025-10-21'],
    '任务':['学生数字档案','课程管理系统','数据图表展示'],
    '状态':['✅完成','⏲进行中','❌︎未完成'],
    '难度':['⭐⭐','⭐','⭐⭐⭐'],
}
# 定义数据框所用的索引
index = pd.Series(['0', '1', '2'], name=' ')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.subheader('默认显示')
st.dataframe(df)

# 创建一个标题展示元素
st.header("💻最新代码成果")

st.subheader('Python代码块')
# 创建要显示的Python代码块的内容
python_code = '''def hello():
    print("你好，Streamlit！")
'''
# 创建一个代码块，用于展示python_code的内容
# language为默认，即该代码块以Python语法高亮
st.code(python_code)

# 分割线
st.markdown('***')

# 动态信息流

st.write("---")

st.write("`>> SYSTEM MESSAGE:` 下一个任务目标已解锁...")

st.write("`>> TARGET:` 课程管理系统")

st.write("`>> COUNTDOWN:`", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))



# 终端效果

st.markdown("""

系统状态: 在线

连接状态: 已加密

""")
