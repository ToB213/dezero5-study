import torch
import matplotlib.pyplot as plt
import torch.nn as nn

torch.manual_seed(0)
x = torch.rand(100, 1)
y = 2 * x + 5 + torch.rand(100, 1)

class Model(nn.Module):
    def __init__(self, input_size=1, output_size=1):
        super().__init__()
        self.linear = nn.Linear(input_size, output_size)
    def forward(self, x):
        return self.linear(x)

lr = 0.1
iters = 100
model = Model()

for param in model.parameters():
    print(param)

optimizer = torch.optim.SGD(model.parameters(), lr=lr)

for i in range(iters):
    y_hat = model(x)
    loss = nn.functional.mse_loss(y, y_hat)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    if i % 10 == 0:
        print(loss.item())

print(loss.item())
print('___')
W = model.linear.weight.item()
b = model.linear.bias.item()
print('W =', W)
print('b =', b)

plt.scatter(x.detach().numpy(), y.detach().numpy(), s=10)
x_line = torch.tensor([[0.0], [1.0]])
y_line = W * x_line.numpy() + b
plt.plot(x_line.numpy(), y_line, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.show()