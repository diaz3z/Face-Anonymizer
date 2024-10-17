# Face Blurring with Mediapipe and Haar Cascade Classifier

This repository contains two implementations for blurring faces in a video stream from the webcam. The first method uses Mediapipe for face detection, and the second method leverages Haar Cascade Classifier. Both implementations apply Gaussian blur to the detected faces in real-time.

## Table of Contents

- Introduction
- Requirements
- Installation
- Usage
  - Mediapipe Implementation
  - Haar Cascade Classifier Implementation
- Example Output

## Introduction

Blurring faces in videos is a common task in privacy protection, video processing, and face anonymization applications. This repository demonstrates two different approaches to accomplish this:

1. Mediapipe: A machine learning-based face detection model that accurately detects facial landmarks and bounding boxes.
2. Haar Cascade Classifier: A classical computer vision method that uses pre-trained models to detect faces based on Haar features.
 

Both implementations use OpenCV for handling video frames and applying Gaussian blur to detected faces.

## Requirements
- Python 3.x
- OpenCV (opencv-python)
- Mediapipe (for the first implementation)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/diaz3z/Face-Anonymizer.git

```
2. Install the required libraries:
```bash
pip install opencv-python mediapipe numpy

```

## Usage

You can run both implementations using your webcam.

## Mediapipe Implementation

This method uses Mediapipe to detect faces and blur them using Gaussian blur within the detected rectangular bounding boxes.

1. Run the script:
```bash
python UsingMediapipe.py

```
## Example Output

This scripts will open a window displaying your webcam feed, where any detected faces will be blurred. You can exit the program by pressing the "q" key.

![Media Pipe](https://github.com/user-attachments/assets/b661d9f6-1286-426a-b5c5-04c463190a90)

![Media Pipe](https://github.com/user-attachments/assets/c618dc26-9687-49f5-9b3f-94356726943b)

## Haar Cascade Classifier Implementation

This method uses Haar Cascade Classifier to detect faces and apply Gaussian blur to the detected regions.

1. Run the script:
```bash
python haarcascadeclassifier.py
```

## Example Output

This scripts will open a window displaying your webcam feed, where any detected faces will be blurred. You can exit the program by pressing the "q" key.

![Harcascade Classifier](https://github.com/user-attachments/assets/667527f7-689d-454c-8837-718250b9ba8c)

![Haarcascade Classifier](https://github.com/user-attachments/assets/1db64317-b4af-4381-a7e8-fbb28edaaf24)




## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/diaz3z/Face-Anonymizer/issues) if you want to contribute.

