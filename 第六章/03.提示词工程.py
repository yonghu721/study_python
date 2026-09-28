#提示词L是引导大模型进行内容生成的命令
#提示词工程:通过有技巧的编写提示词,使大模型生成出尽可能符合预期的内容,这一持续性的过程就成为提示词工程.
"""
    1.给大模型设定角色和能力
    2.明确核心请求与任务
    3.按步骤拆解复杂任务
    4.指定风格与语气
    5.明确要求输出格式
    6.提供输入输出的示例
    主要内容为:
    1.定角色:给大模型设定角色与能力
    2.给任务:明确核心请求与任务按步骤拆解复杂任务
    3.提要求:指定风格与语气明确要求输出格式
"""
#---------------------------------streamlit--------------------------------------------------------------
"""
1.什么是streamlit?
    streamlit是一个用于快速基于python代码构建web网页的python库(数据科学及机器学习领域)
2.streamlit的使用步骤?
    1. 安装streamlit:pip install streamlit
    2. 在python文件中引入streamlit模块
    3. 基于streamlit中提供的API来构建Web应用
    4. 运行程序: streamlit run xxxx.py
"""

#大标题
import streamlit as st
st.title("入门演示")
st.header("一级标题")
st.subheader("二级标题")

#段落文字
st.write("文字演示")
st.write("你好,文字演示2")

#图片
st.image("./resources/下载.jpg",width = 600)

#音频
# st.audio("resources/news.mp3")

#视频
# st.video("resources/news.mp4")

#Logo
st.logo("resources/下载.jpg")

#表格
studen_data = {
    "姓名":["王林","张三","李四","王五","赵六"],
    "学号":["20260001","20260002","20260003","20260004","20260005"],
    "语文":[98,90,59,29,80],
    "数学":[88,78,68,79,28],
    "英语":[88,98,54,78,65]
}
st.table(studen_data)

#输入框
#普通输入框
name = st.text_input("请输入您的姓名:")
st.write("您的姓名为:",name)

#密码输入框
password = st.text_input("请输入您的密码",type="password")
st.write("您输入的密码为:",password)

#单选按钮
gender = st.radio("请输入您的性别:",["男","女","未知"],index = 2)
st.write("您的性别为:",gender)