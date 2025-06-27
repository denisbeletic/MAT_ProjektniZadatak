import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + x**2)

def p1(x):
    return 1 - x**2

def p2(x):
    return 1 - x**2 + x**4

def p3(x):
    return 1 - x**2 + x**4 - x**6

x = np.linspace(-0.8, 0.8, 400)     # generira 400 brojeva, medusobno ravnomjerno rasporedeni u intervalu [-0.8, +0.8]

plt.plot(x, f(x), label='f(x) = 1 / (1 + x^2)', color='black')
plt.plot(x, p1(x), label='Taylorov 1. član')
plt.plot(x, p2(x), label='Taylorov 2. član')
plt.plot(x, p3(x), label='Taylorov 3. član')
plt.legend()
plt.title('Vizualizacija fj-e i Taylorovi polinomi')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()