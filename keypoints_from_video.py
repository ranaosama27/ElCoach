import tensorflow as tf
import cv2
import time
import math
import numpy
import numpy as np
import posenet
from pose import Pose
from score import Score
import pickle
import os
import argparse

# USAGE : python3 keypoints_from_video.py --activity "punch - side" --video "test.mp4"
# USAGE : python keypoints_from_video.py --activity "static_tricep_extension_right" --video "test.mp4"
# USAGE : python keypoints_from_video.py --activity "static_tricep_extension_left" --video "test.mp4"

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--activity", required=True,
                help="activity to be recorder")
ap.add_argument("-v", "--video", required=True,
                help="video file from which keypoints are to be extracted")
ap.add_argument("-l", "--lookup", default="lookup_new.pickle",
                help="The pickle file to dump the lookup table")
args = vars(ap.parse_args())


def main():
    list = os.listdir(
        'F:/GP/mistake/Human-Pose-Compare-master/ex4/' + args["activity"])  # dir is your directory path bta3 el videos
    number_files = len(list)
    print("\n\n\n\n=============================\n\n\n\n")
    print("str(number_files)")
    print(str(number_files))
    print("\n\n\n\n=============================\n\n\n\n")
    with tf.Session() as sess:
        for itr in range(number_files):
            a = Pose()
            b = []
            c = {}
            model_cfg, model_outputs = posenet.load_model(101, sess)

            cap = cv2.VideoCapture('ex4/' + args["activity"] + '/' + args["activity"] + '_' + str(itr + 1) + '.avi')
            i = 1

            if cap.isOpened() is False:
                print("error in opening video")
            while cap.isOpened():
                ret_val, image = cap.read()
                if ret_val:
                    image = cv2.resize(image, (372, 495))
                    input_points, input_black_image = a.getpoints_vis(image, sess, model_cfg, model_outputs)
                    input_points = input_points[0:34]
                    print(input_points)
                    input_new_coords = a.roi(input_points)
                    input_new_coords = input_new_coords[0:34]
                    input_new_coords = np.asarray(input_new_coords).reshape(17, 2)
                    b.append(input_new_coords)
                    cv2.imshow("black", input_black_image)
                    cv2.waitKey(1)
                    i = i + 1
                else:
                    break
            cap.release()

            b = np.array(b)

            cv2.destroyAllWindows
            print(b)
            print(b.shape)
            print("Lookup Table Created")
            c[args["activity"]] = b
            f = open(args["activity"] + '_' + str(itr + 1) + '.pickle', 'wb')
            pickle.dump(c, f)
        # pickle.dump()


if __name__ == "__main__":
    main()
