import cv2

def enhance(img):

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )


    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8,8)
    )


    enhanced = clahe.apply(
        gray
    )


    return enhanced