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

def mouth_aspect_ratio(mouths):
	A = np.linalg.norm(mouths[13] - mouths[19])
	B = np.linalg.norm(mouths[14] - mouths[18])
	C = np.linalg.norm(mouths[15] - mouths[17])
	D = np.linalg.norm(mouths[12] - mouths[16])
	mars = (A + B + C) / (2 * D)
	return mars


def direction(nose, anchor, w, h, mult=1):
	nx, ny = nose
	x, y = anchor

	if ny > y + mult * h:
	    return 'down'
	elif ny < y - mult * h:
	    return 'up'

	if nx > x + mult * w:
	    return 'right'
	elif nx < x - mult * w:
	    return 'left'

	return '-'
