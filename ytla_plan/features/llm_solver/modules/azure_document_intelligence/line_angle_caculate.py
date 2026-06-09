import math
import numpy as np


def get_line_angle(polygon):

    """
    Azure polygon:

    [
      x1,y1,
      x2,y2,
      x3,y3,
      x4,y4
    ]

    """

    x1 = polygon[0]
    y1 = polygon[1]

    x2 = polygon[2]
    y2 = polygon[3]


    return math.degrees(
        math.atan2(
            y2-y1,
            x2-x1
        )
    )



def estimate_angle(result):

    angles = []


    for page in result.pages:

        for line in page.lines:

            angle = get_line_angle(
                line.polygon
            )


            # 去除竖排文字
            if abs(angle) > 45:
                continue


            # 去除太短文本
            xs = line.polygon[::2]
            ys = line.polygon[1::2]


            width = math.dist(
                (xs[0],ys[0]),
                (xs[1],ys[1])
            )


            if width < 40:
                continue


            angles.append(angle)


    if len(angles)==0:
        return 0


    return float(
        np.median(angles)
    )