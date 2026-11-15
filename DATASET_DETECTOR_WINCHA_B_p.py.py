import cv2
import numpy as np
import imutils
import os

Datos = "p"              # Crear carpeta denominada p (Positivos)
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture("http://192.168.18.24:4747/video")

x1, y1 = 120, 40
x2, y2 = 550, 450

count = 0
print("=== MODO POSITIVOS (WINCHA) ===")
print("Coloca la wincha en el recuadro y presiona 's' para guardar. ESC para salir.")

while True:
    ret, frame = cap.read()
    if ret == False: break
    imAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    objeto = imAux[y1:y2, x1:x2]
    objeto = imutils.resize(objeto, width=38)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        cv2.imwrite(Datos + '/objeto_{}.jpg'.format(count), objeto)
        print('Imagen POSITIVA guardada: ' + Datos + '/objeto_{}.jpg'.format(count))
        count = count + 1
    if k == 27:
        break

    cv2.imshow('frame - POSITIVOS', frame)
    cv2.imshow('objeto recortado', objeto)

cap.release()
cv2.destroyAllWindows()
