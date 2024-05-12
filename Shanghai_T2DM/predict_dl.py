import numpy as np
import pandas as pd
from scipy.optimize import minimize

# 差分方程模型
def differential_equation(G_t, theta):
    a0, a1, a2, b1, b2, b3, I_0, I_1 = theta
    Delta_t = 0.25
    leng = len(G_t) - 1
    res = np.zeros(leng + 1)
    res[0] = G_t[0]
    res[1] = G_t[1]
    I = np.zeros(leng + 1)
    I[0] = I_0
    I[1] = I_1
    for i in range(1, leng):
        G_tm1 = G_t[i - 1]
        I_tm1 = I[i - 1]
        G_tp1 = G_tm1 + 2 * Delta_t * (a0 - a1 * G_t[i] - a2 * G_t[i] * I[i])
        I_tp1 = I_tm1 + 2 * Delta_t * (b1 * G_t[i] ** 2 / (G_t[i] ** 2 + b2 ** 2) - b3 * I[i])
        I[i + 1] = I_tp1
        res[i + 1] = G_tp1
    return res

# 损失函数
def loss_function(theta, data, epsilon):
    loss = 0
    # 遍历数据
    for i in range(len(data)):
        G_t = data[i]
        simulated_G = differential_equation(G_t, theta)
        # 损失累加
        loss += np.linalg.norm(data[i] - simulated_G, ord=2)/len(simulated_G)
    # 正则化项
    regularization_term = epsilon * np.linalg.norm(theta)
    # 总损失
    total_loss = loss + regularization_term
    return total_loss

# 数据加载函数
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line_data = line.strip().split(',')
        float_array = np.array([float(value) for value in line_data])
        data.append(float_array)
    return data

# 数据划分函数
def split_data(data, train_ratio=0.8):
    total_rows = len(data)
    train_size = int(total_rows * train_ratio)
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data
def evaluate_model(theta, test_data):
    total_error = 0
    # 遍历测试数据
    for i in range(len(test_data)):
        G_t = test_data[i]
        simulated_G = differential_equation(G_t, theta)
        # 计算误差
        error = np.linalg.norm(test_data[i] - simulated_G, ord=2)
        total_error += error
    
    # 返回测试集上的平均误差
    average_error = total_error / len(test_data)
    return average_error
# 主函数
if __name__ == '__main__':
    # 加载数据
    data_file_path = 'output_vectors_2.txt'
    data = load_data(data_file_path)
    
    # 将数据划分为参数估计集和检验集
    train_data, test_data = split_data(data)
    
    # 初始参数
    initial_theta = np.array([703, 1.5, 0.53, 9, 0.7, 0.75, 11, 14])
    
    # 正则化参数
    epsilon = 0.2
    
    # 优化模型参数
    result = minimize(loss_function, initial_theta, args=(train_data, epsilon), method='BFGS')
    test_error = evaluate_model(result.x, test_data)
    # 打印优化后的结果
    print(f'Optimized parameters: {result.x}')
    print(f'Minimized loss: {result.fun}')
    print(f'Test error: {test_error}')