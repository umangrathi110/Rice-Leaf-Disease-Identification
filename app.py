from flask import Flask, request, jsonify, render_template, redirect
import cv2
import numpy as np
import tensorflow as tf
import os
from werkzeug.utils import secure_filename
import tempfile


# for windows
# UPLOAD_FOLDER= tempfile.gettempdir()


# for linux
UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

# Set the upload folder as a configuration variable
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model

# in windows
# model = tf.keras.models.load_model(r'C:\Users\asus\Desktop\Major Project\Rice-Leaf-Disease-Identification\resnet152_model.h5')

# in linux
model = tf.keras.models.load_model("/home/umang.rathi/Documents/Major Project/resnet152_model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            img = cv2.imread(filepath)
            if img is not None:
                img = cv2.resize(img, (256, 256))
                img = img.astype('float32') / 255
                img = np.expand_dims(img, axis=0)
                print(img.shape)
            else:
                return jsonify({'error': 'Error: Image variable is empty or has no data.'})
        except Exception as e:
            return str(e)

    # Make a prediction on the input image
    prediction = model.predict(img)

    # Get the predicted class
    predicted_class = np.argmax(prediction, axis=1)

    # Load the class names
    class_names = ['Bacterial Leaf Blast', 'Brown Spot', 'Healthy', 'Leaf Blast', 'Leaf Scald', 'Narrow Brown Spot']

    # Print the predicted class
    response = {'class': class_names[predicted_class[0]]}
    return render_template('index.html', result=response)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)