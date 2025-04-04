import argparse

import cv2


def main(video):

    cap = cv2.VideoCapture(video)
    while True:

        ret, img = cap.read()
        cv2.imshow('object detection', img) 
        #cv2.resize(im, (640, 640)))
        kp = cv2.waitKey(1) & 0xFF
        if kp == ord('q'):
            cap.release()
            cv2.destroyAllWindows()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('video')
    args = parser.parse_args()

    main(args.video)