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

# MAX, x ∊ [-0.8, +0.8]  |  f(x) - Tn(x) |

x_vrijednosti = np.linspace(-0.8, 0.8, 1000)

greske_p1 = np.abs(f(x_vrijednosti) - p1(x_vrijednosti))        # f(), p1(), p2() i p3() s argumentom 'x_vrijednosti' vraća niz rezultata jer je 'x_vrijednosti' numpy array
greske_p2 = np.abs(f(x_vrijednosti) - p2(x_vrijednosti))
greske_p3 = np.abs(f(x_vrijednosti) - p3(x_vrijednosti))        # rezultat ovog (i gornjih dvoje) računa je niz razlika, odnosno grešaka za svaku od 1000 točaka

najveca_greska_p1 = np.max(greske_p1)
najveca_greska_p2 = np.max(greske_p2)
najveca_greska_p3 = np.max(greske_p3)

print(f"Najveća greška za p1: {najveca_greska_p1}")
print(f"Najveća greška za p2: {najveca_greska_p2}")
print(f"Najveća greška za p3: {najveca_greska_p3}")