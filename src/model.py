import torch.nn as nn
import torch.nn.functional as F

class SimpleMLP(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleMLP, self).__init__()
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
       # self.multihead_attn = nn.MultiheadAttention(input_size * 16, 16)

    def forward(self, x):
        #x, _ = self.multihead_attn(x.repeat(16), x.repeat(16), x.repeat(16))
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        x = F.sigmoid(x)

        if not self.training:
            x = (x > 0.7).float()
        return x