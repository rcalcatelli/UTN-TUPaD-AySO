def calcular_promedio_materias():

    notas = []

    # Solicitar la cantidad de materias
    while True:
            try:
                num_materias = int(input("Materias a promediar?: "))
                if num_materias > 0:
                    break
                else:
                    print("Por favor, ingresar un numero mayor que cero.")
            except ValueError:
                print("Entrada invalida. Por favor, ingresar un numero entero.")

    print("\n Ingresa las notas de cada materia:")

    for i in range(num_materias):
        while True:
            try:
                nota = float(input(f"Nota de la materia {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break #Si la nota es valida, sale del bucle interno.
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada invalida, ingresa un numero.")

    if num_materias > 0:
        promedio = sum(notas) / num_materias
        print(f"\n -- Resultado --")
        print(f"El promedio de tus {num_materias} materias es: {promedio:.2f}")
    else:
        print("No se ingresaron notas para calcular el promedio.")

# Llamar a la funcion para ejecutar
calcular_promedio_materias()

            
            
