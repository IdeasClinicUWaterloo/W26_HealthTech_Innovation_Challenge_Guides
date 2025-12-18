# Machine Vision Guide
## Table of Contents
### 1. [Introduction](#1)
### 2. [Terminology](#2)
### 3. [Setting up your System](#3)
   - 3.1. [Install Python Libraries](#3.1)
   - 3.2. [Create a Jupyter Notebook](#3.2)
   - 3.3. [Set up a Computer Vision System](#3.3)
   - 3.4. [Machine Learning](#3.4) <!--        - 3.4.1. [Running the Model](#3.4.1) -->
   - 3.5. [Choose a Machine Learning Solution](#3.5)
<!-- ### 4. [Machine Learning](#4)
   - 4.1 [Running the Model](#4.1) -->
   
<h2 id = '1'> 1. Introduction</h2>

This guide walks you through the steps required to set up a machine vision system. By combining machine learning (ML) with computer vision, you'll be able to track and respond to specific activities or the presence or absence of certain objects. Typical applications are quality control, automation, inspection, and process optimization. If you've never worked with machine learning before, check out this [Getting_Started_with_Machine_Learning.md](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/IdeasClinicUWaterloo-patch-1/Machine_Learning/Getting_Started_with_Machine_Learning.md) guide. It will introduce you to machine learning (ML) and explain the workflow that guides development and deployment of ML models.


<h2 id = '2'> 2. Terminology</h2>

**Computer Vision**: a branch of AI that lets machines capture and interpret real-world visual data (images or video)

**Jupyter Notebook**: an open-source web application to create and share documents that contain live code, equations, visualizations, and narrative text. It supports Python, R, Julia, Ruby, Scala, and Node.js languages

**Machine Learning (ML)**:  a branch of AI that teaches systems to think and understand like humans by learning from data

**Machine-Learning Pipeline**: a structured workflow that automates the process of building, training, and deploying machine learning models

**MediaPipe**: Google's open-source framework for building and deploying machine-learning pipelines

**OpenCV**: an open-source software library for computer vision and machine learning (short for Open Source Computer Vision library)

**Python**: an easy-to-use programming environment for general purpose coding

<h2 id = '3'> 3. Setting up your System</h2>

This machine learning system will be created in Python.  If you haven't used Python before or don't have it installed on your computer, please check out this [Getting Started with Python](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/IdeasClinicUWaterloo-patch-1/Python/Getting_Started_with_Python.md) guide. It will guide you through the steps required to install and run Python. Make sure to install a Python **version between 3.9 - 3.11** for this project.

<h3 id = '3.1'> 3.1 Install Python Libraries</h3>
You'll need to install the following libraries for your machine vision system:

 - **OpenCV**: For handling image and video processing
- **MediaPipe Solutions**: For real-time computer vision tasks such as pose estimation, hand tracking, and face detection
- **NumPy**: For matrix and array operations
- **Tensorflow**: For building and training machine learning models (specifically deep learning)

You can use the `requirements.txt` file in this folder and run this one-line command in the terminal: `pip install -r requirements.txt

<h3 id = '3.2'> 3.2 Create a Jupyter Notebook</h3>

Jupyter Notebook is often used for machine learning applications because it provides an interactive environment where you can write and run code in small chunks, visualize data and document your process all in one location. 

If you haven't used Jupyter Notebook before, please check out this [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) site on setting up and using it.

<h3 id = '3.3'> 3.3. Set up a Computer Vision System</h2>

If you've never worked with a computer vision system before, please check out this [Getting Started with OpenCV](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/IdeasClinicUWaterloo-patch-1/Machine_Learning/Getting_Started_with_OpenCV.md) guide. It will introduce you to OpenCV, short for **Open Source Computer Vision Library**, which is an open-source software library for computer vision and machine learning. 

<h3 id = '3.4'> 3.4. Machine Learning</h3>

Machine Learning (ML) is a branch of AI that teaches systems to think and understand like humans by learning from the data.
- Trained ML models must be integrated into an application to make its predictions accessible.
- The model provided in this folder `exercise_classifier.ipynb` can be trained to recognize three exercises using your webcam: bicep curls, shoulder presses, and squats.
   - Follow the steps below to learn more about using this model for your projects.

<h4 id = '3.4.1'> <!-- 3.4.1 --> Running the Model</h4>

There is a ML workflow which guides development and deployment of ML models, consisting of various steps. Here are some of the steps which you will be concerned with regarding this model.
1. Data Collection
   - There are already some videos in the [data](./data) folder/directory for the three exercises.
   - You can stick with these exercises, or you can choose different exercises.
   - There is a list of exercises that CCCARE typically "prescribes" participants (put file location here), you are free to choose exercises from that list [here](./Sample_Exercises_and_Categories.pdf).
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
   - Walk through section 5 and 6 in the [exercise classifier notebook](./exercise_classifier.ipynb).
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

You can find videos for your data at [Kaggle](https://www.kaggle.com/) or use this [dataset from Kaggle](https://www.kaggle.com/datasets/hasyimabdillah/workoutfitness-video).

<h3 id = '3.5'> 3.5. Choose a Machine Learning Solution</h2>

Then you'll want to explore the resources in the [MediaPipe Studio](https://mediapipe-studio.webapps.google.com/home). Here you can choose from vision-related solutions such as object detection, image classification and pose detection, text-related solutions such as text classification and language detection, or audio classification.

- Check out this [Health-Related Application](./Health_Related_Application.md) that uses MediaPipe's pose detection library.

