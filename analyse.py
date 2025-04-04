import argparse

import cv2
import time

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg") 

def main(video):
    plt.ion()
    fig, ax = plt.subplots(1,1, figsize=(8,5))

    cap = cv2.VideoCapture(video)
    paused = False

    while True:
        if not paused:
            # CV
            ret, img = cap.read()
            if not ret:
                break # No image available. Exit loop
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('object detection', img) 
            #cv2.resize(im, (640, 640)))
            hist = cv2.calcHist(img, [0], None, [256], [0, 256])

            # Matplotlib
            ax.clear()
            ax.plot(hist)

            plt.draw()
            plt.pause(0.01)

        # Key Inputs
        kp = cv2.waitKey(1) & 0xFF
        if kp == ord('q'):
            break
        elif kp == 32 or kp == ord('p'):
            paused = not paused

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('video')
    args = parser.parse_args()

    main(args.video)