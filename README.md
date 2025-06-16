
---

# 🎨 Real-Time Color Detector with OpenCV

## 📹 Video Demo

> [Click here to watch](https://www.youtube.com/watch?v=SoSC_lMgSrE)

---

## 📖 Project Description

This project is a **Real-Time Color Detector** built in **Python** using the **OpenCV** and **Pandas** libraries. It captures live video input from the user's **webcam**, detects the average color in the center of the video frame, and displays the **color name**, **RGB values**, and **HEX code** in real-time.

The purpose of this project is to provide a practical and interactive way to explore **computer vision** concepts. It transforms a theoretical understanding into a visually engaging tool that is both educational and useful for developers, designers, and anyone curious about real-world color detection.

---

## 🎯 Objectives

This project was developed as the **final project for CS50**, aiming to apply programming concepts in a real-world application. Key goals include:

* Utilize Python libraries to interact with hardware (webcam) and process video in real-time.
* Apply image processing techniques to analyze colors.
* Practice working with structured datasets (CSV files).
* Develop an interactive and visually intuitive application.
* Consolidate knowledge of modular programming, abstraction, and efficiency.

---

## 🧩 Project Structure

The project contains the following key files and folders:

* `color_detector.py`: Main script that handles video capture, color processing, and display logic.
* `colors.csv`: Dataset containing over 800 color names, along with their RGB and HEX values.
* `assets/harvard_logo.png`: A Harvard logo image used as a watermark overlay in the video frame.
* `images/final-project-havard.png`: A screenshot of the project in action, used in this documentation.
* `README.md`: This markdown file explaining the project in detail.
* `requirements.txt`: (optional) Can be used to simplify installation of Python dependencies.

---

## 🛠️ Technologies Used

* **Python 3**
* **OpenCV** – for image processing and GUI display
* **Pandas** – for reading and handling the color dataset
* **CSV dataset** – used to map RGB values to human-readable color names
* **Webcam** – real-time video input source

---

## ⚙️ How It Works

When the script runs, it starts capturing video from the user's webcam. A square region of 60x60 pixels at the center of the video frame is selected. The average RGB color values of this region are calculated and then compared to a dataset of known color names in the `colors.csv` file.

The comparison is made using **Manhattan distance** (sum of absolute differences in RGB values), and the closest match is considered the detected color. The name of the color, the RGB triplet, and the HEX code are then rendered on top of the video frame using OpenCV’s drawing functions.

A dynamic color panel is also displayed, along with a high-contrast text label and a logo in the corner of the screen.

---

## 🖼️ Features

* 📷 Real-time color detection using webcam video feed
* 🎯 Detects and analyzes the color in the center of the screen
* 🌈 Displays:

  * Color name (closest match)
  * RGB values
  * HEX code
* 🧠 Smart contrast: text automatically switches between black and white for readability based on background brightness
* 🧩 Modular code: logic separated into clear, maintainable functions
* 🖼️ Logo overlay support with transparency

---

## 📁 File Explanations

### `color_detector.py`

This is the core Python file. It opens the webcam, processes each video frame, calculates the average color in the center, compares it to the dataset, and overlays the results on the video. It also includes the `overlay_image()` function to handle images with alpha transparency, such as the Harvard logo.

### `colors.csv`

A simple dataset containing color names and corresponding RGB and HEX values. Each row includes:

* `color_name`
* `R`, `G`, `B`
* `hex`

Used to determine the nearest named color from the average RGB.

### `assets/harvard_logo.png`

This image is included to personalize the UI. It's resized and overlaid on the top-left corner using alpha blending for transparency.

### `images/final-project-havard.png`

A screenshot used to illustrate the output in the documentation.

---

## 🚀 How to Run the Project

### Prerequisites

* Python 3 installed
* A functional webcam connected to your device
* Required libraries installed via pip:

```bash
pip install opencv-python pandas
```

### Execution

Simply run the script:

```bash
python3 color_detector.py
```

A window will open showing your webcam video with the color information rendered on top.

---

## ❗ Common Issues

If you're running this project in an online IDE such as **CS50 IDE**, the webcam might not be accessible due to sandbox restrictions or browser limitations.

In such cases, it is **recommended to run the project locally** on your own machine using an IDE like VS Code or directly through the terminal.

---

## 💡 Design Decisions

* **Center-based detection**: Using the average color of a small region rather than a single pixel reduces noise and improves accuracy.
* **CSV dataset approach**: Allows easy expansion and editing of the color database without modifying the code.
* **OpenCV-only interface**: Avoids dependencies on GUI frameworks like Tkinter, keeping the app lightweight and portable.
* **Alpha channel support**: Properly handles PNG overlays with transparency, improving the visual appeal.

---

## 🔮 Future Improvements

* Mouse-click color detection from any point on the screen
* Export functionality to save detected colors as palettes
* Multi-region or grid-based detection
* Web version using JavaScript and WebRTC

---

## ✅ Conclusion

This Real-Time Color Detector is a compact yet powerful application that brings computer vision concepts to life in an engaging and interactive way. Developed as part of the CS50 Final Project, it combines practical programming, real-world input processing, and clean UI rendering using Python and OpenCV.

It is a proud demonstration of how programming skills acquired in CS50 can be applied to build functional, creative, and visually appealing projects.

---
