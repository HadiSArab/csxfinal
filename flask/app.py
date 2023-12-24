from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageOps
import os

app = Flask(__name__)

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/upload', methods=['POST'])
def upload():   
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Save the uploaded image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        # Apply the selected effect
        effect = request.form['effect']
        image = Image.open(image_path)

        if effect == 'grayscale':
            image = ImageOps.grayscale(image)
        elif effect == 'sepia':
            # Apply sepia effect (you can implement this or use a library)
            pass
        elif effect == 'invert':
            image = ImageOps.invert(image)

        # Save the processed image
        processed_path = os.path.join('static/result/', 'processed_' + file.filename)
        image.save(processed_path)

        return render_template('index.html', image_path=processed_path)

    return redirect(request.url)
if __name__ == '__main__':
    app.run(debug=True)
