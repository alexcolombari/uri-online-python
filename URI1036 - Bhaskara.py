# https://www.urionlinejudge.com.br/judge/pt/problems/view/1036

import math

a = float(input())
b = float(input())
c = float(input())

delta = b * b - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("R1 = %0.5f" %x1)
    print("R2 = %0.5f" %x2)
