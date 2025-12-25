from ultralytics import YOLO

model = YOLO(r'C:\Users\sneha\Desktop\yolo\yolo11n.pt')

train_results = model.train(
    data=r'C:\Users\sneha\Desktop\yolo\Astha.v1i.yolov11\data.yaml',
    epochs=5,
    imgsz=640,
    device='cpu' # or use 0,1,2.. for your gpu  
)
