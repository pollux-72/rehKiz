import pathlib
import argparse

import numpy as np
from PIL import Image, ImageDraw
import cv2


def main(video):


    wait = False
    save = False
    frame = 0

    # read the video
    cap = cv2.VideoCapture(video)

    video = pathlib.Path(video)
    
    # loop over frames
    while True:

        kp = cv2.waitKey(1) & 0xFF

        if kp == ord('s'):
            wait = not wait
        elif kp == ord('w'):
            save = not save
        elif kp == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return

        # stop stream reading
        if wait:
          continue

        ret, orig_img = cap.read()# image as numpy
        # convert to grayscale
        img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
        if not ret:
            return

        # parameters for clipping
        minimum = 120
        maximum = 200
        img = np.clip(img, minimum, maximum)
        i = np.unravel_index(orig_img.argmax(), orig_img.shape)
        r = 20

        # for visualization create a copy
        image_np_with_detections = orig_img.copy()
        image_pil = Image.fromarray(np.uint8(orig_img))
        draw = ImageDraw.Draw(image_pil)
        draw.circle([i[1], i[0]], r)
        np.copyto(image_np_with_detections, np.array(image_pil))

        # show the result
        cv2.imshow('object detection', image_np_with_detections)

        if save:
            filename = f'{video.name}-{frame}.jpg'
            print(f'Save snapshot: {filename}')
            cv2.imwrite(filename, image_np_with_detections)
            save = False

        frame += 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('video')
    args = parser.parse_args()

    main(args.video)