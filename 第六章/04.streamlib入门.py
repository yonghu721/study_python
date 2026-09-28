"""
Streamlit 入门演示页面
运行方式：
    pip install streamlit pandas numpy
    streamlit run app.py
"""

import time

import numpy as np
import pandas as pd
import streamlit as st

# ============================================================
# 1. 页面配置（必须是第一个 st 命令，且只能调用一次）
# ============================================================
st.set_page_config(
    page_title="Streamlit 入门演示",
    page_icon="🎈",
    layout="wide",                 # centered / wide
    initial_sidebar_state="expanded",
)

# ============================================================
# 2. 侧边栏导航
# ============================================================
with st.sidebar:
    st.title("🎈 Streamlit 入门")
    st.caption("一个 Python 文件就能搭出数据应用")

    demo = st.radio(
        "选择演示模块",
        [
            "1️⃣ 文本与 Markdown",
            "2️⃣ 数据展示",
            "3️⃣ 图表与地图",
            "4️⃣ 交互组件",
            "5️⃣ 布局与容器",
            "6️⃣ 缓存与会话状态",
            "7️⃣ 表单与反馈",
        ],
    )

    st.divider()
    st.info("提示：修改代码后点击右上角 **Rerun**，或开启 **Always rerun** 实时刷新。")

st.title("Streamlit 入门演示")

# ============================================================
# 模块 1：文本与 Markdown
# ============================================================
if demo == "1️⃣ 文本与 Markdown":
    st.header("基础文本输出")

    st.markdown("""
### 这是 Markdown 三级标题

支持 **加粗**、*斜体*、`行内代码`、~~删除线~~、[超链接](https://streamlit.io)。

- 无序列表 A
- 无序列表 B

1. 有序列表 1
2. 有序列表 2

> 这是一段引用文字。
""")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("代码块 st.code")
        st.code(
            """def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Streamlit"))""",
            language="python",
        )
    with col2:
        st.subheader("公式 st.latex")
        st.latex(r"E = mc^2")
        st.latex(r"\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i")

    st.divider()

    st.subheader("其它文本 API")
    st.text("st.text：纯文本，不解析 Markdown")
    st.write("st.write：万能输出，能自动识别字符串、字典、DataFrame、图表等")
    st.write({"框架": "Streamlit", "语言": "Python", "难度": "入门"})
    st.caption("st.caption：小号灰色说明文字")

# ============================================================
# 模块 2：数据展示
# ============================================================
elif demo == "2️⃣ 数据展示":
    st.header("展示 DataFrame")

    df = pd.DataFrame(
        np.random.randn(12, 4),
        columns=["语文", "数学", "英语", "物理"],
        index=[f"学生{i:02d}" for i in range(1, 13)],
    ).round(2)

    tab1, tab2, tab3 = st.tabs(["可交互表格", "静态表格", "JSON / 指标卡"])

    with tab1:
        st.write("`st.dataframe`：可排序、可缩放、可下载")
        st.dataframe(df)

    with tab2:
        st.write("`st.table`：静态表格，适合展示小数据")
        st.table(df.head(4))

    with tab3:
        st.write("`st.json`：展示字典 / JSON 结构")
        st.json({"model": "gpt", "temperature": 0.7, "tags": ["nlp", "demo"]})

        st.write("`st.metric`：指标卡，第三个参数是同比变化")
        c1, c2, c3 = st.columns(3)
        c1.metric("今日访问量", "8,432", "+12.4%")
        c2.metric("转化率", "3.7%", "-0.3%")
        c3.metric("平均停留时长", "4分12秒", "+8秒")

# ============================================================
# 模块 3：图表与地图
# ============================================================
elif demo == "3️⃣ 图表与地图":
    st.header("内置图表")

    chart_data = pd.DataFrame(
        np.random.randn(40, 3).cumsum(axis=0),
        columns=["北京", "上海", "广州"],
    )

    st.subheader("折线图 st.line_chart")
    st.line_chart(chart_data)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("柱状图 st.bar_chart")
        st.bar_chart(chart_data.tail(10))
    with col2:
        st.subheader("面积图 st.area_chart")
        st.area_chart(chart_data.tail(10))

    st.divider()

    st.subheader("地图 st.map")
    st.caption("数据需要包含 lat / lon 列（纬度、经度）")
    map_data = pd.DataFrame(
        np.random.randn(300, 2) / [40, 40] + [39.9042, 116.4074],  # 以北京为中心
        columns=["lat", "lon"],
    )
    st.map(map_data, zoom=10, size=20)

# ============================================================
# 模块 4：交互组件
# ============================================================
elif demo == "4️⃣ 交互组件":
    st.header("输入类组件")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("文本输入 st.text_input", placeholder="请输入姓名")
        age = st.slider("滑块 st.slider", 0, 120, 25)
        level = st.radio("单选 st.radio", ["入门", "进阶", "专家"], horizontal=True)
        agree = st.checkbox("复选 st.checkbox：我同意用户协议", value=True)

    with col2:
        city = st.selectbox("下拉框 st.selectbox", ["北京", "上海", "广州", "深圳"])
        hobbies = st.multiselect(
            "多选 st.multiselect",
            ["编程", "篮球", "音乐", "旅行", "摄影"],
            default=["编程"],
        )
        score = st.number_input("数字输入 st.number_input", 0.0, 100.0, 60.0, step=0.5)
        color = st.color_picker("颜色选择 st.color_picker", "#FF4B4B")

    st.divider()

    col3, col4 = st.columns(2)
    with col3:
        birthday = st.date_input("日期 st.date_input")
        meeting = st.time_input("时间 st.time_input")
    with col4:
        uploaded = st.file_uploader("文件上传 st.file_uploader", type=["csv", "txt"])
        if uploaded is not None:
            st.success(f"已收到文件：{uploaded.name}（{uploaded.size} 字节）")

    st.divider()

    st.subheader("组件返回值汇总")
    st.write(
        {
            "姓名": name or "（未填写）",
            "年龄": age,
            "水平": level,
            "同意协议": agree,
            "城市": city,
            "爱好": hobbies,
            "分数": score,
            "颜色": color,
            "生日": str(birthday),
            "会议时间": str(meeting),
        }
    )

    if st.button("点我试试 🎉", type="primary"):
        st.balloons()

