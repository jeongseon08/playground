#02 matplotlib
#1. 단순한 그래프 그리기
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,6,0.1)
y= np.sin(x)
plt.plot(x,y)
plt.show()

#2. pyplot 기능
x= np.arange(0,6,0.1)
y1= np.sin(x)
y2= np.cos(x)

plt.plot(x,y1,label="sin")
plt.plot(x,y2,label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin&cos function by jeongseon")
plt.legend()
plt.show()

#3. 이미지 표시하기
import matplotlib.pyplot as plt
from matplotlib.image import imread
img= imread('증명사진.jpg')
plt.imshow(img)
plt.show()