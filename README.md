# Autonomous QR Code Reading Drone System

A Python-based application that enables autonomous QR code scanning and mapping using DJI Tello drones. This system provides real-time drone control, QR code detection, position tracking, and data export capabilities through an intuitive graphical interface.

## Features

- **Autonomous Drone Control**: Manual and automated navigation of DJI Tello drones
- **Real-time QR Code Detection**: Continuous scanning and decoding of QR codes using drone camera
- **Interactive Map Visualization**: Live position tracking and QR code location marking
- **Data Export**: Automatic export of QR code data and positions to Excel files
- **Customizable Warehouse Dimensions**: Adjustable map boundaries for different environments
- **Return to Home**: One-click return to starting position functionality

## System Architecture

The application consists of six main components:

- **Main.py**: Entry point and application orchestrator
- **MainPanel.py**: PyQt5-based graphical user interface
- **DroneController.py**: Drone movement and position management
- **QRReader.py**: QR code detection using drone camera feed
- **MapVisualizer.py**: Real-time map rendering and visualization
- **ExcelWriter.py**: Data export and logging functionality

## Requirements

- Python 3.7+
- PyQt5
- OpenCV (cv2)
- pyzbar
- djitellopy
- pandas
- matplotlib

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/autonomous-qr-reading-drone.git
cd autonomous-qr-reading-drone
```

2. Install required packages:
```bash
pip install PyQt5 opencv-python pyzbar djitellopy pandas matplotlib
```

3. Ensure your DJI Tello drone is powered on and connected to the same network as your computer.

## Usage

1. Launch the application:
```bash
python Main.py
```

2. Configure warehouse dimensions using the input fields (width, height in centimeters)

3. Set movement parameters (step size, altitude adjustments)

4. Use directional controls to navigate the drone manually

5. The system automatically scans for QR codes during movement

6. Detected QR codes are marked on the map with their positions

7. Click "Save" to export QR code data to Excel

8. Use "Return to Start" to bring the drone back to the origin point

## Controls

- **Directional Buttons**: Move drone up, down, left, right
- **Return to Start**: Navigate back to origin position (0,0)
- **Save**: Export QR code data and save map visualization
- **Update Map**: Apply new warehouse dimensions

## Data Output

The system generates two types of output:

1. **Excel File**: Contains QR code content, coordinates (X,Y), and timestamps
   - Location: `C:\Users\monster\Desktop\Code\python\save\`
   - Format: `qr_codes_YYYYMMDD_HHMMSS.xlsx`

2. **Map Image**: Visual representation of drone path and QR code locations
   - Filename: `map_output.png`

## Technical Specifications

- **Coordinate System**: 2D Cartesian coordinates in centimeters
- **Default Warehouse Size**: 100cm × 1000cm
- **Real-time Processing**: Continuous QR code scanning during drone movement
- **Camera Feed**: Live video stream from DJI Tello camera
- **Position Tracking**: Accurate coordinate logging for each QR code detection

## Safety Notes

- Ensure adequate lighting conditions for optimal QR code detection
- Maintain safe operating distance from obstacles
- Monitor battery level during extended operations
- Verify network connectivity between drone and control system

## Troubleshooting

- **Connection Issues**: Ensure drone and computer are on the same WiFi network
- **QR Code Detection**: Verify proper lighting and QR code visibility
- **Map Display**: Check matplotlib backend compatibility with your system
- **Export Errors**: Verify write permissions for the output directory

## Contributing

This project is designed for warehouse automation and inventory management applications. Contributions for additional features, bug fixes, and performance improvements are welcome.

## License

This project is provided for educational and research purposes. Please ensure compliance with local regulations regarding drone operations.
