基于 Streamlit 和 DeepSeek 大语言模型 构建的 AI 伴侣聊天应用，支持自定义角色人设、会话持久化存储与流式响应输出，模拟真实的陪伴式聊天体验。
✨ 核心功能
自定义伴侣人设 🎭：自由设置 AI 昵称与性格描述，打造专属陪伴风格
完整会话管理 📝：支持聊天记录的保存、加载与删除，历史对话永不丢失
流式响应输出 ⚡：模拟真实打字效果，对话更具交互感与沉浸感
本地数据持久化 🔒：会话数据存储在本地 sessions 目录，数据隐私有保障
简洁开箱即用 🚀：基于 Streamlit 构建的极简界面，无需前端开发经验
🛠️ 快速开始
1. 环境准备
Python 3.8+
有效的 DeepSeek API Key（获取地址）
2. 克隆项目
bash
运行
git clone https://github.com/Xull0924/Streamlit-LLM-Companion.git
cd Streamlit-LLM-Companion
3. 安装依赖
bash
运行
pip install -r requirements.txt
4. 配置 API Key
推荐使用环境变量管理密钥，避免硬编码：
powershell
# Windows
set DEEPSEEK_API_KEY=你的DeepSeek API密钥
bash
运行
# Mac/Linux
export DEEPSEEK_API_KEY=你的DeepSeek API密钥
也可直接在 app.py 中替换默认的 api_key 变量（仅用于快速测试）。
5. 运行项目
bash
运行
streamlit run app.py
浏览器将自动打开 http://localhost:8501，即可开始与 AI 伴侣聊天。
📂 项目结构
plaintext
Streamlit-LLM-Companion/
├── app.py                # 核心应用代码
├── requirements.txt      # 依赖清单
├── README.md             # 项目说明文档
├── .gitignore            # Git忽略规则
├── resources/            # 静态资源目录
│   └── logo.jpg          # 应用Logo
└── sessions/             # 会话数据存储目录（自动生成）
📖 使用说明
创建新会话：点击侧边栏「开始新的会话」，即可开启全新聊天
配置人设：在「伴侣信息」模块输入昵称与性格描述（例如：温柔体贴的治愈系姐姐）
管理历史会话：侧边栏历史会话列表支持一键加载或删除
开始聊天：在底部输入框发送消息，AI 将按设定人设进行流式回复
📦 依赖清单
txt
streamlit>=1.30.0
openai>=1.10.0
python-dotenv>=1.0.0
⚠️ 注意事项
确保 DeepSeek API Key 有效，否则无法调用大模型服务
sessions/ 目录会自动生成，删除该目录将清空所有历史会话
请勿将 API Key 直接提交到代码仓库，建议使用环境变量管理
