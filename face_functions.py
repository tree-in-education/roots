from PIL import Image, ImageDraw
import face_recognition as fr


def face_detection(image):
    fr_loaded = fr.load_image_file(image)
    pil_image = Image.open(image)
    d = ImageDraw.Draw(pil_image)

    face_locations = fr.face_locations(fr_loaded)

    if len(face_locations) == 0:
        face_detected = False
    else:
        face_detected = True

    top, right, bottom, left = face_locations[0]
    d.rectangle([left, top, right, bottom], outline='red', width=5)

    return pil_image, face_detected


def feature_detection(image):
    fr_loaded = fr.load_image_file(image)
    pil_image = Image.open(image)
    draw = ImageDraw.Draw(pil_image)

    face_landmarks_list = fr.face_landmarks(fr_loaded)

    if len(face_landmarks_list) == 0:
        face_detected = False
    else:
        face_detected = True

    for face_landmarks in face_landmarks_list:

        for name, list_of_points in face_landmarks.items():
            print("The {} in this face has the following points: {}".format(name, list_of_points))
            draw.line(list_of_points, fill="red", width=2)

    return pil_image, face_detected

def face_encoding(image):
    image = fr.load_image_file(image)

    # a cute thing would be to literally print the numbers on your face
    # list of numpy arrays of all the encodings of faces in an image
    if len(fr.face_encodings(image)) == 0:
        face_detected = False
    else:
        face_detected = True

    face_encoding = fr.face_encodings(image)[0]

    return face_encoding, face_detected

def compare_to_obama(image):
    fr_loaded = fr.load_image_file(image)
    obama_face_encoding = [-7.23204687e-02, 1.35010049e-01, 6.36744499e-02, -2.67444067e-02,
                           -3.66925448e-03, -3.10106575e-03, -1.11843295e-01, -7.46017992e-02,
                           1.80318102e-01, -1.51639313e-01, 2.66451776e-01, 7.91755319e-02,
                           -2.24254489e-01, -1.32122055e-01, 8.43790323e-02, 1.55045241e-01,
                           -2.41609246e-01, -8.60512853e-02, -1.02505408e-01, -7.33838007e-02,
                           -6.15564734e-03, -1.16154673e-02, 7.17357472e-02, 5.75199276e-02,
                           -8.61256495e-02, -3.88113201e-01, -6.69104606e-02, -1.35969147e-01,
                           -3.78355384e-04, -1.75433964e-01, -1.00276984e-01, -3.08765993e-02,
                           -1.74939394e-01, -1.02570444e-01, -7.17597455e-03, -4.94118407e-03,
                           -4.53869253e-03, -1.34227574e-02, 1.76807612e-01, 3.37669551e-02,
                           -1.26588956e-01, 6.54829592e-02, -6.29560649e-03, 2.26179034e-01,
                           2.41653830e-01, 1.15561515e-01, 2.04917118e-02, -5.90783656e-02,
                           1.38776332e-01, -2.26210535e-01, 5.49663305e-02, 1.71352774e-01,
                           8.63246769e-02, 3.00506130e-02, 1.03940278e-01, -2.04887167e-01,
                           -2.08544433e-02, 8.89000893e-02, -8.18602517e-02, 5.68664223e-02,
                           5.26944473e-02, -7.12841973e-02, 2.98431329e-02, 5.18204197e-02,
                           2.04209730e-01, 4.96703163e-02, -1.09083459e-01, -5.23340516e-02,
                           1.11273251e-01, -2.90242545e-02, -1.32047087e-02, -1.50181986e-02,
                           -1.81545049e-01, -2.26256609e-01, -2.64775723e-01, 6.11639172e-02,
                           3.47226948e-01, 1.91239119e-01, -1.97597116e-01, 5.62040508e-03,
                           -1.68167457e-01, 9.48884711e-03, 6.19610175e-02, 6.48774654e-02,
                           -4.89188768e-02, -8.59653875e-02, -8.95417258e-02, 5.79920560e-02,
                           1.09342173e-01, 5.06685600e-02, -1.94630343e-02, 2.01605737e-01,
                           -3.95128801e-02, 6.05301559e-02, 3.94182280e-04, 1.02596059e-02,
                           -1.55268475e-01, -2.44350061e-02, -1.68045342e-01, -5.60386926e-02,
                           -1.32815316e-02, -1.79292392e-02, -2.84540653e-03, 1.22471094e-01,
                           -1.92314789e-01, 7.54063502e-02, 3.94764543e-03, -1.88698433e-02,
                           -1.49060711e-02, 1.19328767e-01, -8.99328738e-02, -5.09399921e-02,
                           6.87622577e-02, -2.20900357e-01, 2.37240389e-01, 2.76409209e-01,
                           4.07231413e-02, 1.59905136e-01, 7.47956261e-02, 5.56012169e-02,
                           -1.88010707e-02, -2.75503695e-02, -1.56012431e-01, -9.27950889e-02,
                           2.80142948e-02, 7.06249028e-02, 9.05941427e-02, 2.66002864e-03]

    if len(fr.face_encodings(fr_loaded)) == 0:
        face_detected = False
    else:
        face_detected = True

    encoding = face_encoding(image)[0] # numpy can't read
    match_results = fr.face_distance([obama_face_encoding], encoding)

    if match_results < .6:
        message = "Your face is a match! You either used a picture of Obama or look a lot like him. On a scale from 1 to 10, where 0 is the same photo and 9 is very different, your distance from Obama is " + str(int(match_results * 10))
    else:
        message = "Not a match. On a scale from 0 to 9, where 0 is the indicates the same photo and 9 is a very different, your distance from Obama is " + str(int(match_results * 10))

    return message, face_detected

def turn_gray(image):
    img = Image.open(image).convert('LA')
    img.save('greyscale.png')





