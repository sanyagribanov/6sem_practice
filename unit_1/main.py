import cv2 as cv
import numpy as np
import math

# print("Координаты точки A(x1;y1):")
# x1 = int(input("\tx1 = "))
# y1 = int(input("\ty1 = "))
# print("Координаты точки B(x2;y2):")
# x2 = int(input("\tx2 = "))
# y2 = int(input("\ty2 = "))
# print("Координаты точки C(x1;y1):")
# x3 = int(input("\tx1 = "))
# y3 = int(input("\ty1 = "))
# print("Координаты точки D(x2;y2):")
# x4 = int(input("\tx2 = "))
# y4 = int(input("\ty2 = "))
x1 = 50
y1 = 50
x2 = 150
y2 = 150
x4 = 200
y4 = 20
x3 = 70
y3 = 200

print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
teta = math.atan(k)
b = y2 - k*x2
y = k * x2 + b

print(" y = %.2f*x + %.2f" % (k, b))


#создать изображение
img = np.zeros( (512, 512, 3), np.uint8)

#рисование линии
#cv.line(img,int(k), int(b), (0,0,255), 2,cv.LINE_8)

cv.line(img,(0,int(b)), (512, int(k * 512 + b)),(255,255,0), 2,cv.LINE_8)
cv.line(img,(x3,y3), (x4,y4),(255,0,0), 2,cv.LINE_8)

y3 = -x3 * math.sin(teta)+y3 * math.cos(0)
y4 = -x4 * math.sin(teta)+y4 * math.cos(0)

print(y3)
print(y4)
print(y)

if y3 < y < y4:
    print("Вошли")
    entrance = cv.putText(img, 'Entrance', (10, 50), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 2, cv.LINE_AA)
elif y4 < y < y3:
    print("Вышли")
    exit = cv.putText(img, 'Exit', (120, 500), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 2, cv.LINE_AA)
else:
    print("Нет пересечения")

#дисплей
cv.imshow('line', img)
cv.waitKey(20000)

#закрыть окно
cv.destroyAllWindows()
