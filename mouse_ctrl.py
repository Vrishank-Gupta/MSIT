import imutils
import dlib
from imutils import face_utils
from utils import *
import numpy as np
import pyautogui as pag
import cv2



WINK_AR_DIFF_THRESH = 0.04
EYE_AR_THRESH = 0.19
WINK_CONSECUTIVE_FRAMES = 10
WINK_AR_CLOSE_THRESH = 0.19
MOUTH_AR_THRESH = 0.6
MOUTH_AR_CONSECUTIVE_FRAMES = 15
INPUT_MODE = False
EYE_CLICK = False
LEFT_WINK = False
RIGHT_WINK = False
SCROLL_MODE = False
EYE_AR_CONSECUTIVE_FRAMES = 15
MOUTH_COUNTER = 0
EYE_COUNTER = 0
WINK_COUNTER = 0
ANCHOR_POINT = (0, 0)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (255, 0, 0)
YELLOW_COLOR = (0, 255, 255)
RED_COLOR = (0, 0, 255)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

(nStart, nEnd) = face_utils.FACIAL_LANDMARKS_IDXS["nose"]
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

