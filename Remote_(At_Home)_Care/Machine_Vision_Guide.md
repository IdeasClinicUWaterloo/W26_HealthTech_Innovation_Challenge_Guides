# Machine Vision: Integrating Machine Learning with OpenCV and MediaPipe
## Table of Contents
### 1. [Introduction](#1)
### 2. [Installation](#2)
   - 2.1. [Download Python](#2.1)
   - 2.2. [Creating Virtual Environments](#2.2)
   - 2.3. [Install Python Libraries](#2.3)
   - 2.4. [Jupyter Notebook](#2.4)
### 3. [Getting Started with OpenCV](#3)
 - 3.1: [OpenCV Basic Features](#3.1)
 - 3.2: [OpenCV Basic Implementations](#3.2)
### 4. [Health Related Application](#4)
 - 4.1: [Pose Detection Library Features](#4.1)

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

Jupyter Notebook is used for machine learning because it provides an interactive environment where you can write and run code in small chunks, visualize data and document your process all in one location.
- Follow this guide for using [Jupyter Notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) in VSCode

<h2 id='3'>3: Getting Started with OpenCV</h2>

<h3 id='3.1'>3.1: Basic OpenCV Features</h3>

Here are some important concepts and features of OpenCV that beginners should know:

**Image Channels**
- **Grayscale images** have 1 channel that represents the intensity level
    - <img src='images/gray_scale.png' height=200>
    - the smaller the number is, the darker the pixel
- **Colour images** have 3 channels (Red, Green, Blue)
    - <img src='images/rgb_wheel.png' width=450>

**BGR vs RGB Color Format**
- OpenCV processes images in **BGR** format, not the typical **RGB** format used in other image processing libraries. The difference is in the order of the color channels
- This means that when OpenCV reads an image, the pixel values will be ordered as BGR. If you need to convert from BGR to RGB, you can do so like this:
    ```
    # Convert BGR image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    ```
**Working with Arrays**
- OpenCV images are stored as **NumPy arrays**. This means you can use NumPy's powerful indexing and slicing features to manipulate image data directly:
    ```
    # Access the pixel at row 50, column 100
    pixel = image[50, 100]

    # Modify the pixel value (in BGR format)
    image[50, 100] = [255, 0, 0]  # Set to blue
    ```

<h3 id='3.2'>3.2: OpenCV Basic Implementations</h3>


**[Reading and Displaying an Image](cv_examples/read_show_image.py)** (These titles are clickable)

 - Using the [```cv2.imread()```](https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/) and [```cv2.imshow()```](https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/) method.
 - Your first place to start! Now you can display an image from a file with openCV!

**[Converting Image to Grayscale](cv_examples/convert_to_grayscale.py)**
 - Using the [```cv2.cvtColor()```](https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/) method to convert a bgr coloured image to grayscale.
 - Since grayscale images have only one colour channel, their file size is much smaller than coloured images. This is a great option when you want to optimize the computation efficiency of an image/video where you don't need the colour information. 

**[Resize Image](cv_examples/resize_image.py)**
 - Using the [```cv2.resize()```](https://www.geeksforgeeks.org/image-resizing-using-opencv-python/) method.

**[Capture Video from Webcam](cv_examples/capture_from_webcam.py)**
 - Use the [```cv2.VideoCapture()```](https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/) method with parameter 0 to open the built-in webcam of your laptop
 - Call the ```read()``` method on the VideoCapture object in a loop to process it frame by frame

 **[Read Video from File](cv_examples/read_video_from_file.py)**
 - Same as the above, but replace the parameter in the ```VideoCapture()``` method with the path to the file.

**[Edge Detection](cv_examples/detect_edge.py)**
 - Edge detection highlights boundaries within an image where there is a sharp change in brightness. This is used in various applications such as object recognition, image segmentation, motion detection, etc.
 - This code demonstrates the most popular edge detection algorithm, the Canny algorithm with the [```cv2.Canny()```](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html) method. 

**For more tutorials, check out the [official OpenCV-Python Tutorials page](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)**

<h2 id = '5'> 4. Machine Learning</h2>

Machine Learning (ML) is a branch of AI that teaches systems to think and understand like humans by learning from the data.
- Trained ML models must be integrated into an application to make its predictions accessible.
- The model provided in this folder `exercise_classifier.ipynb` can be trained to recognize three exercises using your webcam: bicep curls, shoulder presses, and squats.
   - Follow the steps below to learn more about using this model for your projects.

<h3 id = '5.1'> 4.1 Running the Model</h3>

There is a ML workflow which guides development and deployment of ML models, consisting of various steps. Here are some of the steps which you will be concerned with regarding this model.
1. Data Collection
   - There are already some videos in the [data](./data) folder/directory for the three exercises.
     <!-- (https://github.com/IdeasClinicUWaterloo/W26_HealthTech_Innovation_Challenge_Guides/tree/main/Machine_Vision/data) --> 
   - You can stick with these exercises, or you can choose different exercises.
   - There is a list of exercises that CCCare typically "prescribes" participants (put file location here), you are free to choose exercises from that list [here](./Sample_Exercises_and_Categories.pdf).
   - <!-- (https://github.com/IdeasClinicUWaterloo/W26_HealthTech_Innovation_Challenge_Guides/blob/main/Machine_Vision/Sample_Exercises_and_Categories.pdf). -->
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
     <!-- (https://github.com/IdeasClinicUWaterloo/W26_HealthTech_Innovation_Challenge_Guides/blob/main/Machine_Vision/exercise_classifier.ipynb). -->

<h2 id='4'>4: Health Related Application</h2>

 - Mediapipe provides libraries for a great variety of tasks that you can choose from depending on the goal of your project. You can find a web-based demo of these library utilities on the [MediaPipe Studio site](https://mediapipe-studio.webapps.google.com/demo/pose_landmarker).

    - Use your webcam as the input and tweak the parameter values to have some fun with it!

 - This guide will only go over the basics of the **Pose Detection** library as it may be the most relevant to your problem space.

 <h3 id='4.1'>4.1: Library Features</h3>

 - The Mediapipe Pose Detection library tracks the location of 33 body landmarks.
    - <img src='https://ai.google.dev/static/mediapipe/images/solutions/pose_landmarks_index.png' height=500px>

 - Each landmark contains the x, y, and z coordinates, as well as the visibility of the landmark
    ```bash
        # print an example landmark

        x: 0.401668698
        y: 0.664962471
        z: -0.16625689
        visibility: 0.998352528
    ```
    - ```x``` and ```y``` are normalized coordinates representing the 2D position of the landmark in the image 
        - Ranging from 0 to 1, relative to the image dimensions.
    - ```z``` is a **relative** depth coordinate representing the distance of the landmark from the camera.
        - You are likely not working with a depth camera here, so the ```z``` value is not a real "measured" value. It is rather estimated by the Mediapipe model. 
    - ```visibility``` is a confidence score indicating how likely it is that the landmark is visible or correctly detected. 
        - Ranges from 0.0 to 1.0. 
            - 1.0 == high confidence
            - 0.0 == low confidence
    - Let's say the program can only view the upper body of a person to detect their pose, like this:

        <img src='images/upper_body_pose.png' height=200px>\
    the pose detection method will still, by default, return the ```x y z``` coordinates of the lower body landmarks.
        - The visible upper body landmarks will have very **high** ```visibility``` values
        - the knee joints and ankle joint will have extremely **low** ```visibility``` values.
        - the hip joints will each have a **median** ```visibility```value because the model can estimate the hip joint coordinates with higher confidence based on the visible upper body landmarks.

 <h3 id='4.2'>4.2: Library Basic Implementations</h3>

**[Pose Detection on an Image](mp_examples/draw_landmarks_on_image.py)**
 - Visit this code snippet for the simplest implementation that detects and draws the landmarks on an image. 
 - Think about how you would:
    1. Get the ```x y z``` coordinates and the ```visibility``` value of a specific landmark.
    2. Change the colour and thickness of the landmark labels and the connection lines.
    3. Calculate the angle at the left elbow joint.

**[Pose Detection on LiveStream](mp_examples/draw_landmarks_on_live_stream.py)**
 - Now that you know how to process one image, processing a video or livestream is easy since a video is just numerous frames of an image. 
 - Check out this code on how that is done, then, you are ready to start your own journey of using CV and Mediapipe to complete your own project!

<h3 id= '4.3'>4.3: Resources to help you</h3>
You can find videos for your data at [Kaggle](https://www.kaggle.com/) or use this [dataset from Kaggle](https://www.kaggle.com/datasets/hasyimabdillah/workoutfitness-video).
Here is an application of using MediaPipe in the [JupyterNotebook File](Remote_(At_Home)_Care/exercise_classifier.ipynb)
 ---

 Good Luck!


