import os
import cv2
import time
import uuid

# Задаем путь для сохранения изображений
IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')
labels = ['Привет', 'Спасибо', 'да', 'нет', 'я люблю тебя']
number_images = 15

# Создание директорий для меток
for label in labels:
    label_path = os.path.join(IMAGES_PATH, label)
    os.makedirs(label_path, exist_ok=True)

# Открытие камеры
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Не удалось открыть камеру")
    exit()

for label in labels:
    print(f"Собирается картина для {label}")
    time.sleep(5)
    for imgnum in range(number_images):
        ret, frame = cap.read()
        if not ret:
            print("Не удалось захватить изображение")
            continue

        print(f"Размер кадра: {frame.shape}, Тип: {frame.dtype}")

        imgname = os.path.join(IMAGES_PATH, label, f"{label}.{str(uuid.uuid1())}.jpg")
        cv2.imshow("camera", frame)
        success = cv2.imwrite(imgname, frame)
        if success:
            print(f"Изображение сохранено: {imgname}")
        else:
            print(f"Не удалось сохранить изображение: {imgname}")
            print(f"Путь: {imgname}")
            print(f"Права доступа: {os.access(os.path.dirname(imgname), os.W_OK)}")


        time.sleep(1)

        if cv2.waitKey(1) & 0xFF == 27:
            break

# Освобождение камеры и закрытие всех окон
cap.release()
cv2.destroyAllWindows()
