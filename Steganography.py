"""
Steganography.py

This program finds the secret message hidden in one of the bit planes,
on one of the color channels from the given image.

@author: Anushree Das (ad1707)
"""

import cv2
from os import path
import numpy as np


def displayRotatedImage(filename):
    """
    loads the image and displays all 8 bit-planes for all 3 channels of the given image
    :param filename: path to file
    :return: None
    """
    # load image
    img = cv2.imread(filename)

    # if image loaded successfully
    if img is not None:
        # loop through all 3 channels
        for i in range(3):
            # extract one channel from the image data
            channel=img[:, :, i]

            # loop through all 8 bit-planes for given channel
            for k in range(0, 7):
                # create an image with value as 2^k for each pixel
                bitplane = np.full((channel.shape[0], channel.shape[1]), 2 ** k, np.uint8)

                # perform bitwise and operation between above created image and one channel of the image
                # the position of pixels with same value as 2^k from second image will result as 1
                # rest will be 0
                res = cv2.bitwise_and(bitplane, channel)

                # multiply ones with 255 for better visibility of the hidden message
                x = res * 255

                # display the bit-plane image
                cv2.imshow("Channel:"+str(i+1)+" Bit plane: "+str(k+1), x)
                ch = cv2.waitKey(0)
                # press 's' on keboard to save the image
                if ch == ord('s'):
                    cv2.imwrite('secret_msg_'+filename,x)
                    cv2.destroyAllWindows()
                else:
                    # press any key to see next bit plane
                    cv2.destroyAllWindows()



def main():
    # given image
    filename = 'CAT_Kitten_img_17.jpg' #'CAT_Kitten_img_22.jpg'

    # check if file exists
    if path.exists(filename):
        displayRotatedImage(filename)
    else:
        print("File doesn't exist")


if __name__ == "__main__":
    main()
