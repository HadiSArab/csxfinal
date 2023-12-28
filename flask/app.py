from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageOps
import os
# from flask import Flask, render_template, request
from functions import rmbg,rot,find_face,Blur,Gray,Canny

app = Flask(__name__)

# app = Flask(__name__)

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['image']
    selected_options = request.form.getlist('options')

    fname = uploaded_file.filename.split('.')[0]
    selected = selected_options[0]
    
    # Sample: Save the uploaded image to a folder named 'uploads'
    if uploaded_file:
        uploaded_file.save('static/uploads/' + uploaded_file.filename)

    if selected == "RemoveBG":
        print("RemoveBG")
        path = rmbg(uploaded_file,fname)
        # Redirect to the display page with the filename as a parameter
        return redirect(url_for('display', filename=uploaded_file.filename.split('.')[0]+"_rmbg.png"))
        
    elif selected == "FindFace":
        print("ّFindFace")
        path = find_face(uploaded_file.filename)
        # Redirect to the display page with the filename as a parameter
        return redirect(url_for('display', filename=uploaded_file.filename.split('.')[0]+"_faceD.jpg"))
    
    elif selected =="Rotate":
        print("Rotate")
        path = rot(uploaded_file.filename)
        # Redirect to the display page with the filename as a parameter
        return redirect(url_for('display', filename=uploaded_file.filename.split('.')[0]+"_rot90.jpg"))
    
    elif selected =="Blur":
        print("Blur")
        path = Blur(uploaded_file.filename)
        # Redirect to the display page with the filename as a parameter
        return redirect(url_for('display', filename=uploaded_file.filename.split('.')[0]+"_Blur.jpg"))
    
    elif selected =="Grayscale":
        print("Grayscale")
        path = Gray(uploaded_file.filename)
        # Redirect to the display page with the filename as a parameter
        return redirect(url_for('display', filename=uploaded_file.filename.split('.')[0]+"_gray.jpg"))
    
    elif selected =="Canny":
        print("Canny")
        path = Canny(uploaded_file.filename)
        # Redirect to the display page with the filename as a parameter
        return redirect(url_for('display', filename=uploaded_file.filename.split('.')[0]+"_Canny.jpg"))


    return "File uploaded and form submitted successfully!"

@app.route('/display/<filename>')
def display(filename):
    # Render the display page with the provided filename
    return render_template('display.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
