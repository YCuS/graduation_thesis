import numpy as np
import pandas as pd
from scipy.optimize import minimize

# 差分方程模型
def differential_equation(G_t, theta):
    a0, a1, a2, b1, b2, b3, I_0, I_1 = theta
    Delta_t = 0.25
    leng= len(G_t)-1
    res= np.zeros(leng+1)
    res[0]= G_t[0]
    res[1]= G_t[1]
    I= np.zeros(leng+1)
    I[0]= I_0
    I[1]= I_1
    for i in range(1, leng):
        G_tm1 = G_t[i-1]
        I_tm1 = I[i-1]
        G_tp1 = G_tm1 + 2 * Delta_t * (a0 - a1 * G_t[i] - a2 * G_t[i] * I[i] )
        I_tp1 = I_tm1 + 2 * Delta_t * (b1 * G_t[i] ** 2 / (G_t[i] ** 2 + b2 ** 2) - b3 * I[i])
        I[i+1] = I_tp1
        res[i+1]= G_tp1
    # print(I)
    # print(res)
    return res

# 损失函数
def loss_function(theta, data, epsilon):
    loss = 0
    
    # 遍历数据
    for i in range(1, len(data)):
        G_t = data[i]
        simulated_G= differential_equation(G_t, theta)
        # print(np.linalg.norm(data[i] - simulated_G, ord=2)/len(simulated_G))
        # 损失累加
        loss += np.linalg.norm(data[i] - simulated_G, ord=2)
    
    # 正则化项
    regularization_term = epsilon * np.linalg.norm(theta)
    
    # 总损失
    total_loss = loss + regularization_term
    
    
    return total_loss

# 使用梯度下降法优化模型参数

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        # 移除换行符和多余空格，然后以逗号分隔字符串
        line_data = line.strip().split(',')
        # 将字符串列表转换为浮点数组
        float_array = np.array([float(value) for value in line_data])
        data.append(float_array)
        
    return data

# 主函数
if __name__ == '__main__':
    # 加载数据
    # 请将数据文件路径替换为实际文件路径
    data_file_path = 'output_vectors.txt'
    
    data = load_data(data_file_path)
    initial_theta = np.array([703,1.5,0.53,9,0.7,0.75,11,14])
    # 正则化参数
    epsilon = 0.5
    # 对每一段数据进行优化