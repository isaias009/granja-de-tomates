import cv2
import numpy as np

def ColorHSV(img, inicio, limite):
  LowColor = inicio
  HighColor = limite

  CompColor = cv2.inRange(img, LowColor, HighColor)
  return np.sum(np.nonzero(CompColor))

def AnalizarTomate(url):
  img = cv2.imread('resources/'+url)

  CountBlack = ColorHSV(img, (0, 0, 0), (0, 0, 0))
  CountRed = ColorHSV(img, (0,0,255), (128,128,255))
  CountGreen = ColorHSV(img, (0, 50, 120), (10, 255, 255))

  if (CountRed != 0 and CountGreen != 0 and CountBlack == 0) or (CountRed != 0 and CountBlack == 0):
    return 0

  elif CountBlack != 0 and CountGreen != 0:
    return 1

  elif CountGreen != 0:
    return 2

# 0 => maduro
# 1 => podrido
# 2 => no maduro