# Machine Vision: Integrating Machine Learning with OpenCV and MediaPipe
## Table of Contents
### 1. [Introduction](#1)
### 2. [Installation](#2)
   - 2.1. [Download Python](#2.1)
   - 2.2. [Creating Virtual Environments](#2.2)
   - 2.3. [Install Python Libraries](#2.3)
   - 2.4. [Jupyter Notebook](#2.4)
### 3. [Computer Vision Basics](#3)
### 4. [Machine Learning](#4)
   - 4.1 [Running the Model](#4.1)

<h2 id = '1'> 1. Introduction</h2>

This guide will walk you through a machine learning (ML) model that you can train to identify exercises in combination with Google's Mediapipe and OpenCV. This ML model is an LSTM (long short-term memory) model, which can make predictions from sequences of data. 

<h2 id = '2'> 2. Installation</h2>

<h3 id = '2.1'> 2.1 Download Python (version 3.9 - 3.11)</h3>

* Currently, Mediapipe is only supported on python versions 3.9 to 3.12.
* You can download a compatible version of python [here](https://www.python.org/downloads/).

<h3 id = '2.2'> 2.2 Creating Virtual Environments</h3>

A Python virtual environment (venv) is a self-contained directory that allows you to install packages and dependencies for a specific project without affecting the global Python installation or other projects.

1. Download the starter code contained in this folder (it is recommended you use git to download and share these files)
2. Open a terminal in vscode and use `cd *directory*` to navigate to the directory where you stored the code you downloaded in step 1
3. Create a venv:
   - Enter `python -m venv *name-of-your-venv*` in the same terminal. This should create a new folder with the name of your venv under the "Computer Vision" directory
4. Activate the venv:
   - You might get a prompt in VSCode after creating the venv, asking if you want to use the new venv for your project. If you select yes, you don't need to do the following.
   - for Mac/Linux users: `source ./name-of-your-venv/bin/activate`
   - for Windows users: `name-of-your-venv/Scripts/activate`
   - When prompted, type R and then enter to run once
   - you should now see `(name-of-your-venv)` being appended to your input prompt, indicating that you have activated your venv

<h3 id = '2.3'> 2..3 Install Python Libraries</h3>

- **OpenCV**: For handling image and video processing.
- **MediaPipe Solutions**: For real-time computer vision tasks such as pose estimation, hand tracking, and face detection.
- **Numpy**: For matrix and array operations.
- **Tensorflow**: For building and training machine learning models (specifically deep learning).

You can use the `requirements.txt` file in this folder and run this one-line command in the terminal: `pip install -r requirements.txt`

<h3 id = '2.4'> 2.4 Jupyter Notebook</h3>

Jupyter Notebook is used for machine learning becuase it provides an interactive environment where you can write and run code in small chunks, visualize data and document your process all in one location.
- Follow this guide for using [Jupyter Notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) in VSCode


<h2 id = '3'> 3. Computer Vision Basics</h2>

Refer to the tech stack from the Winter 2025 [Health Tech Innovation Challenge](https://github.com/IdeasClinicUWaterloo/W25_HealthTech_Innovation_Challenge_Guides/tree/4b4f367f191157d8503dc93de521de78b7b8d533/Computer_Vision) for a beginners guide to OpenCV and Mediapipe.

<h2 id = '4'> 4. Machine Learning</h2>

Machine Learning (ML) is a branch of AI that teaches systems to think and understand like humans by learning from the data.
- Trained ML models must be integrated into an application to make its predictions accessible.
- The model provided in this folder `exercise_classifier.ipynb` can be trained to recognize three exercises using your webcam: bicep curls, shoulder presses, and squats.
   - Follow the steps below to learn more about using this model for your projects.

<h3 id = '4.1'> 4.1 Running the Model</h3>

There is a ML workflow which guides development and deployment of ML models, consisting of various steps. Here are some of the steps which you will be concerned with regarding this model.
1. Data Collection
   - There are already some videos in the [data](https://github.com/IdeasClinicUWaterloo/W26_HealthTech_Innovation_Challenge_Guides/tree/main/Machine_Vision/data) folder/directory for the three exercises.
   - You can stick with these exercises, or you can choose different exercises.
   - There is a list of exercises that CCCare typically "prescribes" participants (put file location here), you are free to choose exercises from that list [here](https://github.com/IdeasClinicUWaterloo/W26_HealthTech_Innovation_Challenge_Guides/blob/main/Machine_Vision/Sample_Exercises_and_Categories.pdf).
   - Requirements if you are selecting your own data:
        - Videos must be .MP4 format.
        - Make sure that the video shows at least **two** repetitions of the exercise.
        - Ensure that you get videos of the exercise from various angles (not just front facing videos).
2. Data Cleaning and Preprocessing
   - Data cleaning: addressing issues such as missing values, outliers and inconsistencies.
   - Data preprocessing: standardizing formats, scaling data, encoding categorical variables for consistency.
        - The data should be formatted as sequences of mediapipe keypoint coordinates (x, y, z positions) extracted for each exercise.
3. Model Selection
   - This classifier is a long short-term memory (LSTM) model.
   - LSTMs are mainly used in cases where remembering previous information is important, like analyzing sequences of body movements.
4. Model Training
   - Walk through section 5 and 6 in the [exercise classifier notebook](https://github.com/IdeasClinicUWaterloo/W26_HealthTech_Innovation_Challenge_Guides/blob/main/Machine_Vision/exercise_classifier.ipynb).
5. Model Evaluation and Tuning
    - This involves allowing the model to make predictions using the test dataset, and evaluating how well the model performs (refer to section 9 of the exercise classifier notebook).
6. Model Deployment
   - There are various methods to deploy your model once it is finished.
   - Offline:
        - Good for running predictions on videos post-recording
        - Save the trained model (.h5 file)
        - Create a script/function
        - Ensure that the preprocessing and sequence formatting is the same as used to train the model
   - Web or Desktop App:
        - Good for letting other use it via a GUI
        - You can wrap the model in an app using Streamlit or Flask/FastAPI
        - Tutorial for [Streamlit](https://www.geeksforgeeks.org/python/a-beginners-guide-to-streamlit/)
        - Tutorial for [FastAPI](https://www.geeksforgeeks.org/python/fastapi-introduction/)
   - There are many more ways to make use of your ML model, be as creative as you want!

For more information on the machine learning workflow check out this [link](https://www.geeksforgeeks.org/machine-learning/machine-learning-lifecycle/)!




