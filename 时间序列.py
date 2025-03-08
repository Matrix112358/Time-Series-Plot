import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.ticker import FormatStrFormatter  # 用于设置 Y 轴坐标格式

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
data = pd.DataFrame({
    -2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    -1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    1: [-26.263, -11.854, -5.22, -2.64, -1.387, -31.591, -13.759, -5.717, -2.813, -1.46, -31.724, -13.846, -5.742, -2.825, -1.467, -26.973, -12.072, -5.292, -2.676, -1.408],
    2: [2.3484, -15.629, -5.9542, -2.0327, -0.9075, 4.1913, -15.895, -6.0496, -2.0108, -0.8981, 6.0996, -6.2867, -4.1446, -1.7184, -0.8177, 6.238, -1.4092, -2.2917, -1.3017, -0.6899],
    3: [2.7828, -1.4231, -19.262, -7.733, -2.885, -2.638, -4.474, -20.376, -7.95, -2.952, 1.288, -12.655, -12.278, -6.23, -2.701, 0.811, -7.616, -6.941, -4.361, -2.262],
    4: [5.3133, 4.8532, 2.2858, -12.111, -4.3139, 5.8074, 4.3294, -0.7554, -7.4659, -3.7726, 4.4301, 0.0773, -10.932, -5.4396, -2.8702, 1.8737, -9.9723, -8.3183, -4.2367, -2.223],
    5: [7.2773, 7.4455, 5.0324, 0.2693, -13.012, 8.6329, 8.7001, 4.4199, -5.2135, -8.7204, 8.6192, 8.1235, 0.5753, -13.065, -6.4492, 7.29, 6.617, -8.8578, -8.9325, -4.7684],
    6: [7.3878, 7.4909, 3.6663, -5.2051, -6.8751, 8.8368, 9.1957, 3.9123, -13.933, -20.157, 8.8603, 9.3009, 4.2722, -10.301, -22.403, 7.5213, 7.9056, 4.1955, -14.087, -13.658],
    7: [9.4575, 11.596, 12.639, 12.865, 10.403, 11.03, 13.652, 14.796, 15.812, 12.587, 11.052, 13.659, 14.677, 14.146, 8.5416, 9.5956, 11.811, 12.57, 11.491, -2.5996],
    8: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    9: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}, index=range(1, 21))

# 侧边栏
with st.sidebar:
    st.header("标测电极")
    
    # 标测电极A
    electrode_a = st.slider("标测电极A", 1, 20, 10, 1, key="electrode_a")
    
    # 标测电极B
    electrode_b = st.slider("标测电极B", 1, 20, 10, 1, key="electrode_b")
    
    # 调整 X 轴紧凑度的滑动条
    x_spacing = st.slider(
        "X 轴紧凑度", 
        min_value=0.1, 
        max_value=1.0, 
        value=0.5, 
        step=0.1, 
        key="x_spacing"
    )
    
    # 显示具体数值的按钮
    show_values = st.button("显示具体数值")

# 计算差值
diff_a = data.loc[electrode_a]
diff_b = data.loc[electrode_b]
diff_ab = diff_a - diff_b

# 时间序列图
st.header("时间序列图")

# 动态调整图像宽度
fig_width = 10 * x_spacing  # 根据 x_spacing 动态调整图像宽度
fig, (ax_a, ax_b, ax_ab) = plt.subplots(3, 1, figsize=(fig_width, 10))

# 动态调整 X 轴范围
x_values = np.arange(len(data.columns)) * x_spacing  # 根据 x_spacing 调整 X 轴范围

# 电极 A
ax_a.plot(x_values, diff_a, marker="o", markersize=4, linewidth=1.5)
ax_a.set_title(f"{electrode_a}", fontsize=10)
ax_a.set_xlabel("", fontsize=8)
ax_a.set_ylabel("")  # 隐藏 Y 轴标签
ax_a.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # Y 轴保留两位小数
ax_a.set_xticks(x_values)  # 设置 X 轴刻度
ax_a.set_xticklabels(data.columns, rotation=90, fontsize=8)  # X 轴标签垂直显示
ax_a.grid(True, linestyle="--", alpha=0.6)

# 电极 B
ax_b.plot(x_values, diff_b, marker="o", markersize=4, linewidth=1.5)
ax_b.set_title(f"{electrode_b}", fontsize=10)
ax_b.set_xlabel("", fontsize=8)
ax_b.set_ylabel("")  # 隐藏 Y 轴标签
ax_b.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # Y 轴保留两位小数
ax_b.set_xticks(x_values)  # 设置 X 轴刻度
ax_b.set_xticklabels(data.columns, rotation=90, fontsize=8)  # X 轴标签垂直显示
ax_b.grid(True, linestyle="--", alpha=0.6)

# 电极 A-B
ax_ab.plot(x_values, diff_ab, marker="o", markersize=4, linewidth=1.5)
ax_ab.set_title(f"{electrode_a} -  {electrode_b}", fontsize=10)
ax_ab.set_xlabel("", fontsize=8)
ax_ab.set_ylabel("")  # 隐藏 Y 轴标签
ax_ab.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # Y 轴保留两位小数
ax_ab.set_xticks(x_values)  # 设置 X 轴刻度
ax_ab.set_xticklabels(data.columns, rotation=90, fontsize=8)  # X 轴标签垂直显示
ax_ab.grid(True, linestyle="--", alpha=0.6)

# 调整子图间距
plt.tight_layout()

# 显示图表
st.pyplot(fig)

# 显示具体数值（横排显示）
if show_values:
    st.subheader("具体数值（横排显示）")
    
    # 将数据转换为横排格式
    df_a = pd.DataFrame({f"电极 {electrode_a} 差值": diff_a}).T
    df_b = pd.DataFrame({f"电极 {electrode_b} 差值": diff_b}).T
    df_ab = pd.DataFrame({f"电极 {electrode_a} - 电极 {electrode_b} 差值": diff_ab}).T
    
    # 显示表格
    st.write("电极 A 差值：")
    st.dataframe(df_a)
    
    st.write("电极 B 差值：")
    st.dataframe(df_b)
    
    st.write("电极 A-B 差值：")
    st.dataframe(df_ab)
