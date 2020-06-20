from flask import Flask, render_template, request
import os
import face_recognition as fr
from PIL import Image, ImageDraw
import base64
import io
from face_functions import face_detection, feature_detection, face_encoding, compare_to_obama, turn_gray

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def start_page():
    return render_template('index.html')

@app.route("/<page>")
def another_page(page):
    return render_template(page)

@app.route('/upload_face_detection', methods=['POST'])
def upload_face_detection():
    file = request.files['image']
    pil_image, face_detected = face_detection(file)
    img = prepare_image(pil_image)

    return render_template('course-page3.html', faceDetected=face_detected, image_to_show=img.decode('ascii'),
                           init=True)


@app.route('/upload_feature_detection', methods=['POST'])
def upload_feature_detection():
    file = request.files['image']
    pil_image, face_detected = feature_detection(file)
    img = prepare_image(pil_image)

    return render_template('course-page4.html', faceDetected=face_detected, image_to_show=img.decode('ascii'),
                           init=True)


@app.route('/upload_face_encoding', methods=['POST'])
def upload_face_encoding():
    file = request.files['image']
    encoding, face_detected = face_encoding(file)

    return render_template('course-page6.html', faceDetected=face_detected, image_to_show=True, encoding=encoding,
                           init=True)


@app.route('/upload_face_comparison', methods=['POST'])
def upload_face_comparison():
    file = request.files['image']
    distance, face_detected = compare_to_obama(file)

    return render_template('course-page7.html', faceDetected=face_detected, image_to_show=True, distance=distance,
                           init=True)

def prepare_image(pil_image):
    # resize image
    basewidth = 300
    wpercent = (basewidth / float(pil_image.size[0]))
    hsize = int((float(pil_image.size[1]) * float(wpercent)))
    pil_image = pil_image.resize((basewidth, hsize), Image.ANTIALIAS)

    # save image
    img_io = io.BytesIO()
    pil_image.save(img_io, 'jpeg', quality=70)
    img_io.seek(0)
    img = base64.b64encode(img_io.getvalue())

    return img


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)





