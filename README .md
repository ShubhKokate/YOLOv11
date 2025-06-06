
#  Real-Time Traffic Congestion Detection using YOLOv11

This project implements a real-time traffic congestion detection system using the YOLOv11 object detection model. It identifies vehicles in live video feeds and classifies the traffic condition based on vehicle count and density.

📌 Overview Traffic congestion is a critical issue in urban areas, impacting daily life and logistics. This project uses deep learning and computer vision techniques to monitor and analyze traffic in real time.

## 🎯 Objectives Detect vehicles in video streams using YOLOv11
* Measure congestion levels based on vehicle density and lane occupancy

* Provide visual feedback with bounding boxes and congestion alerts

* Enable future integration with smart city systems
## 🛠️ Technologies Used Python
* penCV

* YOLOv11

* NumPy

* Jupyter Notebook



# Demo


https://www.kaggle.com/code/subhdrabaipatil/real-time-traffic-congestion-detection-yolov11/output
## Kaggle Notebook

https://www.kaggle.com/code/subhdrabaipatil/real-time-traffic-congestion-detection-yolov11/notebook
## Folder Stucture
```bash
├── src/
│   └── ultralytics-main
|           
├── bin/
│   └── Dockerfile
|   └── app.py
|   └── best.pt
|   └── last.pt
|   └── real-time-traffic-congestion-detection-yolov11.ipynb
|   └── requirement.txt
|   └── result.mp4
|   └── Dataset 
└── docs/
    └── README.md