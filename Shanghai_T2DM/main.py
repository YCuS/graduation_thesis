import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import math
import numpy as np


class DFNet(nn.Module):
    def __init__(self):
        super(DFNet, self).__init__()
        self.a0 = nn.Parameter(torch.tensor(0.75))
        self.a1 = nn.Parameter(torch.tensor(3.7438e-05))
        self.a2 = nn.Parameter(torch.tensor(0.0002))
        self.b1 = nn.Parameter(torch.tensor(3.27))
        self.b2 = nn.Parameter(torch.tensor(190.0))
        self.b3 = nn.Parameter(torch.tensor(0.08))
        self.I_0 = nn.Parameter(torch.tensor(10.0))
        self.delta_t = 0.15

    def forward(self, x):
        length = x.size(0) - 1
        res = [torch.tensor(0.0)] * (length + 1) * 100
        res[0] = x[0]
        G = [torch.tensor(0.0)] * (length + 1)
        I = [torch.tensor(0.0)] * (length + 1) * 100
        I[0] = self.I_0
        for i in range(length * 100 + 99):
            res[i + 1] = res[i] + 2 * self.delta_t * (self.a0 - self.a1 * res[i] - self.a2 * res[i] * I[i])
            I[i + 1] = I[i] + 2 * self.delta_t * (self.b1 * res[i] ** 2 / (res[i] ** 2 + self.b2 ** 2) - self.b3 * I[i])
        for i in range(length + 1):
            G[i] = res[i * 100]
        return torch.stack(G, 0)

    def loss(self, x):
        pred = self.forward(x)
        return torch.nn.functional.mse_loss(x, pred)
def model2(data,params):
    a0, a1, a2, b1, b2, b3, I_0 = params
    sk=2
    r=80
    m=4
    length = len(data) - 1
    res = [0] * (length + 1) * 100
    res[0] = data[0]
    G = [0] * (length + 1)
    I = [0] * (length + 1) * 100
    I[0] = I_0
    delta_t = 0.15
    for i in range(length * 100 + 99):
        res[i + 1] = res[i] + 2 * delta_t * (a0 - a1 * res[i] - a2 * res[i] * I[i]+sk/(r**m+I[i]**m))
        I[i + 1] = I[i] + 2 * delta_t * (b1 * res[i] ** 2 / (res[i] ** 2 + b2 ** 2) - b3 * I[i])
    for i in range(length + 1):
        G[i] = res[i * 100]
    return G
if __name__ == "__main__":
    model = DFNet()
    model.load_state_dict(torch.load('model.pth'))
    optimizer = torch.optim.SGD(model.parameters(), lr=2e-12, weight_decay=0.01)
    data = torch.tensor([331.2,322.2,313.2,304.2,291.6,277.2,259.2,239.4,214.2,194.4,199.8])

    
    # pred_new = model2(data, (model.a0.item(), model.a1.item(), model.a2.item(), model.b1.item(), model.b2.item(), model.b3.item(), model.I_0.item()))
    # plt.clf()
    # pred = model(data).detach().numpy()
    # mse = torch.nn.functional.mse_loss(torch.tensor(pred), data)
    # print(f"MSE: {mse.item()}")
    # plt.plot(pred,color='blue', label='predict')
    # # plt.plot(pred_new, color='green', label='predict_new')
    # plt.plot(data, color='red', label='origin data')  # 使用红色线条表示实际值
    # plt.xlabel('Time (15 min)')
    # plt.ylabel('Glucose (mg dl-1)')
    # plt.title('Model2 prediction')
    # plt.grid(True)
    # plt.legend()
    # plt.show()
    # plt.close()
    # best_params = model.a0, model.a1, model.a2, model.b1, model.b2, model.b3, model.I_0
    # best_loss = torch.tensor(float('inf'))
    with torch.autograd.set_detect_anomaly(True):
        for i in range(50):
            loss = model.loss(data)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # if loss < best_loss:
            #     best_loss = loss
            #     best_params = model.a0, model.a1, model.a2, model.b1, model.b2, model.b3, model.I_0
            print(f'Iteration {i}, Loss: {loss.item()}')
    print(model.a0, model.a1, model.a2, model.b1, model.b2, model.b3, model.I_0)
    torch.save(model.state_dict(), 'model.pth')


