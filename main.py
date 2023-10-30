
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

perimetro = lado1 + lado2 + lado3
semiperimetro = perimetro / 2

area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5

# resultados.
print(f"El perímetro del triángulo es: {perimetro}")
print(f"El área del triángulo es: {area}")


