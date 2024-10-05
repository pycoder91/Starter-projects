# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:08:21 2024

@author: Omansh Arora
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:26:33 2024

@author: Omansh Arora
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("Lennabw.png",0)
hist = np.zeros(256)
s = I.shape
#print(s)

for i in range(s[0]):
    for j in range(s[1]):
        intensity = I[i,j]
        
        if intensity > 127:
            intensity = 255
        if intensity <= 127:
            intensity = 0
            
        I[i][j] = intensity

cv2.imwrite("intensityImage.png",I)