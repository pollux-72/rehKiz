import argparse

import cv2
import time
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg") 

def showPixelValue(event, x, y, flags, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel_value = img[y, x]
        text = f"{pixel_value}"
        cv2.putText(img, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.imshow('object detection', img)

def main(video):
    # plt.ion()
    # fig, ax = plt.subplots(1,1, figsize=(8,5))

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
            cv2.setMouseCallback('object detection', showPixelValue, img)
            cv2.resize(img, (640, 640))
            # hist = cv2.calcHist(img, [0], None, [256], [0, 256])

            # Differentiate in X and Y
            gradX = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
            gradY = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
            abs_grad_x = cv2.convertScaleAbs(gradX)
            abs_grad_y = cv2.convertScaleAbs(gradY)
            
            # Resulting Gradient
            grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
            cv2.imshow("gradient", grad)

            # Gaussian filter for Blur
            blur = cv2.GaussianBlur(grad, (41, 41), 0)

            # Reduce Noise in Image
            gradBlurDiff = cv2.subtract(grad, blur)
            cv2.imshow("Grad - Blur", gradBlurDiff)

            # Binarization with hard threshold
            _, binary = cv2.threshold(grad, 150, 255, cv2.THRESH_BINARY)

            # Closing holes in binarized Image
            closure = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (40, 40)))
            cv2.imshow("Schliessung", closure)

            # Exept for the fawn
            diletation = cv2.dilate(closure, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
            cv2.imshow("Diletation", diletation)

            # Visualizing Contours
            contours, hierarchy = cv2.findContours(diletation,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # So the bounding box can be colorful
            cv2.drawContours(img, contours, -1, (0, 0, 140), 3)
            cv2.imshow("Bounding Box", img)

            # Matplotlib
            # ax.clear()
            # ax.plot(hist)

            # plt.draw()
            # plt.pause(0.01)

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