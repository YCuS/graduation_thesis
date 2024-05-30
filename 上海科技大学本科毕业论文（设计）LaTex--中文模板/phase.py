import numpy as np
import matplotlib.pyplot as plt

# 定义系统的动态方程
def system_dynamics(x, y, r):
    x_dot = r - x**2
    y_dot = -y
    return x_dot, y_dot

# 绘制相图的函数
def plot_phase_portrait(r, ax):
    # 创建网格空间
    x = np.linspace(-2.0, 2.0, 20)
    y = np.linspace(-2.0, 2.0, 20)
    
    X, Y = np.meshgrid(x, y)
    U, V = np.zeros_like(X), np.zeros_like(Y)
    
    # 计算每个点的动态方程
    for i in range(len(x)):
        for j in range(len(y)):
            x_dot, y_dot = system_dynamics(X[i, j], Y[i, j], r)
            U[i, j] = x_dot
            V[i, j] = y_dot
    
    # 绘制向量场
    ax.quiver(X, Y, U, V, color='blue')
    
    # 标出不动点或鬼魂区域
    if r > 0:
        ax.plot(np.sqrt(r), 0, 'ro')  # 红色点表示不动点
        ax.text(np.sqrt(r), 0, 'P', ha='right', va='bottom')
        ax.plot(-np.sqrt(r), 0, 'ro')
        ax.text(-np.sqrt(r), 0, 'Q', ha='right', va='bottom')
        # 可以添加代码来圈出鬼魂区域，例如使用ax.add_patch()...
    elif r == 0:
        ax.plot(0, 0, 'ro')
        ax.text(np.sqrt(r), 0, 'F', ha='right', va='bottom')
        # 绘制鬼魂区域，例如使用ax.add_patch()...
        pass

    # 设置标题和坐标轴标签
    ax.set_title(f'Phase Portrait for r={r}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

# 创建图形和子图
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# 绘制r<0的相图
plot_phase_portrait(-1, axs[0])

# 绘制r=0的相图
plot_phase_portrait(0, axs[1])

# 绘制r>0的相图
plot_phase_portrait(1, axs[2])

# 显示图形
plt.tight_layout()
plt.show()
