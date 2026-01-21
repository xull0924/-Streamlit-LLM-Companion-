import streamlit as st

#设置页面配置项
st.set_page_config(
    page_title="许诺女士的网站",
    page_icon="🧊",
    #布局
    layout="wide",
    #控制侧边栏
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'Report a bug': "https://docs.streamlit.io/",
        'About': "# 这是一个Streamlit入门程序!"
    }
)

#大标题
st.title("Streamlit Test")
st.header("一级标题")
st.subheader("二级标题")

#大段文字
st.write("布偶猫是原产于美国的大型半长毛宠物猫品种。其体型大而长，公猫体重 6.8-9.0 千克，母猫体重 4.5-6.8 千克，体长含尾部可达 1 米。被毛蓬松，绒毛较少，不易打结，有海豹色、蓝色等六种毛色。眼睛大而圆，为蓝色，十分迷人。"
         )
st.write("布偶猫性情温和悠闲，顽皮却不过分活跃，环境适应力强，能与人类及其他动物友好相处，还较为容易被训练，是理想的室内伴侣。因其抱起来像布偶一样柔软，故而得名。"
         "")

#图片
st.image("./resources/照片.jpg")

#音频
st.audio("./resources/news.mp3")

#视频
st.video("./resources/news.mp4")

#logo
st.logo("./resources/logo.png")

#表格
student_data = {
    "name":["lhy","xxa"],
    "age":[20,20],
    "gender":["male","female"],
}
st.table(student_data)

#输入框
title = st.text_input("请输入姓名", "xxa")
st.write("姓名为：", title)

password = st.text_input("请输入密码", type="password")
st.write("密码为为：", password)

#单选按钮
gender = st.radio("请输入你的性别",["男","女","保密"],index=2)
st.write("你的性别为",gender)






