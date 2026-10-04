import streamlit as st
import os
import json
from datetime import datetime
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
#创建会话标识的函数
def create_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#保存回话函数
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }

        # 如果sessions文件夹不存在则创建他
        if not os.path.exists("sessions"):
            os.makedirs("sessions")

        # 保存会话数据
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)

#加载所有的会话列表信息
def load_sessions():
    sessions_list = []
    #加载sessions文件夹下的所有json文件
    if os.path.exists("sessions"):
        for file in os.listdir("sessions"):
            if file.endswith(".json"):
                sessions_list.append(file[:-5])

    return sessions_list

#加载指定会话信息
def load_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            #读取会话数据
            with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_id
                st.session_state.messages = session_data["messages"]
    except Exception as e:
        st.error(f"加载会话出错:{e}")

#删除指定会话功能
def delete_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            os.remove(f"sessions/{session_id}.json")
            #如果删除的是当前会话则需要更新消息列表
            if session_id == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = create_session_id()
    except Exception as e:
        st.error(f"删除会话出错:{e}")


#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

 #伴侣昵称
if "nick_name" not in st.session_state:
        st.session_state.nick_name = "小甜甜"

#伴侣性格
if "nature" not in st.session_state:
        st.session_state.nature = "活泼开朗的南方姑娘"

#会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = create_session_id()

#是否有新消息(用于判断新建会话时是否需要保存)
if "has_new_message" not in st.session_state:
    st.session_state.has_new_message = False

#大标题
st.title("AI伴侣")
#logo
st.logo("❤️")
#系统提示词
system_prompt = f"""
你叫{st.session_state.nick_name},现在是用户的真实伴侣,请完全代入伴侣的角色.
规则:
    1.每次只回复1条消息
    2.禁止任何场景或状态描述性文字
    3.匹配用户的语言
    4.回复简短,像聊天一样
    5.有需要的话可以用❤️等emoji文字
    6.用符合伴侣性格的方式对话
    7.回复的内容,要充分体现伴侣的性格特征
伴侣性格:
    - {st.session_state.nature}
你必须严格遵守以上规则,并用符合伴侣性格的方式对话.
"""

#侧边栏 --- with:streamlit中上下文管理器
with st.sidebar:
    #AI控制面板
    st.subheader("AI控制面板")

    #新建会话
    if st.button("新建会话",width="stretch",icon="🔖"):
        # #1.保存当前会话信息
        if st.session_state.has_new_message:
            save_session()
            st.session_state.has_new_message = False

        # 2.重置为新的空会话
        st.session_state.messages = []
        st.session_state.current_session = create_session_id()
        st.rerun()

    #历史会话
    st.text("历史会话")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:
            #加载会话信息
            #三元运算符:如果条件为真,则返回第一个表达式的值,否则返回第二个表达式的值 --> 语法: 值1 if 条件 else 值2
            if st.button(session,width="stretch", key=f"load_{session}",icon="📄",type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()

        with col2:
            #删除会话信息
            if st.button("", width="stretch",key=f"delete_{session}",icon="❌️"):
                delete_session(session)
                st.rerun()

    #分隔线
    st.divider()
    #伴侣信息
    st.subheader("伴侣信息")
    #昵称输入框
    nick_name = st.text_input("昵称", placeholder="请输入伴侣昵称",value = st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
    nature = st.text_area("性格", placeholder="请输入伴侣性格",value = st.session_state.nature)
    if nature:
        st.session_state.nature = nature

#展示聊天信息
st.text(f"会话名称:{st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

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

    # print([
    #     {"role": "system", "content": system_prompt},
    #     *st.session_state.messages
    # ])
    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果(非流式输出的解析方式 )
    # print("<---------------------大模型返回结果",response.choices[0].message.content)
    # st.chat_message("assistant").write(f"AI:{response.choices[0].message.content}")

    # 流式输出大模型返回结果(流式输出的解析方式)
    response_message = st.empty()  # 创建一个空的元素来显示大模型的返回结果

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    #保存AI大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content":full_response})

    # 标记有新消息,并保存会话
    st.session_state.has_new_message = True
    save_session()


