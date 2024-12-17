import pandas as pd
from matplotlib import pyplot as plt
import random
#from tqdm import tqdm
import numpy as np
from PIL import Image
img = Image.open('homak.png')
arr = np.array(img)

# Определение размеров
rows, cols, colors = arr.shape

# Ядро свертки (в данном случае просто пример)
A = np.ones((3, 3))  # Вы можете использовать свое ядро, например, для размытия
A /= A.sum()  # Нормализация ядра, чтобы сумма всех значений была равна 1


# Свертка по каждому каналу
for i in range(rows - 2):
    for j in range(cols - 2):
        # Инициализация временных переменных для хранения суммы цветовых значений
        sum_red = 0
        sum_green = 0
        sum_blue = 0

        for m in range(3):
            for n in range(3):
                # Умножение значений пикселей на соответствующие значения из ядра
                sum_red += arr[i + m, j + n, 0] * A[m, n]
                sum_green += arr[i + m, j + n, 1] * A[m, n]
                sum_blue += arr[i + m, j + n, 2] * A[m, n]

        # Заполнение результирующих массивов
        B_red[i, j] = sum_red
        B_green[i, j] = sum_green
        B_blue[i, j] = sum_blue
        # Преобразование результатов в диапазон [0, 255] и тип uint8
B_red = np.clip(B_red, 0, 255).astype(np.uint8)
B_green = np.clip(B_green, 0, 255).astype(np.uint8)
B_blue = np.clip(B_blue, 0, 255).astype(np.uint8)


# Визуализация значений каждого канала в виде глубин пикселей в цельной картинке
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(B_red, cmap='Reds')
axes[0].set_title('Red Channel')
axes[0].axis('off')

axes[1].imshow(B_green, cmap='Greens')
axes[1].set_title('Green Channel')
axes[1].axis('off')

axes[2].imshow(B_blue, cmap='Blues')
axes[2].set_title('Blue Channel')
axes[2].axis('off')

plt.show()

img = Image.open('homak.png').convert('L')

arr = np.array(img)

rows, cols = arr.shape

# Определение вертикального фильтра Собеля
sobel_vertical = np.array([[1, 0, -1],
                            [2, 0, -2],
                            [1, 0, -1]])

# Массив для хранения отфильтрованного изображения
filtered_image = np.zeros((rows-2, cols-2), dtype=np.int16)

# Применение фильтра Собеля
for i in range(1, rows-1):
    for j in range(1, cols-1):
        # Свертка
        filtered_value = int(0)
        for m in range(3):
            for n in range(3):
                filtered_value += arr[i+m-1, j+n-1] * sobel_vertical[m, n]
        filtered_image[i-1, j-1] = filtered_value

# Нормализация результатов для отображения
filtered_image_normalized = np.clip(filtered_image, 0, 255).astype(np.uint8)


# Визуализация оригинального и отфильтрованного изображений
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(arr, cmap='gray')
axes[0].set_title('Оригинальное изображение')
axes[0].axis('off')

axes[1].imshow(filtered_image_normalized, cmap='gray')
axes[1].set_title('Изображение после фильтра Собеля')
axes[1].axis('off')

plt.show()