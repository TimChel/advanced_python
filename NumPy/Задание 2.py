import imageio
# Напишите полностью векторизованный вариант
# Дан трёхмерный массив, содержащий изображение, размера (height, width, numChannels), а также вектор длины numChannels.
# Сложить каналы изображения с указанными весами, и вернуть результат в виде матрицы размера (height, width). Считать
# реальное изображение можно при помощи функции scipy.misc.imread (если изображение не в формате png, установите пакет
# pillow: conda install pillow). Преобразуйте цветное изображение в оттенки серого, использовав коэффициенты
# np.array([0.299, 0.587, 0.114]).

massiv_img = imageio.imread('img.png')
print(massiv_img.shape)
massiv_bw_img = massiv_img[:, :, 0]*0.299 + massiv_img[:, :, 1]*0.587 + massiv_img[:, :, 2]*0.114
imageio.imwrite('img_2.png', massiv_bw_img)


