# 🎨 Real-Time Color Detector with OpenCV

This project is a **Real-Time Color Detector** built using Python and OpenCV. It captures video from your webcam and displays the name, RGB values, and HEX code of the color located at the center of the screen — updating in real time.

It's a simple yet powerful tool to help you identify and visualize colors instantly, whether you're a developer, designer, artist, or just curious about the world of colors.

---

## 🖼️ Features

- 📷 Real-time webcam color detection  
- 🎯 Detects color from the center of the screen  
- 🌈 Displays:
  - Color name (based on closest match)
  - RGB values
  - HEX code
- 🧠 Automatically adjusts text color for better readability
- 💡 Clean and modern UI with translucent overlay and shadowed text
- 🧩 Modular and easy to expand

---

## 📁 How It Works

1. A 60x60 region is selected in the center of the webcam frame.
2. The average color of that region is calculated.
3. The script finds the closest color match from a CSV dataset.
4. The result is rendered on the screen with RGB and HEX info.

---

## 📸 Screenshot

![Color Detector Screenshot](https://via.placeholder.com/800x400.png?text=Color+Detector+Preview)

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed. Then install the required libraries:

```bash
pip install opencv-python pandas
OR
py -m pip install opencv-python pandas
