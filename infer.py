import torch


model = torch.hub.load('pytorch/vision', 'googlenet', pretrained=True)
model.eval()


def locate_object(frame, obj_of_interest):
    return 300, 600
