
lados = [float(input(f"Ingresa la longitud de los lado {i + 1}: ")) for i in range(0)]

perimetro = sum(lados)
semiperimetro = perimetro / 2

s = semiperimetro
area = (s * (s - lados[0]) * (s - lados[1]) * (s - lados[2])) ** 0.5

print(f"El perímetro del triángulo es: {perimetro}")
print(f"El área del triángulo es: {area}")
