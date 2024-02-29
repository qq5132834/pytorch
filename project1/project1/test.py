import torch
st = torch.cuda.is_available()
print(st)

t = torch.zeros(5)
print(t)
type = t.dtype
print(type)

d = t.device
print(d)

t = torch.FloatTensor([[1,2],[3,4]])
print(t)