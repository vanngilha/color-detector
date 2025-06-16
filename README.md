# 🎨 Real-Time Color Detector with OpenCV

### 📹 Video Demo:
> *https://www.youtube.com/watch?v=SoSC_lMgSrE*

---

## 📖 Project Description

This project is a **Real-Time Color Detector** developed in Python using **OpenCV** and **Pandas**. It captures video from your **webcam**, identifies the average color at the center of the frame, and displays the **name**, **RGB values**, and **HEX code** of that color — all in real time.

It’s a lightweight yet powerful tool, ideal for developers, designers, artists, or anyone curious about exploring the world of colors through computer vision.

---

## 🎯 Objective

The main goal of this project is to apply **computer vision** concepts in a practical way by using Python libraries to detect and interpret colors from live webcam input. This helps solidify skills learned in the CS50 course and showcases real-world application of programming knowledge.

---

## 🛠️ Technologies Used

- 🐍 Python 3  
- 🧠 OpenCV  
- 📊 Pandas  
- 📷 Webcam Input  
- 📁 CSV Dataset for Color Names

---

## 🖼️ Features

- 📷 Real-time color detection via webcam  
- 🎯 Detects color from the center of the screen  
- 🌈 Displays:
  - Color name (closest match)
  - RGB values
  - HEX code  
- 🧠 Smart contrast: adjusts text color for readability  
- 🧩 Modular code structure  
- 💡 Clean, modern UI with overlay and shadows

---

## ⚙️ How It Works

1. Captures video feed from webcam.
2. Selects a 60x60 pixel region at the center of the frame.
3. Calculates the average color of that region.
4. Compares it with a CSV database of colors to find the closest match.
5. Displays the matched color name, RGB, and HEX values on the screen.

---

## 🖼️ Screenshot

![Color Detector Screenshot](https://ibb.co/Y4hsKs9c)

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your machine. Then, install the required libraries using pip:

```bash
pip install opencv-python pandas
# OR
py -m pip install opencv-python pandas
