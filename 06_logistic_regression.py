from torch import tensor
from torch import nn
import torch.nn.functional as F
import torch.optim as optim

x_data = tensor([[1.0], [2.0], [3.0], [4.0]])
y_data = tensor([[0.], [0.], [1.], [1.]])


class Model(nn.Module):
    def __init__(self):
        '''
        In  the constructor we instantiate nn.Linear module
        '''
        super(Model, self).__init__()
        self.linear = nn.Linear(1, 1)  # One in and one out

    def forward(self, x):
        y_pred = F.sigmoid(self.linear(x))
        return y_pred


# our model
model = Model()

# Construct our loss function and an Optimizer. The call to model.parameters()
# in the SGD constructor will contain the learnable parameters of the two
# nn.Linear modules which are members of the modle
criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x_data)

    # Compute and print loss
    loss = criterion(y_pred, y_data)
    print(f'Epoch {epoch+1}/1000 | Loss: {loss.item():.4f}')

    # Zero gradients, perform a backward pass, and update the weights
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# After training
print(f'\n Let\'s predict the hours need to score above 50%\n{"=" * 50}')
hour_var = model(tensor([[1.0]]))
print(
    f'Prediction after 1 hour of training: {hour_var.item():.4f} | Above 50%: {hour_var.item()>0.5}'
)
hour_var = model(tensor([[7.0]]))
print(
    f'Prediction after 7 hour of training: {hour_var.item():.4f}| Above 50%: {hour_var.item()>0.5}'
)
