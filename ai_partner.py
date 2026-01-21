import streamlit as st
import os
import json
from openai import OpenAI
from datetime import datetime

#设置页面配置项
st.set_page_config(
    page_title="智能伴侣",
    page_icon="💌",
    #布局
    layout="wide",
    #控制侧边栏
    initial_sidebar_state="expanded",
    menu_items={}
)
#生成会话标识函数
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 保存会话信息函数
def save_session():
    if st.session_state.current_session:
        session_data = {
            "ll_name": st.session_state.ll_name,
            "ll_character": st.session_state.ll_character,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        if os.path.exists("sessions") == False:
            os.mkdir("sessions")
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

#加载所有会话列表信息
def load_sessions():
    session_list = []
    # 加载sessions目录下的文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for file_name in file_list:
            if file_name.endswith(".json"):
                session_list.append(file_name[:-5])
    session_list.sort(reverse=True)
    return session_list

#加载指定会话信息
def load_session(session_name):
    try:
        if os.path.exists("sessions/%s.json" % session_name):
            with open("sessions/%s.json" % session_name, "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.current_session = session_name
                st.session_state.ll_name = session_data["ll_name"]
                st.session_state.ll_character = session_data["ll_character"]
    except Exception as e:
        print( e)
        st.error("加载会话失败：%s" % e)

# 删除会话信息函数
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")  # 删除文件
            # 如果删除的是当前会话, 则需要更新消息列表
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
    except Exception:
        st.error("删除会话失败!")

#大标题
st.title("智能伴侣")

#添加logo
st.logo("./resources/logo.jpg")

#系统提示词
system_prompt = """
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
    """

#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
#昵称
if 'll_name' not in st.session_state:
    st.session_state.ll_name = "小爱"
#性格
if 'll_character' not in st.session_state:
    st.session_state.ll_character = "古灵精怪傲娇的姑娘"
#会话标识
if 'current_session' not in st.session_state:
    st.session_state.current_session = generate_session_name()

#展示聊天信息
st.text(f"会话名称: {st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])

#创建OpenAI客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")


#左侧侧边栏
with st.sidebar:
    st.subheader("AI控制面板")

    if st.button("开始新的会话",width="stretch",icon="👋"):
        #保存当前会话数据
        save_session()
        #创建新的会话并保存
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()

    #会话历史
    st.text("会话历史")
    sessions_list = load_sessions()
    for session in sessions_list:
        col1, col2 = st.columns([4,1])
        with col1:
            if st.button(session, width="stretch", icon="📄", key=f"load_{session}",
                         type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("",width="stretch",icon="❌️",key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    # 分割线
    st.divider()

    st.subheader("伴侣信息")

    ll_name = st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.ll_name)
    if ll_name:
        st.session_state.ll_name = ll_name

    ll_character = st.text_area("性格",placeholder="请输入性格",value=st.session_state.ll_character)
    if ll_character:
        st.session_state.ll_character = ll_character


#输入框
prompt = st.chat_input("请输入你的问题")
if prompt:
    st.chat_message("user").write(prompt)
    #保存用户输入
    st.session_state.messages.append({"role":"user", "content":prompt})

    #调用ai大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.ll_name, st.session_state.ll_character)},
            *st.session_state.messages
        ],
        stream=True
    )

    #流式输出结果
    response_message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
    #保存大模型返回结果
    st.session_state.messages.append({"role":"assistant", "content":full_response})
    save_session()
















