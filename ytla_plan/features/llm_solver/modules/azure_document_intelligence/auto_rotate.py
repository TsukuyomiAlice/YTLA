import cv2
import numpy as np



def rotate_bound(img, angle):

    h,w = img.shape[:2]


    center = (
        w/2,
        h/2
    )


    M = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0
    )


    cos = abs(M[0,0])
    sin = abs(M[0,1])


    new_w = int(
        h*sin+w*cos
    )

    new_h = int(
        h*cos+w*sin
    )


    M[0,2] += (
        new_w/2-center[0]
    )

    M[1,2] += (
        new_h/2-center[1]
    )


    return cv2.warpAffine(
        img,
        M,
        (new_w,new_h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )