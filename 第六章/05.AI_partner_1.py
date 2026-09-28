import streamlit as st
import os
from openai import OpenAI

#设置页面的配置项
st.set_page_config(
    page_title="AI伙伴",
    page_icon="🤖",
    #布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state = "expanded",
    menu_items = {}
)

#大标题
st.title("AI伙伴")
#logo
st.logo("❤️")
#系统提示词
system_prompt = "You are a helpful assistant."

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(f"用户:{message['content']}")
    # else:
    #     st.chat_message("assistant").write(f"AI:{message['content']}")


#创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#聊天输入框
prompt = st.chat_input("请输入你的问题")
if prompt:
    st.chat_message("user").write(f"用户:{prompt}")
    print("----------------->调用AI大模型,提示词",prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("<---------------------大模型返回结果",response.choices[0].message.content)
    st.chat_message("assistant").write(f"AI:{response.choices[0].message.content}")
    #保存AI大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})



