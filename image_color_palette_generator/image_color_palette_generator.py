import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex
from PIL import Image # for reading image files
from collections import Counter
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['SECRET_KEY'] = 'N6NnTBUUxTxrovGfBjEU'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

Bootstrap(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Forms
class UploadFileForm(FlaskForm):
    task_name = StringField('What you need to do: ', validators=[DataRequired()])
    due_date = DateField('When you need to finish it by: ', validators=[DataRequired()])
    note = StringField('Any notes about this task? If none, leave blank.', render_kw={"placeholder": "N/A"})
    submit = SubmitField('Submit')

# Routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        # Setting up the ndarray from the image
        img = Image.open(f"static/uploads/{filename}")
        img_array = np.array(img) / 255

        # Obtaining the Hex Values from the ndarray
        hex_values = [rgb2hex(img_array[x][y]) for x in range(img_array.shape[0]) for y in range(img_array.shape[1])]

        # Counting the occurences top 10 most common hex values in image
        top_10 = Counter(hex_values).most_common(10)

        return render_template('index.html', filename=filename, top_10 = top_10)
    else:
        flash('Allowed image types are -> png, jpg, jpeg')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)




if __name__ == "__main__":
    app.run(debug=True)
