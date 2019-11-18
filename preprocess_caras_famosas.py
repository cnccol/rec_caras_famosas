import os
import pickle
import numpy as np
import cv2
import imutils 
import face_recognition

def main():
    W = 1280
    H = 720

    encodings_caras_famosas = []
    index_to_name = {}
    index = 0

    for img_name in os.listdir('caras_famosas'):
        if img_name.endswith('.jpg') or img_name.endswith('.png'):
            img = cv2.imread('caras_famosas/' + img_name)
            if (img.shape[0] < H) and (img.shape[1] < W//2):
                print(img_name, 'not big enough')
                continue

            if img.shape[0] > img.shape[1]:
                img = imutils.resize(img, width=W//2)[:H, :, :]
            else:
                img = imutils.resize(img, height=H)[:, W//4:-W//4, :]

            face_locations = face_recognition.face_locations(img)

            if face_locations:
                face_location = face_locations[0]
                top, right, bottom, left = face_location

                face_encoding = face_recognition.face_encodings(img,
                                                                [face_location])[0]

                cv2.rectangle(img, (left, top), (right, bottom), (200, 0, 0), 2)

                if img.shape[0] != H:
                    print(img_name, 'of incorrect size', img.shape)
                    img = imutils.resize(img, height=H)
                    print(img.shape)

                cv2.imwrite('caras_famosas/preprocessed/' + str(index) + '.jpg',
                            img)

                name = img_name[:-4].replace('_', ' ')
                index_to_name[index] = name
                encodings_caras_famosas.append(face_encoding)
                index += 1

                print('Done with', img_name)

            else:
                print('No face found in', img_name)

    encodings_caras_famosas = np.array(encodings_caras_famosas)

    with open('encodings_caras_famosas.pickle', 'wb') as enc_f:
        pickle.dump(encodings_caras_famosas, enc_f)

    with open('index_to_name.pickle', 'wb') as itn_f:
        pickle.dump(index_to_name, itn_f)

if __name__ == '__main__':
    main()
