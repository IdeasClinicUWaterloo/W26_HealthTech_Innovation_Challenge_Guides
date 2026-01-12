# Machine Vision Guide
## Table of Contents
### 1. [Introduction](#1)
### 2. [Terminology](#2)
### 3. [Setting up your System](#3)
   - 3.1. [Install Python Libraries](#3.1)
   - 3.2. [Create a Jupyter Notebook](#3.2)
   - 3.3. [Set up a Computer Vision System](#3.3)
   - 3.4. [Machine Learning](#3.4)
   - 3.5. [Choose a Machine Learning Solution](#3.5)
   
<h2 id = '1'> 1. Introduction</h2>

This guide walks you through the steps required to set up a machine vision system. By combining machine learning (ML) with computer vision, you'll be able to track and respond to specific activities or the presence or absence of certain objects. Typical applications are quality control, automation, inspection, and process optimization. If you've never worked with machine learning before, check out this [Getting_Started_with_Machine_Learning](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Machine_Learning/Getting_Started_with_Machine_Learning.md) guide. It will introduce you to machine learning (ML) and explain the workflow that guides development and deployment of ML models.

<h2 id = '2'> 2. Terminology</h2>

**Computer Vision**: a branch of AI that lets machines capture and interpret real-world visual data (images or video)

**Jupyter Notebook**: an open-source web application to create and share documents that contain live code, equations, visualizations, and narrative text. It supports Python, R, Julia, Ruby, Scala, and Node.js languages

**Machine Learning (ML)**:  a branch of AI that teaches systems to think and understand like humans by learning from data

**Machine-Learning Pipeline**: a structured workflow that automates the process of building, training, and deploying machine learning models

**MediaPipe**: Google's open-source framework for building and deploying machine-learning pipelines

**OpenCV**: an open-source software library for computer vision and machine learning (short for Open Source Computer Vision library)

**Python**: an easy-to-use programming environment for general purpose coding

<h2 id = '3'> 3. Setting up your System</h2>

This machine learning system will be created in Python.  If you haven't used Python before or don't have it installed on your computer, please check out this [Getting Started with Python](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Python/Getting_Started_with_Python.md) guide. It will guide you through the steps required to install and run Python. Make sure to install a Python **version between 3.9 - 3.11** for this project.

<h3 id = '3.1'> 3.1 Install Python Libraries</h3>
You'll need to install the following libraries for your machine vision system:

 - **OpenCV**: For handling image and video processing
- **MediaPipe Solutions**: For real-time computer vision tasks such as pose estimation, hand tracking, and face detection
- **NumPy**: For matrix and array operations
- **Tensorflow**: For building and training machine learning models (specifically deep learning)

You can download the `requirements.txt` file in this folder and run this one-line command in the terminal: `pip install -r requirements.txt

<h3 id = '3.2'> 3.2 Create a Jupyter Notebook</h3>

Jupyter Notebook is often used for machine learning applications because it provides an interactive environment where you can write and run code in small chunks, visualize data and document your process all in one location. 

If you haven't used Jupyter Notebook before, please check out this [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) site on setting up and using it.

<h3 id = '3.3'> 3.3. Set up a Computer Vision System</h2>

If you've never worked with a computer vision system before, please check out this [Getting Started with OpenCV](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Machine_Learning/Machine_Vision/Getting_Started_with_OpenCV.md) guide. It will introduce you to OpenCV, short for **Open Source Computer Vision Library**, which is an open-source software library for computer vision and machine learning. 

<h3 id = '3.4'> 3.4. Machine Learning</h3>

If you've never worked with machine learning before, check out this [Getting_Started_with_Machine_Learning](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Machine_Learning/Getting_Started_with_Machine_Learning.md) guide. It will introduce you to machine learning (ML) and explain the workflow that guides development and deployment of ML models.  

<h3 id = '3.5'> 3.5. Choose a Machine Learning Solution</h2>

Then you'll want to explore the resources in the [MediaPipe Studio](https://mediapipe-studio.webapps.google.com/home). Here you can choose from vision-related solutions such as object detection, image classification and pose detection, text-related solutions such as text classification and language detection, or audio classification.

- Check out this [Health-Related Application](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Machine_Learning/Machine_Vision/Health_Related_Application.md) that uses MediaPipe's pose detection library.

