# Al-Based-Accident-Prevention-in-MMS-Modular-Manufacturing-System-
Real-time accident prevention system using YOLO/MediaPipe and Arduino relay control
# AI-Based Accident Prevention System using Arduino

This project provides a real-time safety mechanism for Modular Manufacturing Systems (MMS) by detecting human presence near dangerous machinery using AI-based visual monitoring (MediaPipe) and stopping a 24V machine via an Arduino-controlled relay, buzzer, and LED alert.

---

## 📌 Features

- 🧠 AI-based detection using MediaPipe (468 Face Mesh, 21 Hand Landmarks, 33 Pose Points)
- ⚠️ Danger zone detection with STOP command to Arduino
- 🔌 Relay-controlled shutdown of motor
- 🚨 Buzzer and LED alerts on human detection
- 💻 Python script with USB Serial communication to Arduino

---

## 🎯 Project Goals

- Reduce industrial accidents using low-cost AI + hardware
- Integrate computer vision with real-world actuation
- Demonstrate modular, scalable design for factory safety
- Enable future expansion with Raspberry Pi or PPE detection

---

## 🛠 Components Used

| No. | Component             | Quantity | Purpose                                           |
|-----|------------------------|----------|----------------------------------------------------|
| 1   | Arduino Uno            | 1        | Receives STOP/START from Python via USB           |
| 2   | 5V Relay Module        | 1        | Switches 24V motor ON/OFF                         |
| 3   | 24V DC Motor / Fan     | 1        | Represents drilling/fan station                   |
| 4   | USB Webcam             | 1        | Captures real-time video for detection            |
| 5   | LED (Red)              | 1        | Glows when danger is detected                     |
| 6   | Buzzer (5V)            | 1        | Sound alert when danger detected                  |
| 7   | Breadboard + Wires     | Many     | Circuit connections                               |
| 8   | Laptop or PC           | 1        | Runs Python code (YOLOv8/MediaPipe)               |

---

## 🧠 How It Works

1. Webcam sends real-time video to Python program
2. MediaPipe detects human face/hand/pose mesh
3. If any landmark enters danger zone (Y threshold), Python sends `STOP` via Serial
4. Arduino receives command and:
   - Turns OFF relay (motor power cut)
   - Turns ON buzzer and LED
5. When danger clears, Python sends `START` to resume

---

## 🧾 Installation

### Python Dependencies
```bash
pip install opencv-python mediapipe pyserial
