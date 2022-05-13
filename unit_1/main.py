import cv2 as cv
import numpy as np

print("Координаты точки A(x1;y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))
print("Координаты точки B(x2;y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print(" y = %.2f*x + %.2f" % (k, b))

#создать изображение
img = np.zeros( (512, 512, 3), np.uint8)

#рисование линии
cv.line(img,(k[0],b[0]), (212, 500), (0,0,255), 2,cv.LINE_8)

cv.line(img,(x1[0],y1[0]), (90, 500), (0,255,255), 2,cv.LINE_8)

cv.line(img,(x2[0],y2[0]), (30, 400), (0,255,0), 2,cv.LINE_8)


cv.putText(img,'Entrance',(10,50),cv.FONT_HERSHEY_PLAIN , 4,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'Exit',(120,500),cv.FONT_HERSHEY_PLAIN , 4,(255,255,255),2,cv.LINE_AA)

#дисплей
cv.imshow('line', img)
cv.waitKey(5000)

#закрыть окно
cv.destroyAllWindows()



