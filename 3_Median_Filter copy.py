import numpy as np 
import cv2
import matplotlib.pyplot as plt
body=cv2.imread("Input/body.png",cv2.IMREAD_GRAYSCALE)
elec=cv2.imread("Input/elec.png",cv2.IMREAD_GRAYSCALE)
circle=cv2.imread("Input/circle.png",cv2.IMREAD_GRAYSCALE)
party=cv2.imread("Input/party.png")
woman=cv2.imread("Input/woman.png")
things=cv2.imread("Input/things.png",cv2.IMREAD_GRAYSCALE)


for i in range(5):
    body=cv2.medianBlur(body,3)

for i in range(2):
    elec=cv2.medianBlur(elec,3)

for i in range(2):
    circle=cv2.medianBlur(circle,3)

for i in range(5):
    party=cv2.medianBlur(party,3)

for i in range(4):
    woman=cv2.medianBlur(woman,5)
for i in range(3):
    woman=cv2.medianBlur(woman,7)

for i in range(7):
    things=cv2.medianBlur(things,3)



cv2.imshow("",body)
cv2.waitKey()
cv2.imshow("",elec)
cv2.waitKey()
cv2.imshow("",circle)
cv2.waitKey()
cv2.imshow("",party)
cv2.waitKey()
cv2.imshow("",woman)
cv2.waitKey()
cv2.imshow("",things)
cv2.waitKey()

cv2.imwrite("Output/result_Body.png",body)
cv2.imwrite("Output/result_Elec.png",elec)
cv2.imwrite("Output/result_Circle.png",circle)
cv2.imwrite("Output/result_Party.png",party)
cv2.imwrite("Output/result_Woman.png",woman)
cv2.imwrite("Output/result_Things.png",things)