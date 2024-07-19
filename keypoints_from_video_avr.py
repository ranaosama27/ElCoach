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
import argparse
import os

#USAGE : python keypoints_from_video.py --activity "shoulder abduction" --video "shoulder_abduction_1.avi"

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--activity", required=True,
    help="activity to be recorder")
ap.add_argument("-v", "--video", required=True,
    help="video file from which keypoints are to be extracted")
ap.add_argument("-l", "--lookup", default="shoulder abduction.pickle",    # khle el default esm el tmrena
    help="The pickle file to dump the lookup table")
args = vars(ap.parse_args())



def main():
    shapes = []
    a = Pose()
    sum1 = np.zeros([1, 17, 2])
    c = {}
    rows = [0]

    list = os.listdir('D:/Asmaa/folder projectsss/Human-Pose-Compare-final/dataset/shoulder abduction')  # dir is your directory path bta3 el videos
    number_files = len(list)
    with tf.Session() as sess:
        for itr in range(number_files):
            b = []
            model_cfg, model_outputs = posenet.load_model(101, sess)

            cap = cv2.VideoCapture('dataset/shoulder abduction/shoulder_abduction_' + str(itr + 1) + '.avi')  # esm el video 3dl w mtnsosh _1 _2 _3 ... etc
            i = 1

            if cap.isOpened() is False:
                print("error in opening video")
            while cap.isOpened():
                ret_val, image = cap.read()
                if ret_val:
                    image = cv2.resize(image,(372,495))
                    input_points,input_black_image = a.getpoints_vis(image,sess,model_cfg,model_outputs)
                    input_points = input_points[0:34]
                    print(input_points)
                    input_new_coords = a.roi(input_points)
                    input_new_coords = input_new_coords[0:34]
                    input_new_coords = np.asarray(input_new_coords).reshape(17,2)
                    b.append(input_new_coords)
                    cv2.imshow("black", input_black_image)
                    cv2.waitKey(1)
                    i += 1
                else:
                    break
            cap.release()


            b = np.array(b)
            shapes.append(b.shape)  #de haga lyaa msh mohma

            row_arr, col , ind = b.shape   # b3ml save le shape el keypoints el tl3aly mn video
            row_sum, col , ind = sum1.shape  # b3ml save le shape el sum kol mra
            rows = np.append(rows, row_arr)  #b append 3dad el rows bs bta3t b
            if row_sum < row_arr:            # bkarn lw el shape el sum olyl 3n shape el b el dkhle mn elvideo ,
                diff = row_arr - row_sum    #bakhod el diff mbenhom w azwdo 3l list elsum b zeros
                z = np.zeros([diff, 17, 2])
                sum1 = np.concatenate((sum1, z))
            length = len(rows)    # length el list el byb2a feha kol el shapes
            for j in range(length - 1):    # de hafhmlhko b voice notes
                sum1[rows[j]:rows[j + 1], :, :] +=  ( (b[rows[j]:rows[j + 1], :, :]) / (number_files - j) )
            print("--------el average -------")
            print(sum1)
            average = sum1
            print("-------------------------------------------------type el avg --------------------------------")
            print(type(average))
            cv2.destroyAllWindows

            print("Lookup Table Created")
        print('-------------------------ell summ---------------------------------')
        print(average)
        print('------------------------shapes --------------------------------')
        print(shapes)
        fin = np.array(average)
        c[args["activity"]] = fin
        f = open(args["lookup"],'wb')
        pickle.dump(c,f)
        # pickle.dump()

if __name__ == "__main__":
    main()


