
# Online Image Editor - CS50x Final Project

Hello, I'm Hadi Safararab. I participated in the CS50x 2023 course, and today, I present my final project, an "Online Image Editor" website. This website is written in Python and Flask. For designing t he web pages, I used HTML, Bootstrap, and JavaScript. The project consists of two main pages: `index.html` as the landing page and `display.html` to showcase the edited images. Additionally, two Python files are included: `app.py` serves as the main file to run the Flask server and define the routes, and `functions.py` contains image editing functions called by `app.py`.

## Project Overview

The main functionality of this project is implemented on the `index.html` page. A form is provided to the user, prompting them to upload an image and select an editing option among "Remove Background," "Find Face," "Grayscale," and "Canny." After choosing, the user clicks the submit button.

Upon clicking submit, a POST request is sent to the server at the `/upload` route. In the `app.py` file, a route is defined to handle the form with the POST method, storing the uploaded image in the variable `uploaded_file`. The selected option is also saved using `request.form.getlist('options')` in the variable `selected_options`. The uploaded file is then saved in the `/static/uploads` directory.

Next, based on the user's selected option, conditional statements determine which specific function to apply. For instance, the `find_face()` function is used for face detection, and `rmbg()` is used for background removal. These functions are defined in the `functions.py` file and imported into the main file.

After applying the necessary edits, the path and filename of the output file saved in the `/static/export` directory are passed to the `display.html` page for the user to view. A route `@app.route('/display/<filename>')` is created to send the filename as input to the `display.html` page.

## Displaying Edited Image

In `display.html`, an `img` tag is used to display the edited image by concatenating the given filename with the pre-defined path. This generates the exact image address for visualization.

Feel free to explore the [Online Image Editor](#) and experiment with different image editing options!

# Project Components

Let me explain a bit about the components that constitute this project. As mentioned, this project consists of three main sections.

### 1. Python Virtual Environment

The first section is the Python Virtual Environment, which is a virtual environment that allows you to create a separate and isolated environment for running Python programs. This environment prevents dependencies and packages of one project from conflicting with others. It also enables you to install editors and tools separately for each project. All installed packages for this project are saved in the `requirements.txt` file using the command `pip freeze > requirements.txt`.

### 2. app.py File

The `app.py` file serves as the main file to specify the path and execute the Flask web service. Below, each part of this file will be explained:

#### Import Libraries

```python
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageOps
import os
from functions import rmbg, rot, find_face, Blur, Gray, Canny

- `Flask`: Used to create a web application.
- `render_template`: Sends and displays templates.
- `request`: Retrieves data sent from forms.
- `redirect` and `url_for`: Used for page redirection.
- `PIL`: Used for working with images.
- `os`: Used for performing system operations like file storage and retrieval.
- `functions`: A module containing image editing functions.

#### Create an Instance of the Flask Class

```python
app = Flask(__name__)
```

#### Configuration Settings for File Upload

```python
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
```

- `UPLOAD_FOLDER`: The path to store uploaded files.
- `ALLOWED_EXTENSIONS`: Allowed file types for upload.

#### Function to Check Allowed File Type

```python
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
```

This function checks whether the uploaded file type is allowed or not.

#### Home Page Route

```python
@app.route('/')
def index():
    return render_template('index.html')
```

Displays the home page to the user.

#### File Upload and Image Editing Route

```python
@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['image']
    selected_options = request.form.getlist('options')

    if uploaded_file:
        uploaded_file.save('static/uploads/' + uploaded_file.filename)

    if selected == "RemoveBG":
        # ...
        return redirect(url_for('display', filename=uploaded_file.filename.split('.')[0]+"_rmbg.png"))
    # (Other options follow similarly)

    return "File uploaded and form submitted successfully!"
```

#### Display Edited Image Route

```python
@app.route('/display/<filename>')
def display(filename):
    return render_template('display.html', filename=filename)
```

Displays the edited image to the user.

#### Run the Application

```python
if __name__ == '__main__':
    app.run(debug=True)
```

Runs the program in debug mode.

### 3. functions.py File

In this file, various libraries are used to edit images. One of the most important ones is OpenCV. OpenCV is an open-source library that is commonly used for image and video processing. It supports various programming languages, including Python, C++, and Java. It is recognized as a powerful tool in the fields of computer vision and image processing.

Additionally, the `mediapipe` library is utilized. This is an open-source library from Google that provides tools and algorithms for machine vision, enabling the detection and processing of various body and face parts. It supports Python and is used for projects requiring face detection, hand detection, detection of different body parts, and other machine vision-related tasks.

The functions in this code provide various image editing capabilities. Below are explanations for each function:

#### 1. `rmbg` Function (Remove Background)

- Input: Image and filename.
- Output: Output file path.
- This function uses the `rembg` library to remove the background from the input image and saves the resulting image at the specified path.

#### 2. `rot` Function (Rotate 90 Degrees)

- Input: Image filename.
- Output: Output file path.
- This function rotates the image 90 degrees around the vertical axis and saves the resulting image at the specified path.

#### 3. `Gray` Function (Convert to Grayscale)

- Input: Image filename.
- Output: Output file path.
- This function converts the image to grayscale and saves the resulting image at the specified path.

#### 4. `Blur` Function (Apply Blur Effect)

- Input: Image filename.
- Output: Output file path.
- This function applies a blur effect to the image and saves the resulting image at the specified path.

#### 5. `Canny` Function (Edge Detection using Canny Algorithm)

- Input: Image filename.
- Output: Output file path.
- This function applies the Canny algorithm for edge detection to the image and saves the resulting image at the specified path.

#### 6. `find_face` Function (Face Detection using MediaPipe)

- Input: Image filename.
- Output: Output file path.
- This function uses the `mediapipe` library to detect faces in the image. It adds key points and a bounding rectangle to the image and saves the resulting image at the specified path.

It's worth noting that this code uses some well-known libraries such as OpenCV, Pillow (PIL), and Mediapipe for image processing.

### Bootstrap

In this project, Bootstrap is used to standardize and facilitate frontend design. Bootstrap is an open-source library based on HTML, CSS, and JavaScript, widely used by web developers to accelerate and simplify the development of websites and web applications. Bootstrap provides tools for designing and animating web user interfaces, aiding in the rapid structuring and styling of web pages.
