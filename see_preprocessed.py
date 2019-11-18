import os
import pickle
import numpy as np
import cv2

danger_mode = True

with open('index_to_name.pickle', 'rb') as itn_f:
    index_to_name = pickle.load(itn_f)

imgs_dir = 'caras_famosas/preprocessed/'

repreprocess = False

for img_name in os.listdir(imgs_dir):
    img = cv2.imread(imgs_dir + img_name)

    index = int(img_name[:-4])
    name = index_to_name[index]

    cv2.imshow(name, img)

    key = cv2.waitKey(0)

    if danger_mode and (key == ord('d')):
        with open('para_meter.txt', 'a') as pm_f:
            pm_f.write(name)

        os.remove(imgs_dir + img_name)

        repreprocess = True

    if key == ord('q'):
        break

    cv2.destroyWindow(name)

cv2.destroyAllWindows()

if repreprocess:
    import preprocess_caras_famosas

    preprocess_caras_famosas.main()