# ============================================================
# 模块 5：布局与容器
# ============================================================
elif demo == "5️⃣ 布局与容器":
    st.header("布局方式")

    st.subheader("1. 多列 st.columns")
    c1, c2, c3 = st.columns([1, 2, 1])  # 宽度比例
    c1.success("第一列（窄）")
    c2.info("第二列（宽）")
    c3.warning("第三列（窄）")

    st.divider()

    st.subheader("2. 选项卡 st.tabs")
    t1, t2, t3 = st.tabs(["📊 数据", "📈 图表", "📝 说明"])
    t1.write("这里是数据区域")
    t2.write("这里是图表区域")
    t3.write("这里是说明区域")

    st.divider()

    st.subheader("3. 折叠面板 st.expander")
    with st.expander("点击展开查看更多"):
        st.write("折叠面板适合放次要信息，比如参数说明、帮助文档等。")

    st.divider()

    st.subheader("4. 占位容器 st.container / st.empty")
    with st.container(border=True):
        st.write("这是一个带边框的容器，可以把相关元素组合在一起。")

    placeholder = st.empty()
    placeholder.info("我是 st.empty 占位符，稍后会被替换")

    st.divider()

    st.subheader("5. 并排按钮 + 嵌套布局")
    left, right = st.columns(2)
    with left:
        with st.container(border=True):
            st.write("左侧卡片")
            st.button("左侧按钮", key="btn_left")
    with right:
        with st.container(border=True):
            st.write("右侧卡片")
            st.button("右侧按钮", key="btn_right")

# ============================================================
# 模块 6：缓存与会话状态
# ============================================================
elif demo == "6️⃣ 缓存与会话状态":
    st.header("性能与状态管理")

    # ---------- 缓存 ----------
    st.subheader("1. 数据缓存 @st.cache_data")

    @st.cache_data(show_spinner=False)
    def slow_add(a: int, b: int) -> int:
        """模拟耗时计算，第一次调用慢，之后命中缓存秒回"""
        time.sleep(2)
        return a + b

    a = st.number_input("参数 a", 0, 100, 10)
    b = st.number_input("参数 b", 0, 100, 20)

    if st.button("开始计算（第一次需要 2 秒）"):
        with st.spinner("计算中…"):
            result = slow_add(a, b)
        st.success(f"结果：{a} + {b} = {result}")
        st.caption("再次点击同样参数，会立刻返回结果（走缓存）。改参数才会重新计算。")

    st.divider()

    # ---------- 会话状态 ----------
    st.subheader("2. 会话状态 st.session_state")
    st.caption("每次点击按钮页面都会重跑，普通变量会被重置，用 session_state 才能保存状态。")

    if "count" not in st.session_state:
        st.session_state.count = 0

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ 加 1"):
            st.session_state.count += 1
    with col2:
        if st.button("➖ 减 1"):
            st.session_state.count -= 1
    with col3:
        if st.button("🔄 重置"):
            st.session_state.count = 0

    st.metric("当前计数", st.session_state.count)

    with st.expander("查看 session_state 全部内容"):
        st.write(dict(st.session_state))

# ============================================================
# 模块 7：表单与反馈
# ============================================================
elif demo == "7️⃣ 表单与反馈":
    st.header("表单 st.form")

    with st.form("login_form", clear_on_submit=False):
        st.write("表单内的组件不会触发页面重跑，只有点击提交按钮才会。")
        username = st.text_input("用户名")
        password = st.text_input("密码", type="password")
        submitted = st.form_submit_button("提交", type="primary")

    if submitted:
        if username and password:
            st.success(f"欢迎回来，{username}！")
        else:
            st.error("用户名和密码不能为空")

    st.divider()

    st.header("消息与反馈组件")

    c1, c2 = st.columns(2)
    with c1:
        st.success("st.success：操作成功")
        st.info("st.info：普通提示")
        st.warning("st.warning：警告信息")
        st.error("st.error：错误信息")
        st.exception(ValueError("st.exception：显示异常堆栈"))
    with c2:
        if st.button("显示进度条 st.progress"):
            bar = st.progress(0, text="处理中…")
            for i in range(101):
                time.sleep(0.01)
                bar.progress(i, text=f"处理中… {i}%")
            bar.empty()
            st.toast("处理完成 ✅")

        if st.button("显示加载动画 st.spinner"):
            with st.spinner("拼命加载中…"):
                time.sleep(1.5)
            st.toast("加载完成 🎈")

        if st.button("下雪特效 st.snow"):
            st.snow()

# ============================================================
# 页脚
# ============================================================
st.divider()
st.caption("🎈 Streamlit 入门演示 · 文档：https://docs.streamlit.io")