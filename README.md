<div align="center">

# 🎨 Real-Time Color Detector

**Point your webcam at anything and get its color name, RGB and HEX, live.**

Built with Python and OpenCV · Final project for [Harvard CS50x](https://cs50.harvard.edu/x/)

[![Python](https://img.shields.io/badge/Python_3-100f0d?style=for-the-badge&logo=python&logoColor=d9a05b)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-100f0d?style=for-the-badge&logo=opencv&logoColor=d9a05b)](https://opencv.org/)
[![Pandas](https://img.shields.io/badge/Pandas-100f0d?style=for-the-badge&logo=pandas&logoColor=d9a05b)](https://pandas.pydata.org/)
[![CS50x](https://img.shields.io/badge/CS50x-Final_Project-100f0d?style=for-the-badge&logo=harvard&logoColor=d9a05b&labelColor=2b2117)](https://certificates.cs50.io/81532b44-9b96-4a68-bf98-cd162cff7011.pdf?size=letter)

<br>

<!-- To use a GIF: record the window (ScreenToGif works well), save it as images/demo.gif and swap the src below. -->
<img src="images/final-project-havard.png" alt="Color detector identifying the red face of a Rubik's cube: Red, RGB(234, 9, 3), HEX #EA0903" width="820"/>

<br><br>

[![Watch the demo on YouTube](https://img.shields.io/badge/%E2%96%B6%20Watch%20the%20demo-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white&labelColor=100f0d)](https://www.youtube.com/watch?v=SoSC_lMgSrE)

</div>

<br>

## ✨ Features

| | |
|---|---|
| 📷 **Live webcam feed** | Reads every frame in real time, no photo upload needed |
| 🎯 **Center sampling** | Averages a 60×60 px area instead of a single pixel, so noise doesn't flip the result |
| 🌈 **Name + RGB + HEX** | Matches the nearest of 141 named colors and shows all three values on screen |
| 🧠 **Smart contrast** | Text switches between black and white depending on how bright the color is |
| 🖼️ **Clean overlay** | Translucent color panel, swatch preview and PNG logo with real alpha blending |

<br>

## 🚀 Quick start

```bash
git clone https://github.com/vanngilha/color-detector.git
cd color-detector
pip install -r requirements.txt
python color_detector.py
```

A window opens with your webcam. Put something in the white square and the color shows up on top. Press **Esc** to quit.

> [!TIP]
> No webcam on your PC? Apps like **DroidCam** turn your phone into one. That's how the screenshot above was taken.

> [!NOTE]
> Online IDEs (like the CS50 codespace) can't reach your webcam. Run it locally in VS Code or a terminal.

<br>

## ⚙️ How it works

```mermaid
flowchart LR
    A[Webcam frame] --> B[60×60 center crop]
    B --> C[Average B, G, R]
    C --> D[Nearest color in colors.csv<br/>Manhattan distance]
    D --> E[Overlay name, RGB, HEX]
    E --> A

    classDef step fill:#100f0d,stroke:#d9a05b,color:#ffffff
    class A,B,C,D,E step
```

1. Each frame is captured with `cv2.VideoCapture`.
2. The square in the middle of the frame is averaged into one color.
3. That color is compared with every row in `colors.csv` using the sum of the absolute differences in R, G and B. The smallest difference wins.
4. The name, RGB and HEX are drawn on the frame with OpenCV, and the loop repeats.

<br>

## 📁 Project structure

```
color-detector/
├── color_detector.py   # capture, color matching and drawing
├── colors.csv          # 141 named colors with HEX and RGB
├── requirements.txt    # opencv-python, pandas
├── assets/
│   └── harvard_logo.png
└── images/
    └── final-project-havard.png
```

Want more colors? Add a row to `colors.csv` (`color_name,hex,R,G,B`). No code changes needed.

<br>

## 🔮 Roadmap

- [ ] Click anywhere on the video to pick that point's color
- [ ] Save detected colors as a palette (PNG / JSON)
- [ ] Grid mode to detect several regions at once
- [ ] Web version in JavaScript with WebRTC

Ideas and PRs are welcome. Open an [issue](https://github.com/vanngilha/color-detector/issues) and let's talk.

<br>

<div align="center">

**If this project helped you or you just liked it, leave a ⭐. It really helps!**

Made by [Christopher Oliveira](https://www.chrisoliveira.dev) · [LinkedIn](https://www.linkedin.com/in/chriisoliveira)

</div>
