# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import random

# tf Keras
import tensorflow as tf
from skimage.transform import resize

# import unet from model.py
#from model import unet

# Flask utils
from flask import Flask,flash, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# model architacture path
MODEL_JSON_PATH = 'model_save/unet_model.json'
# trained model weights
MODEL_PATH = 'model_save/best_model.h5'
LETTER_SET = list(set('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
# Uploaded image folder path
UPLOAD_FOLDER = 'static/uploaded'
# predicted image folder path
PRED_FOLDER = 'static/predicted'


def generate_random_name(filename):
    """ Generate a random name for an uploaded file. """
    ext = filename.split('.')[-1]
    rns = [random.randint(0, len(LETTER_SET) - 1) for _ in range(3)]
    chars = ''.join([LETTER_SET[rn] for rn in rns])

    new_name = "{new_fn}.{ext}".format(new_fn=chars, ext=ext)
    new_name = secure_filename(new_name)

    return new_name



def model_prediction(image_path,model):
    ''' This function predicts mask image'''
    img = tf.keras.preprocessing.image.load_img(image_path,color_mode='grayscale')
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = resize(img,(128,128),mode='constant',preserve_range=True)
    img = np.expand_dims(img,axis=0)
    img = img/255.0

    # do prediction
    prediction = model.predict(img)
    return prediction[0]


@app.route('/', methods=['GET', 'POST'])
def upload(model):
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file was uploaded.')
            return redirect(request.url)
        # Get the file from post request
        image_file = request.files['image']

        if image_file.filename == '':
            flash('No file was uploaded.')
            return redirect(request.url)

        if image_file:
            # Save the file to ./uploads
            # uploaded image file path
            file_path = os.path.join(UPLOAD_FOLDER,image_file.filename)
            # save uploaded image
            image_file.save(file_path)

            # Make prediction
            preds = model_prediction(file_path, model)
            pred_img = tf.keras.preprocessing.image.array_to_img(preds)
            # generate random image file name for predicted image
            pred_filename = generate_random_name(image_file.filename)
            # predicted image absolute path
            pred_filepath = os.path.join(PRED_FOLDER,pred_filename)
            # save predicted image
            pred_img.save(pred_filepath)


            return render_template('index.html',
            uploaded_image=image_file.filename,pred_image=pred_filename)
    return render_template('index.html',uploaded_image=None,pred_image=None)

if __name__ == '__main__':
    # Load pre-trained model
    json_file = open(MODEL_JSON_PATH, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = tf.keras.models.model_from_json(loaded_model_json)
    model.load_weights(MODEL_PATH)
    print('Model Loaded Succesfully')
    app.run(host='0.0.0.0',port=8080,debug=True)
