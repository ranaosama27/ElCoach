import tensorflow as tf
import pickle
import cv2
import time
import numpy as np
import posenet
from pose import Pose
from score import Score
from dtaidistance import dtw
import os

# list = os.listdir("D:/Asmaa/original/GP/pickle files/shoulder abduction pickles")  # dir is your directory path
# number_files = len(list)

# x = []
# number_files = 0

class get_Score(object):
    # list = os.listdir("D:/Asmaa/original/GP/pickle files/" + object)  # dir is your directory path

    def __init__(self, lookup='lookup.pickle'):
        self.a = Pose()
        self.s = Score()
        self.b = lookup
        self.input_test = []
        self.x = []
        list = os.listdir('C:/Users/progh/OneDrive/Desktop/Final/pickle files/' + self.b)  # dir is your directory path
        self.number_files = len(list)
        # for reading also binary mode is important
        for i in range(self.number_files):
            dbfile = open('pickle files/' + self.b + '/'+self.b+'_' + str(i + 1) + '.pickle', 'rb')
            db = pickle.load(dbfile)
            self.x.append(db)

    def get_action_coords_from_dict(self, action):
        r = []
        s = []
        for i in range(self.number_files):
            for (k, v) in self.x[i].items():
                (model_array, no_of_frames) = (v, v.shape[0])
            s.append(model_array)
            r.append(no_of_frames)
        return s, r

    def calculate_Score(self, video, action,miniVideo):
        with tf.Session() as sess:
            model_cfg, model_outputs = posenet.load_model(101, sess)
            model_array, j = self.get_action_coords_from_dict(action)           
            cap = cv2.VideoCapture(0)
            # minivideo = 'minivideo/'+miniVideo
            cap2 = cv2.VideoCapture('minivideo/arm_lifting.mp4') #video of avatar
            i = 0
            if cap.isOpened() is False:
                print("error in opening video")
            start_time = time.time()
            while cap.isOpened() & cap2.isOpened():
                ret_val, image = cap.read()
                ret, frame = cap2.read()
                if ret_val & ret:
                    if video == "none":
                        # show frame
                        cv2.imshow('preview', image)
                        cv2.imshow('avatar',frame) # show avatar video
                        # c = cv2.waitKey(1)
                        if cv2.waitKey(1) and 0xFF == ord('q'):
                            # break
                            break
                            cap.release()
                        if time.time() - start_time >= 30:
                            break
                            cap.release()
                    input_points = self.a.getpoints(cv2.resize(image, (372, 495)), sess, model_cfg, model_outputs)
                    input_new_coords = np.asarray(self.a.roi(input_points)[0:34]).reshape(17, 2)
                    self.input_test.append(input_new_coords)
                    i = i + 1
                else:
                    break
            if video == "none":
                cap.release()
                cv2.destroyAllWindows()

            else:
                cap.release()
            finscore = []
            scorelist = []
            for w in range(self.number_files):
                modelarray = model_array[w]
                jj = j[w]
                b = np.array(self.input_test)
                row, col, t = b.shape
                row1, col1, t1 = modelarray.shape
                if (jj > i):
                    modelarray = modelarray[0:row]
                    jj = i

                final_score, score_list = self.s.compare(np.asarray(self.input_test), np.asarray(modelarray), jj, i)
                finscore.append(final_score)
                scorelist.append(score_list)

        return finscore, scorelist
