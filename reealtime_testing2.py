from modules import *
from MP_holistic_styled_landmarks import mp_holistic,draw_styled_landmarks
from mediapipe_detection import mediapipe_detection
from keypoints_extraction import extract_keypoints
import keras
from folder_setup import *
from visualization import prob_viz,colors
from PIL import ImageFont, ImageDraw, Image
import pyttsx3

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
sequence = []
sentence = []
threshold = 0.9

model = keras.models.load_model('d3test3.h5')
# model = keras.models.load_model('test_cap.h5')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

mean = "수화 단어:"
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        image, results = mediapipe_detection(frame, holistic)

        draw_styled_landmarks(image, results)

        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-50:]
        #print(len(sequence))
        b, g, r, a = 255, 255, 255, 0
        fontpath = "GowunDodum-Regular.ttf"
        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)

        if len(sequence) == 50:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            #print(np.argmax(res))

            print(actions[np.argmax(res)])
            mean = "수화 단어:" + actions[np.argmax(res)]
            s = pyttsx3.init()
            data = str(actions[np.argmax(res)])
            s.say(data)
            s.runAndWait()

            sequence.clear()
            cv2.waitKey(100)

            if res[np.argmax(res)] > threshold:
                if len(sentence) > 0:
                    if actions[np.argmax(res)] != sentence[-1]:
                        sentence.append(actions[np.argmax(res)])
                else:
                    sentence.append(actions[np.argmax(res)])

            if len(sentence) > 2:
                sentence = sentence[-2:]

            #image = prob_viz(res, actions, image, colors)

        draw.rectangle([(0, 0), (550, 40)], fill=(96,96,96,0), outline =(255,51,51), width=2)
        draw.rectangle([(0, 50), (400, 100)], fill=(96,96,96,0), outline =(255,51,51), width=2)
        draw.ellipse((1180, 20, 1270, 95), fill = (96,96,96,0), outline =(255,51,51), width=2)

        draw.text((10, 10),"이전 단어 목록: " + ' '.join(sentence), font=ImageFont.truetype(fontpath, 20), fill=(b, g, r, a))
        draw.text((10, 50), mean, font=ImageFont.truetype(fontpath, 40), fill=(b, g, r, a))
        draw.text((1200, 30), str(len(sequence)), font=ImageFont.truetype(fontpath, 40), fill=(b, g, r, a))
        image = np.array(img_pil)

        cv2.imshow('Korean Sign-language', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()