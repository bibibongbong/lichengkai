import streamlit as st
from datetime import datetime, timedelta
from datetime import datetime, time

st.set_page_config(page_title="个人简历生成器", page_icon="", layout="wide")
st.header("个人信息表单")
st.text('使用stream创建您的个性化简历')

c1,c2 =st.columns([1,2])
with c1:
    st.subheader("个人信息表单")
    st.markdown('***')


    name = st.text_input('姓名', autocomplete='name')

    position = st.text_input('职位', autocomplete='position')

    phone = st.text_input('电话', autocomplete='phone')

    postbox = st.text_input('邮箱', autocomplete='postbox')


# value参数默认为None，初始状态为今天
    date = st.date_input("出生日期", value=None)

    st.write('性别')
# 设置标签为“hidden”
# 设置水平排列
    gender = st.radio(
    '你的性别是什么？',
    ['男', '女', '其他'],
    horizontal=True,
    label_visibility='hidden'
)
    st.write('学历')
    education = st.selectbox(
    '选择学历',
    ['小学', '初中','中专','高中','大专','本科','研究生','博士'],
    label_visibility='collapsed'
)
    st.write('语言能力')
    # 自定义format_func函数
    def my_format_func(option):
        return f'{option}'
    options = st.multiselect(
        '语言能力',
        ['英语', '法语','德语','日语','西班牙语','意大利语','其他'],
        format_func=my_format_func,
        label_visibility='hidden'
        )

    # 自定义format_func函数
    def my_format_func(option):
        return f'{option}'
    st.write('技能（可多选）')
    options_2 = st.multiselect(
        '选择你的技能',
        ['圈米', 'AWP的使用'],
         format_func=my_format_func,
        label_visibility='hidden'
        )

    age = st.slider('工作经验（年）', 0, 30, 3)

    values = st.slider(
        '选择一组范围',
        3000, 50000, (10000, 20000))

    gr = st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...',
                      height=200, max_chars=200)

    w2 = st.time_input("每日最佳联系时间段", time(8, 45))

    photo = st.file_uploader('上传你的照片')
    if photo is not None:
        bytes_data=photo.getvalue()

with c2:
    st.subheader('简历实时预览')
    st.markdown('***')
    b1,b2 =st.columns(2)
    with b1:
        st.image(bytes_data)
        st.write('姓名:',name)
        st.write('职位:',position)
        st.write('电话:',phone)
        st.write('邮箱:',postbox)
        st.write('出生日期:',date)
    with b2:
        st.write('性别:',gender)
        st.write('学历:',education)
        st.write('期望薪资:',values)
        st.write('工作经验:',age)
        st.write('最佳联系时间:',w2 )
        st.write('语言能力:',options)
    st.markdown('***')
    st.write('个人简介',gr)
    st.write('专业技能',options_2)


    
