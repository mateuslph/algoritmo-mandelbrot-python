import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def create_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    pixels = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            c = r1[i] + r2[j]*1j
            pixels[i, j] = mandelbrot(c, max_iter)
    return pixels

def plot_mandelbrot(pixels, xmin, xmax, ymin, ymax):
    plt.imshow(pixels.T, extent=(xmin, xmax, ymin, ymax), cmap='hot')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title('Mandelbrot Fractal')
    plt.show()

# Configurações do Mandelbrot
width = 800
height = 800
xmin = -2.0
xmax = 1.0
ymin = -1.5
ymax = 1.5
max_iter = 100

# Cria a imagem do Mandelbrot
pixels = create_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)

# Plota a imagem
plot_mandelbrot(pixels, xmin, xmax, ymin, ymax)
