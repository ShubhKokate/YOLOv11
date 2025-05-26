🚦 Real-Time Traffic Congestion Detection using YOLOv11
This project implements a real-time traffic congestion detection system using the YOLOv11 object detection model. It identifies vehicles in live video feeds and classifies the traffic condition based on vehicle count and density.

📌 Overview
Traffic congestion is a critical issue in urban areas, impacting daily life and logistics. This project uses deep learning and computer vision techniques to monitor and analyze traffic in real time.

🎯 Objectives
Detect vehicles in video streams using YOLOv11

Measure congestion levels based on vehicle density and lane occupancy

Provide visual feedback with bounding boxes and congestion alerts

Enable future integration with smart city systems

🛠️ Technologies Used
Python

OpenCV

YOLOv11

NumPy

Jupyter Notebook

📂 Project Structure
bash
Copy
Edit
├── yolov11_config/         # YOLOv11 config and weights
├── input_videos/           # Sample video inputs
├── output/                 # Processed video outputs
├── traffic_detection.ipynb # Main Jupyter Notebook
├── utils.py                # Utility functions (vehicle count, draw boxes, etc.)
├── README.md
🚀 How to Run
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/real-time-traffic-detection.git
cd real-time-traffic-detection
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Download YOLOv11 Weights
Make sure you have the YOLOv11 weights file in the yolov11_config/ directory. (Add instructions or a link here for download.)

Run the Notebook
Open and run traffic_detection.ipynb in Jupyter Notebook or JupyterLab.

📊 Output
Real-time detection of vehicles with bounding boxes

Dynamic classification of traffic congestion levels:

🚗 Low (Green)

🚧 Medium (Yellow)

🛑 High (Red)

📈 Sample Results

🔮 Future Enhancements
Support for multiple camera streams

Integration with alert systems or dashboards

Geo-location tagging for congestion mapping

🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

📄 License
MIT License
