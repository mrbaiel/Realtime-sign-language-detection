import cv2
import os
import uuid
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Не удалось открыть камеру")
    exit()
IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

ret, frame = cap.read()
if ret:
    imgname = os.path.join(IMAGES_PATH, f"photo.{str(uuid.uuid1())}.jpg")
    cv2.imshow('Test Frame', frame)
    success = cv2.imwrite(IMAGES_PATH, frame)
    if success:
        print("Изображение успешно сохранено")
    else:
        print("Не удалось сохранить изображение")
    cv2.waitKey(0)
else:
    print("Не удалось захватить изображение")

cap.release()
cv2.destroyAllWindows()
