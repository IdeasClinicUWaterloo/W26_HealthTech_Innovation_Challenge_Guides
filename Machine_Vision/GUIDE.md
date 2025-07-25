# Machine Vision: Integrating Machine Learning with OpenCV and MediaPipe
## Table of Contents
1. [Introduction](1.)
2. [Installation](2.)

## 1. Introduction
This guide will walk you through a machine learning (ML) model that is trained to identify exercises in combination with Google's Mediapipe and OpenCV. This ML model is an LSTM (long short-term memory) model, which can make predictions from sequences of data. 

## 2. Installation
2.1 Download Python (version 3.9 - 3.12)
* Currently, Mediapipe is only supported on python versions 3.9 to 3.12.
* You can download a compatible version of python [here](https://www.python.org/downloads/).

2.2 Creating Virtual Environments
A Python virtual environment (venv) is a self-contained directory that allows you to install packages and dependencies for a specific project without affecting the global Python installation or other projects.
1. Download the starter code contained in this folder (it is recommended you use git to download and share these files)
2. Open a terminal in vscode and use `cd *directory*` to navigate to the directory where you stored the code you downloaded in step 1
3. Create a venv:
   * Enter `python -m venv *name-of-your-venv*` in the same terminal. This should create a new folder with the name of your venv under the "Computer Vision" directory
4. Activate the venv:
   * for Mac/Linux users: `source ./name-of-your-venv/bin/activate`
   * for Windows users: `name-of-your-venv/Scripts/activate`
   * When prompted, type R and then enter to run once
   * you should now see `(name-of-your-venv)` being appended to your input prompt, indicating that you have activated your venv

2.3 Install Python Libraries
OpenCV: For handling image and video processing.
MediaPipe Solutions: For real-time computer vision tasks such as pose estimation, hand tracking, and face detection.
Numpy: For matrix and array operations.
Tensorflow:

You can use the `requirements.txt` file in this folder and run this one-line command in the terminal: `pip install -r requirements.txt`

## 3. Computer Vision Basics
Refer to the github page from the [Winter 2025 HealthTech Inovation Challenge](https://github.com/IdeasClinicUWaterloo/W25_HealthTech_Innovation_Challenge_Guides/blob/4b4f367f191157d8503dc93de521de78b7b8d533/Computer_Vision/GUIDE.md) for a beginners guide to OpenCV and Mediapipe

## 4. Machine Learning
