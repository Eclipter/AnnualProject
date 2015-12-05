from PIL import Image, ImageFilter
import numpy as np
import mnist


def load_image(img_name='custom_img.png'):
    filename = format('data/' + str(img_name))
    img = Image.open(filename).convert('L').filter(ImageFilter.BLUR)
    img = img.resize((28, 28))
    pixels = list(img.getdata())
    i = 0
    for x in pixels:
        new_pixel = ((-1) * x + 255) / 255
        pixels[i] = new_pixel
        i += 1
    pixels = np.asarray(pixels, np.float32)
    mnist.plot_mnist_digit(np.reshape(pixels, (-1, 28)))
    reshaped_pixels = np.reshape(pixels, (784, 1))
    return reshaped_pixels
