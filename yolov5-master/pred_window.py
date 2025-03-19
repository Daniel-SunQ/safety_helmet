import torch
import os
# model = torch.hub.load('./', 'custom', path='./runs/train/exp2/weights/best.pt', source='local')
#
# img = './0_Concern-In-China-As-Mystery-Virus-Spreads_jpg.rf.5633f5fe7a9b926101b7fc16615dfb6a.jpg'
# result = model(img)
# result.show()
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
root_path = r'C:\Users\Administrator\Downloads\yolov5-master\construction_safety\test\labels'
label_root = './runs/detect/exp7/labels'
img_path = os.listdir(root_path)

for img in img_path:
    test_path = os.path.join(root_path, img)
    pred_path = os.path.join(label_root, img)
    with open(test_path) as f:
        f.readline()