# rec_caras_famosas

Uses face_recognition library to find the nearest match to a face in front of the webcam in a folder ("caras_famosas") with images of given people (in this case of famous colombian people).

* preprocess_caras_famosas.py
  * Does preprocessing (including locating face end extracting encoding) of images in folder.
  
* see_preprocessed.py
  * Serves for checking if preprocessed images look right.

* find_match.py
  * Main function of the program; opens webcam, takes picture, finds nearest face in database and shows result.
