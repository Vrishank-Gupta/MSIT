import numpy as np

def eye_aspect_ratio(eyes):
	A = np.linalg.norm(eyes[1] - eyes[5])
    B = np.linalg.norm(eyes[2] - eyes[4])
    C = np.linalg.norm(eyes[0] - eyes[3])
    ears = (A + B) / (2.0 * C)
    return ears

def direction(nose, anchor, w, h, mult=1):
    nx, ny = nose
    x, y = anchor

    if nx > x + mult * w:
        return 'right'
    elif nx < x - mult * w:
        return 'left'

    if ny > y + mult * h:
        return 'down'
    elif ny < y - mult * h:
        return 'up'

    return '-'