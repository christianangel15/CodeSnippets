import os

import cv2
import face_recognition

# Thanks to SentDex


def FaceRecognition(TrainingPath, TestingPath, TOL, MODEL):
    FRAME = 3
    FONT = 2
    print('Loading training Images for identity...')
    TrainedFaces = []
    TrainedNames = []

    for identity in os.listdir(TrainingPath):
        for IMGName in os.listdir(f'{TrainingPath}/{identity}'):
            image = face_recognition.load_image_file(
                f'{TrainingPath}/{identity}/{IMGName}')
            encode = face_recognition.face_encodings(image)
            if encode:
                print(f'{IMGName}:Encoded as {identity}')
                TrainedFaces.append(encode[0])
                TrainedNames.append(identity)

    for IMGName in os.listdir(TestingPath):
        print(f'Processing {IMGName} for identification..')
        IMG = face_recognition.load_image_file(f'{TestingPath}/{IMGName}')
        locs = face_recognition.face_locations(IMG, model=MODEL)
        encods = face_recognition.face_encodings(IMG, locs)
        IMG = cv2.cvtColor(IMG, cv2.COLOR_RGB2BGR)

        for encode, faceLoc in zip(encods, locs):
            results = face_recognition.compare_faces(
                TrainedFaces, encode, TOL)
            match = None
            if True in results:
                match = TrainedNames[results.index(True)]
                print(f'{IMGName} has {match} in it..!')

                top_L = (faceLoc[3], faceLoc[0])
                btm_R = (faceLoc[1], faceLoc[2])
                color = [0, 0, 255]
                cv2.rectangle(IMG, top_L, btm_R, color, FRAME)

                top_L = (faceLoc[3], faceLoc[2])
                btm_R = (faceLoc[1], faceLoc[2]+22)
                cv2.rectangle(IMG, top_L, btm_R, color, cv2.FILLED)
                cv2.putText(IMG, match, (faceLoc[3]+10, faceLoc[2]+15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT)

        cv2.imshow(IMGName, IMG)
        cv2.waitKey(5000)
        cv2.destroyWindow(IMGName)


FaceRecognition('Known_faces', 'Unknown_faces', 0.5, 'hog')
# TrainingPath = 'Known_faces'
# TestingPath = 'Unknown_faces'
# TOL = 0.5

# MODEL = 'hog'   or cnn(GPU)
