from flask import render_template, url_for, flash, redirect , request
from covid import app
from covid.forms import UploadForm
import os

import cv2
import numpy as np
from tensorflow.keras.models import load_model
import joblib

UPLOAD_FOLDER = 'covid/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


covid_model = load_model("covid_detector_model.h5")


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/upload" , methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = request.files['picture_file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],'upload_chest.jpg'))
        image = cv2.imread('covid/static/images/upload_chest.jpg')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # arrange format as per keras
        image = cv2.resize(image,(224,224))
        image = np.array(image) / 255
        image = np.expand_dims(image, axis=0)
        pred=covid_model.predict(image)
        return render_template('prediction.html',pred=pred)
    return render_template('upload.html',form = form)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/prediction")
def prediction():
    return render_template('prediction.html')

@app.route("/prevention")
def prevention():
    return render_template('prevention.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
